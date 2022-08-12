import tempfile

import pandas as pd
from utils.database import queries
from utils.database.connection import cnxn
from datetime import datetime
from dotenv import load_dotenv
import os

from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

from utils.functions.finance_splitter import report_for_agreement_splitter
from utils.functions.functions import determine_vehicle_power_type
from utils.functions.rfl_splitter import report_for_rfl_splitter
from utils.functions.vehicle_spend import all_fleet_split
from utils.functions.hire_splitter import report_for_hire_splitter
import utils.asset_file.excel_column_orders as co


load_dotenv()
sharepoint_site_url = os.getenv("SHAREPOINTASSETFILESITEURL")
sharepoint_username = os.getenv("SHAREPOINTASSETFILEUSER")
sharepoint_password = os.getenv("SHAREPOINTASSETFILEPASSWORD")
sharepoint_file_path = os.getenv("SHAREPOINTASSETMASTERFILEFILEURL")

master_frame = None


def asset_file_generation(tidy_names: bool = False,
                          account_manager: bool = None,
                          stood_fleet: bool = False,
                          existing_fleet: bool = True,
                          layout = None):
    # Get Master File For Comparison Purposes
    global master_frame
    ctx = ClientContext(sharepoint_site_url).with_credentials(UserCredential(sharepoint_username,sharepoint_password))
    download_path = os.path.join(tempfile.mkdtemp(), os.path.basename(sharepoint_file_path))
    with open(download_path, 'wb') as local_file:
        file = ctx.web.get_file_by_server_relative_path(sharepoint_file_path).download(local_file).execute_query()
        master_frame = pd.read_excel(download_path, index_col='Registration')

    # Queries That Need To Be Referred To (Need to Make these Async For Performance)
    vehicles_hires_customers = pd.read_sql(str(queries.af_vehicle_and_hire_and_customer_query), cnxn)
    addresses = pd.read_sql(str(queries.af_address_query), cnxn)
    finance = pd.read_sql(str(queries.af_finance_query), cnxn)
    spend_split = all_fleet_split(vehicles_hires_customers)
    revenue_split = report_for_hire_splitter(vehicles_hires_customers)
    finance_split = report_for_agreement_splitter(vehicles_hires_customers)
    rfl_split = report_for_rfl_splitter(vehicles_hires_customers)

    # DataFrame Creation
    df = vehicles_hires_customers.merge(
        right=addresses,
        how="left",
        left_on="supplier_ID",
        right_on="organisation_ID")
    df = df.merge(
        right=finance,
        how="left",
        left_on="last_finance_unique_id",
        right_on="finance_id")

    if existing_fleet:
        df = df[~df[['vehicle_status']].isin(['No longer on fleet', 'Vehicle On Order']).any(axis=1)]

    if stood_fleet:
        df = df[df['customer_name'] == "Not On Hire"]

    if account_manager:
        df = df[~df['relationship_manager'] == account_manager]

    df['registration_2'] = df['registration']
    df['vehicle_type_2'] = df['vehicle_type']
    df['hire_expiry_date_2'] = df['hire_expiry_date'].dt.strftime('%d/%m/%Y')
    df['Current_Contract_Expiry_Month'] = df.apply(lambda x: x['hire_expiry_date'].month, axis=1)
    df['Current_Contract_Expiry_Year'] = df.apply(lambda x: x['hire_expiry_date'].year, axis=1)
    df['Contract_Billing_Amount_Monthly'] = df.apply(contract_billing_amount_monthly, axis=1)
    df['Contract_Billing_Amount_Weekly'] = df.apply(contract_billing_amount_weekly, axis=1)
    df['Contract_Billing_Amount_Annually'] = df.apply(contract_billing_amount_yearly,  axis=1)
    df['Days_On_Rent'] = df.apply(days_on_rent, axis=1)
    df['mileage_difference'] = df.apply(mileage_difference, axis=1)
    df['daily_mileage'] = df.apply(daily_mileage, axis=1)
    df['projected_end_mileage'] = df.apply(projected_end_mileage, axis=1)
    df['rated_mileage_at_reading_date'] = df.apply(rated_mileage_at_reading_date, axis=1)
    df['over_under_rated_mileage_number'] = df.apply(over_under_rated_mileage_number, axis=1)
    df['over_under_rated_mileage_percentage'] = df.apply(over_under_mileage_percent, axis=1)
    df['power_type'] = df.apply(determine_vehicle_power_type, axis=1)

    customer_fleet_numbers = total_hexagon_fleet(df)

    df['hexagon_powered_fleet'] = df.apply(count_fleet, args=(customer_fleet_numbers, "Power Fleet"), axis=1)
    df['hexagon_trailer_fleet'] = df.apply(count_fleet, args=(customer_fleet_numbers, "Trailer Fleet"), axis=1)
    df['hexagon_ancillary_fleet'] = df.apply(count_fleet, args=(customer_fleet_numbers, "Ancillary Unit"), axis=1)
    df['hexagon_undefined_fleet'] = df.apply(count_fleet, args=(customer_fleet_numbers, "Undefined"), axis=1)
    df['total_customer_fleet'] = df.apply(total_customer_fleet, args=(customer_fleet_numbers,), axis=1)
    df['3_month_spend'] = df.apply(lookup_split,args=(spend_split, '3'), axis=1)
    df['12_month_spend'] = df.apply(lookup_split, args=(spend_split, '12'), axis=1)
    df['life_spend'] = df.apply(lookup_split, args=(spend_split, 'Life'), axis=1)
    df['3_month_revenue'] = df.apply(lookup_split,args=(revenue_split, '3'), axis=1)
    df['12_month_revenue'] = df.apply(lookup_split, args=(revenue_split, '12'), axis=1)
    df['life_revenue'] = df.apply(lookup_split, args=(revenue_split, 'Life'), axis=1)
    df['3_month_finance'] = df.apply(lookup_split, args=(finance_split,'3'), axis=1)
    df['12_month_finance'] = df.apply(lookup_split, args=(finance_split, '12'), axis=1)
    df['life_finance'] = df.apply(lookup_split, args=(finance_split, 'Life'), axis=1)
    df['3_month_rfl'] = df.apply(lookup_split, args=(rfl_split,'3'), axis=1)
    df['12_month_rfl'] = df.apply(lookup_split, args=(rfl_split, '12'), axis=1)
    df['life_rfl'] = df.apply(lookup_split, args=(rfl_split, 'Life'), axis=1)
    df['3_month_margin'] = df.apply(lambda x: x['3_month_revenue'] - (x['3_month_spend'] + x['3_month_finance'] + + x['3_month_rfl']), axis=1)
    df['3_month_margin_%'] = df.apply(three_month_margin_percent, axis=1)
    df['12_month_margin'] = df.apply(lambda x: x['12_month_revenue'] - (x['12_month_spend'] + x['12_month_finance'] + x['12_month_rfl']), axis=1)
    df['12_month_margin_%'] = df.apply(twelve_month_margin_percent, axis=1)
    df['life_margin'] = df.apply(lambda x: x['life_revenue'] - (x['life_spend'] + x['life_finance'] + x['life_rfl']), axis=1)
    df['life_margin_%'] = df.apply(life_margin_percent, axis=1)
    df['customer_status'] = df['account_status']
    df['in_scope'] = df.apply(calculate_in_scope, axis=1)
    df['engagement_level'] = df.apply(lookup_from_master, args=('Engagement Level',), axis=1)
    df['current_view'] = df.apply(lookup_from_master, args=('Current View',), axis=1)
    df['expected_return_date'] = df['hire_expiry_date'].dt.strftime('%d/%m/%Y')
    df['second_decision'] = df.apply(lookup_from_master, args=('2nd Decision',), axis=1)
    df['expected_return_date_2'] = df['hire_expiry_date'].dt.strftime('%d/%m/%Y')
    df['plan_view'] = df.apply(lookup_from_master, args=('Plan View',), axis=1)
    df['product_manager_view'] = df.apply(lookup_from_master, args=('Product Manager View',), axis=1)
    df['product_manager_return_date'] = df.apply(lookup_from_master, args=('Product Manager Return Date',), axis=1)
    df['mileage_banding'] = df.apply(calculate_mileage_banding, axis=1)
    df['up_priced'] = df.apply(lookup_from_master, args=('Up Priced',), axis=1)
    df['latest_increase'] = df.apply(lookup_from_master, args=('Latest Increase',), axis=1)
    df['effective_date'] = df.apply(lookup_from_master, args=('Effective Date',), axis=1)
    df['segment'] = None
    df['years_in_service'] = df.apply(years_in_service, axis=1)
    df['fridge'] = None
    df['capital'] = None
    df['contract_status'] = df.apply(calculate_contract_status, axis=1)
    df['hire_expiry_date'] = df['hire_expiry_date'].dt.strftime('%d/%m/%Y')
    df['vehicle_on_fleet_date'] = df['vehicle_on_fleet_date'].dt.strftime('%d/%m/%Y')
    df['mileage_date'] = df['mileage_date'].dt.strftime('%d/%m/%Y')
    df['hire_start_date'] = df['hire_start_date'].dt.strftime('%d/%m/%Y')
    df['original_hire_date'] = df['original_hire_date'].dt.strftime('%d/%m/%Y')
    df['finance_end_date'] = df['finance_end_date'].dt.strftime('%d/%m/%Y')

    # Tidying DataFrame

    if not layout:
        df = df[co.default_order]
    else:
        pass

    rename_dictionary = \
    {
        'vehicle_status': 'Vehicle Status',
        'customer_group': 'Customer Group',
        'relationship_manager': 'Account Manager',
        'vehicle_type': 'Vehicle Type',
        'registration': 'Registration',
        'hire_expiry_date': 'Hire End Date',
        'customer_status': 'Customer Status',
        'in_scope': 'In Scope?',
        'engagement_level': 'Engagement Level',
        'current_view': 'Current View',
        'expected_return_date': 'Expected Return Date',
        'second_decision': '2nd Decision',
        'expected_return_date_2': 'Expected Return Date',
        'plan_view': 'Plan View',
        'product_manager_view': 'Product Manager View',
        'product_manager_return_date': 'Product Manager Return Date',
        'mileage_banding': 'Mileage Banding',
        'up_priced': 'Up Priced',
        'latest_increase': 'Latest Increase',
        'effective_date': 'Effective Date',
        'customer_acc_number': 'Customer Account Number',
        'customer_name': 'Customer Name',
        'segment': 'Segment',
        'hexagon_powered_fleet': 'Hexagon Powered Fleet',
        'hexagon_trailer_fleet': 'Hexagon Trailer Fleet',
        'hexagon_ancillary_fleet': 'Hexagon Ancillary Fleet',
        'hexagon_undefined_fleet': 'Hexagon Undefined Fleet',
        'total_customer_fleet': 'Total Hexagon Fleet',
        'power_type': 'Power Type',
        'vehicle_on_fleet_date': 'Vehicle On Fleet Date',
        'years_in_service': 'Years In Service',
        'manufacturer': 'Manufacturer',
        'model': 'Model',
        'parent_type': 'Parent vehicle Type',
        'fridge': 'Fridge?',
        'supplier_name': 'Supplier name',
        'supplier_post_code': 'Supplier Post Code',
        'mileage': 'Current Mileage',
        'mileage_date': 'Mileage Reading Date',
        'daily_mileage': 'Daily Mileage',
        'projected_end_mileage': 'Project Mileage At Contract End',
        'contract_annual_mileage': 'Contract Annual Mileage Allowance',
        'rated_mileage_at_reading_date': 'Rated Mileage @ Reading Date',
        'over_under_rated_mileage_number': 'Over/Under Rated Mileage @ Reading Date',
        'over_under_rated_mileage_percentage': 'Over/Under Rated Mileage % @ Reading Date',
        'financer': 'Financer',
        'capital': 'Capital',
        'net_book_value': 'NBV',
        'residual_value': 'Residual',
        'finance_end_date': 'Finance End Date',
        'monthly_depreciation': 'Monthly Depreciation',
        'hire_start_date': 'Hire Start Date',
        'original_hire_date': 'Original Hire Start Date',
        'Contract_Billing_Amount_Monthly': 'Contract Billing Amount(Monthly)',
        'Contract_Billing_Amount_Annually': 'Contract Billing Amount(Annually)',
        'Contract_Billing_Amount_Weekly': 'Contract Billing Amount(Weekly)',
        'billing_frequency': 'Billing Frequency',
        'Current_Contract_Expiry_Month': 'Current Contract Expiry Month',
        'Current_Contract_Expiry_Year': 'Current Contract Expiry Year',
        'contract_status': 'Contract Status',
        '3_month_revenue': '3 Month Revenue',
        '3_month_spend': '3 Month Expenditure',
        '3_month_margin': '3 Month Margin',
        '3_month_margin_%': '3 Month Margin %',
        '12_month_revenue': '12 Month Revenue',
        '12_month_spend': '12 Month Expenditure',
        '12_month_margin': '12 Month Margin',
        '12_month_margin_%': '12 Month Margin %',
        'life_revenue': 'Life Revenue',
        'life_spend': 'Life Expenditure',
        'life_margin': 'Life Margin',
        'life_margin_%': 'Life Margin %',
        'registration_2': 'Registration 2',
        'vehicle_type_2': 'Vehicle Type 2',
        'hire_expiry_date_2': 'Hire End Date 2',
        '3_month_finance': '3 Month Finance',
        '12_month_finance': '12 Month Finance',
        'life_finance': 'Life Finance',
        '3_month_rfl': '3 Month RFL',
        '12_month_rfl': '12 Month RFL',
        'life_rfl': 'Life RFL',
    }

    # Check to see if the columns need renaming or not
    if tidy_names:
        df.rename(columns=rename_dictionary, inplace=True)

    return df


