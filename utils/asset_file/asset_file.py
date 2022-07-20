import pandas as pd
from utils.database import queries
from utils.database.connection import cnxn
from datetime import datetime
from utils.functions.functions import determine_vehicle_power_type


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
    merged['Current_Contract_Expiry_Month'] = merged.apply(contract_expiry_month, axis=1)
    merged['Current_Contract_Expiry_Year'] = merged.apply(contract_expiry_year, axis=1)
    merged['Contract_Billing_Amount_Monthly'] = merged.apply(contract_billing_amount_monthly, axis=1)
    merged['Contract_Billing_Amount_Weekly'] = merged.apply(contract_billing_amount_weekly, axis=1)
    merged['Contract_Billing_Amount_Annually'] = merged.apply(contract_billing_amount_yearly,  axis=1)
    merged['Days_On_Rent'] = merged.apply(days_on_rent, axis=1)
    merged['mileage_difference'] = merged.apply(mileage_difference, axis=1)
    merged['daily_mileage'] = merged.apply(daily_mileage, axis=1)
    merged['projected_end_mileage'] = merged.apply(projected_end_mileage, axis=1)
    merged['rated_mileage_at_reading_date'] = merged.apply(rated_mileage_at_reading_date, axis=1)
    merged['over_under_rated_mileage_number'] = merged.apply(over_under_mileage_amount, axis=1)
    merged['over_under_rated_mileage_percentage'] = merged.apply(over_under_mileage_percent, axis=1)
    merged['power_type'] = merged.apply(determine_vehicle_power_type, axis=1)

    customer_fleet_numbers = total_hexagon_fleet(merged)

    merged['customer_powered_fleet'] = merged.apply(count_fleet, args=(customer_fleet_numbers, "Power Fleet"), axis=1)
    merged['customer_trailer_fleet'] = merged.apply(count_fleet, args=(customer_fleet_numbers, "Trailer Fleet"), axis=1)
    merged['customer_ancillary_fleet'] = merged.apply(count_fleet, args=(customer_fleet_numbers, "Ancillary Unit"), axis=1)
    merged['customer_undefined_fleet'] = merged.apply(count_fleet, args=(customer_fleet_numbers, "Undefined"), axis=1)
    return merged


def contract_expiry_month(vehicle):
    return vehicle['hire_expiry_date'].month


def contract_expiry_year(vehicle):
    return vehicle['hire_expiry_date'].year


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
    start_date = vehicle['hire_start_date']
    todays_date = datetime.now()
    original_hire_date = vehicle['original_hire_date']
    days_on_rent = None

    if pd.notnull(original_hire_date):
        start_date = original_hire_date

    days_on_rent = (todays_date - start_date).total_seconds() / 86400

    try:
        days_on_rent = round(days_on_rent)
    except:
        days_on_rent = None

    return days_on_rent


def mileage_difference(vehicle):
    start_mileage = vehicle['hire_start_mileage']
    current_mileage = vehicle['mileage']
    original_hire_mileage = vehicle['original_hire_mileage']

    if pd.notnull(original_hire_mileage):
        start_mileage = original_hire_mileage

    return current_mileage - start_mileage


def daily_mileage(vehicle):
    _mileage_difference = vehicle['mileage_difference']
    _days_on_rent = vehicle['Days_On_Rent']
    daily_mileage = None

    try:
        daily_mileage = _mileage_difference / _days_on_rent
    except:
        daily_mileage = None

    try:
        daily_mileage = round(daily_mileage)
    except:
        daily_mileage = None
    return daily_mileage


def projected_end_mileage(vehicle):
    todays_date = datetime.now()
    hire_end_date = vehicle['hire_expiry_date']
    days_until_end = (hire_end_date - todays_date).total_seconds() / 86400
    projected_additional_mileage = None
    projected_end_mileage = None

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
    annual_mileage_allowance = vehicle['contract_annual_mileage']
    daily_allowance = annual_mileage_allowance / 365
    days_on_rent = vehicle['Days_On_Rent']
    start_mileage = vehicle['hire_start_mileage']
    original_hire_mileage = vehicle['original_hire_mileage']

    if pd.notnull(original_hire_mileage):
        start_mileage = original_hire_mileage

    expected_mileage = start_mileage + (daily_allowance * days_on_rent)
    try:
        return round(expected_mileage)
    except:
        return expected_mileage


def over_under_mileage_amount(vehicle):
    return vehicle['mileage'] - vehicle['rated_mileage_at_reading_date']


def over_under_mileage_percent(vehicle):
    try:
        return round((vehicle['rated_mileage_at_reading_date'] / vehicle['mileage']) / 100)
    except:
        return None


def total_hexagon_fleet(table):
    customers_and_vehicles = {}
    for row in table.iterrows():
        customer_id = row[1][18]
        power_type = row[1][50]
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
    customer_id = vehicle['customer_ID']
    try:
        return lookup_table[customer_id][power_type]
    except:
        return None
