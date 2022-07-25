import pandas as pd
from utils.database import queries
from utils.database.connection import cnxn
from datetime import datetime
from utils.functions.functions import determine_vehicle_power_type
from utils.functions.vehicle_spend import all_fleet_split
from utils.functions.hire_splitter import report_for_hire_splitter


def merged_query():
    vehicles_hires_customers = pd.read_sql(str(queries.af_vehicle_and_hire_and_customer_query), cnxn)
    addresses = pd.read_sql(str(queries.af_address_query), cnxn)
    finance = pd.read_sql(str(queries.af_finance_query), cnxn)
    merged = vehicles_hires_customers.merge(
        right=addresses,
        how="left",
        left_on="supplier_ID",
        right_on="organisation_ID")
    merged = merged.merge(
        right=finance,
        how="left",
        left_on="last_finance_unique_id",
        right_on="finance_id")
    merged['Current_Contract_Expiry_Month'] = merged.apply(lambda x: x['hire_expiry_date'].month, axis=1)
    merged['Current_Contract_Expiry_Year'] = merged.apply(lambda x: x['hire_expiry_date'].year, axis=1)
    merged['Contract_Billing_Amount_Monthly'] = merged.apply(contract_billing_amount_monthly, axis=1)
    merged['Contract_Billing_Amount_Weekly'] = merged.apply(contract_billing_amount_weekly, axis=1)
    merged['Contract_Billing_Amount_Annually'] = merged.apply(contract_billing_amount_yearly,  axis=1)
    merged['Days_On_Rent'] = merged.apply(days_on_rent, axis=1)
    merged['mileage_difference'] = merged.apply(mileage_difference, axis=1)
    merged['daily_mileage'] = merged.apply(daily_mileage, axis=1)
    merged['projected_end_mileage'] = merged.apply(projected_end_mileage, axis=1)
    merged['rated_mileage_at_reading_date'] = merged.apply(rated_mileage_at_reading_date, axis=1)
    merged['over_under_rated_mileage_number'] = \
        merged.apply(lambda x: x['mileage'] - x['rated_mileage_at_reading_date'], axis=1)
    merged['over_under_rated_mileage_percentage'] = merged.apply(over_under_mileage_percent, axis=1)
    merged['power_type'] = merged.apply(determine_vehicle_power_type, axis=1)
    customer_fleet_numbers = total_hexagon_fleet(merged)
    merged['customer_powered_fleet'] = merged.apply(count_fleet, args=(customer_fleet_numbers, "Power Fleet"), axis=1)
    merged['customer_trailer_fleet'] = merged.apply(count_fleet, args=(customer_fleet_numbers, "Trailer Fleet"), axis=1)
    merged['customer_ancillary_fleet'] = \
        merged.apply(count_fleet, args=(customer_fleet_numbers, "Ancillary Unit"), axis=1)
    merged['customer_undefined_fleet'] = merged.apply(count_fleet, args=(customer_fleet_numbers, "Undefined"), axis=1)
    spend_split = all_fleet_split()
    merged['3_month_spend'] = merged.apply(lookup_spend_split,args=(spend_split,'3'), axis=1)
    merged['12_month_spend'] = merged.apply(lookup_spend_split, args=(spend_split, '12'), axis=1)
    merged['life_spend'] = merged.apply(lookup_spend_split, args=(spend_split, 'Life'), axis=1)
    revenue_split = report_for_hire_splitter()
    merged['3_month_revenue'] = merged.apply(lookup_revenue_split,args=(revenue_split,'3'), axis=1)
    merged['12_month_revenue'] = merged.apply(lookup_revenue_split, args=(revenue_split, '12'), axis=1)
    merged['life_revenue'] = merged.apply(lookup_revenue_split, args=(revenue_split, 'Life'), axis=1)
    return merged


def contract_billing_amount_monthly(vehicle):
    if vehicle['billing_frequency'] == "Monthly":
        return vehicle['sales']
    elif vehicle['billing_frequency'] == "Weekly":
        return (vehicle['sales']*52)/12
    else:
        return None


def contract_billing_amount_weekly(vehicle):
    if vehicle['billing_frequency'] == "Monthly":
        return (vehicle['sales'] * 12)/52
    elif vehicle['billing_frequency'] == "Weekly":
        return vehicle['sales']
    else:
        return None


def contract_billing_amount_yearly(vehicle):
    if vehicle['billing_frequency'] == "Monthly":
        return vehicle['sales']*12
    elif vehicle['billing_frequency'] == "Weekly":
        return vehicle['sales']*52
    else:
        return None


def days_on_rent(vehicle):
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


def mileage_difference(vehicle):
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


def over_under_mileage_percent(vehicle):
    try:
        return round((vehicle['rated_mileage_at_reading_date'] / vehicle['mileage']) / 100)
    except:
        return None


def total_hexagon_fleet(table):
    customers_and_vehicles = {}
    for row in table.iterrows():
        customer_id = row[1][19]
        power_type = row[1][51]
        if customer_id in customers_and_vehicles.keys():
            if power_type in customers_and_vehicles[customer_id].keys():
                customers_and_vehicles[customer_id][power_type] += 1
            else:
                customers_and_vehicles[customer_id][power_type] = 1
        else:
            customers_and_vehicles[customer_id] = {}
            customers_and_vehicles[customer_id][power_type] = 1
    return customers_and_vehicles


def count_fleet(vehicle, lookup_table, power_type):
    try:
        return lookup_table[vehicle['customer_ID']][power_type]
    except:
        return None


def lookup_spend_split(vehicle, lookup_table, month):
    try:
        return lookup_table[vehicle['vehicle_id']][month]
    except:
        return None


def lookup_revenue_split(vehicle, lookup_table, month):
    try:
        return lookup_table[vehicle['vehicle_id']][month]
    except:
        return None