# Apply Functions
def contract_billing_amount_monthly(vehicle) -> float | None:
    if vehicle['billing_frequency'] == "Monthly":
        return round(vehicle['sales'], 2)
    elif vehicle['billing_frequency'] == "Weekly":
        return round((vehicle['sales']*52)/12, 2)
    else:
        return None


def contract_billing_amount_weekly(vehicle) -> float | None:
    if vehicle['billing_frequency'] == "Monthly":
        return round((vehicle['sales'] * 12)/52, 2)
    elif vehicle['billing_frequency'] == "Weekly":
        return round(vehicle['sales'], 2)
    else:
        return None


def contract_billing_amount_yearly(vehicle) -> float | None:
    if vehicle['billing_frequency'] == "Monthly":
        return round(vehicle['sales']*12, 2)
    elif vehicle['billing_frequency'] == "Weekly":
        return round(vehicle['sales']*52, 2)
    else:
        return None


def years_in_service(vehicle) -> int | None:
    delta = datetime.now() - vehicle['vehicle_on_fleet_date']
    try:
        return int(delta.days / 365)
    except:
        return None


def days_on_rent(vehicle) -> int:
    _start_date = vehicle['hire_start_date']
    today = datetime.now()
    original_hire_date = vehicle['original_hire_date']
    _days_on_rent = None

    if pd.notnull(original_hire_date):
        _start_date = original_hire_date
    _days_on_rent = (today - _start_date).total_seconds() / 86400

    try:
        _days_on_rent = round(_days_on_rent)
    except:
        _days_on_rent = None

    return _days_on_rent


def mileage_difference(vehicle) -> int:
    start_mileage = vehicle['hire_start_mileage']

    if pd.notnull(vehicle['original_hire_mileage']):
        start_mileage = vehicle['original_hire_mileage']

    return vehicle['mileage'] - start_mileage


def daily_mileage(vehicle):
    try:
        _daily_mileage = round(vehicle['mileage_difference'] / vehicle['Days_On_Rent'])
    except:
        _daily_mileage = None

    return _daily_mileage


def projected_end_mileage(vehicle):
    days_until_end = (vehicle['hire_expiry_date'] - datetime.now()).total_seconds() / 86400

    try:
        days_until_end = round(days_until_end)
    except:
        days_until_end = None

    try:
        projected_additional_mileage = vehicle['daily_mileage'] * days_until_end
    except:
        projected_additional_mileage = None

    try:
        projected_end_mileage = projected_additional_mileage + vehicle['mileage']
    except:
        projected_end_mileage = None

    return projected_end_mileage


def rated_mileage_at_reading_date(vehicle):
    daily_allowance = vehicle['contract_annual_mileage'] / 365
    start_mileage = vehicle['hire_start_mileage']

    if pd.notnull(vehicle['original_hire_mileage']):
        start_mileage = vehicle['original_hire_mileage']

    try:
        return round(start_mileage + (daily_allowance * vehicle['Days_On_Rent']))
    except:
        return None


def over_under_rated_mileage_number(vehicle):
    try:
        return  vehicle['mileage'] - vehicle['rated_mileage_at_reading_date']
    except:
        pass


def over_under_mileage_percent(vehicle):
    try:
        return round((vehicle['rated_mileage_at_reading_date'] / vehicle['mileage']) / 100)
    except:
        return None


def total_hexagon_fleet(table):
    customers_and_vehicles = {}
    for row in table.iterrows():
        customer_group = row[1].loc['customer_group']
        power_type = row[1].loc['power_type']
        if customer_group in customers_and_vehicles.keys():
            if power_type in customers_and_vehicles[customer_group].keys():
                customers_and_vehicles[customer_group][power_type] += 1
            else:
                customers_and_vehicles[customer_group][power_type] = 1
        else:
            customers_and_vehicles[customer_group] = {}
            customers_and_vehicles[customer_group][power_type] = 1
    return customers_and_vehicles


def count_fleet(vehicle, lookup_table, power_type):
    try:
        return lookup_table[vehicle['customer_group']][power_type]
    except:
        return None


def total_customer_fleet(vehicle, lookup_table):
    try:
        return sum(lookup_table[vehicle['customer_group']].values(), 0)
    except:
        return None


def lookup_split(vehicle, lookup_table, month):
    try:
        return lookup_table[vehicle['vehicle_id']][month]
    except:
        return None


def three_month_margin_percent(vehicle) -> float | None:
    try:
        return (vehicle['3_month_revenue'] - (vehicle['3_month_spend'] + vehicle['3_month_finance'] + vehicle['3_month_rfl'])) / vehicle['3_month_revenue']
    except:
        return None


def twelve_month_margin_percent(vehicle) -> float | None:
    try:
        return (vehicle['12_month_revenue'] - (vehicle['12_month_spend'] + vehicle['12_month_finance'] + vehicle['12_month_rfl'])) / vehicle['12_month_revenue']
    except:
        return None


def life_margin_percent(vehicle) -> float | None:
    try:
        return (vehicle['life_revenue'] - (vehicle['life_spend'] + vehicle['life_finance'] + vehicle['life_rfl'])) / vehicle['life_revenue']
    except:
        return None


def calculate_contract_status(vehicle):
    match vehicle['hire_type_name']:
        case 'Admin':
            return 'Admin Vehicle'
        case 'Captive Sub' | 'Replacement':
            return 'Replacement'
        case 'Contract' | 'Contract Hire':
            return 'Contract Hire'
        case 'Cross Hire':
            return 'Cross Hire'
        case 'Customer own Vehicle':
            return 'Customer Own Vehicle'
        case 'Fleet Management':
            return 'Fleet Management'
        case 'PAYG':
            return 'PAYG'
        case 'Peak':
            return 'Peak'
        case 'Spot Hire':
            return 'Spot Hire'
        case None:
            return 'Not On Hire'
        case _:
            return "Undefined Hire Type"


def calculate_in_scope(vehicle):
    try:
        months_until_end = (((vehicle['hire_expiry_date'] - datetime.today()).days / 365) * 12) + 1
        if months_until_end <= 6:
            return 'Yes'
        else:
            pass
    except:
        pass


def calculate_mileage_banding(vehicle):
    over_under_mileage = vehicle['over_under_rated_mileage_number']
    try:
        if over_under_mileage <= 0:
            return 'Green'
        elif over_under_mileage > 0 and over_under_mileage < 50000:
            return 'Amber'
        elif over_under_mileage >= 50000:
            return 'Red'
        else:
            return None
    except:
        pass


def lookup_from_master(vehicle, lookup):
    global master_frame
    try:
        return master_frame.loc[vehicle.loc['registration']][lookup]
    except:
        pass

