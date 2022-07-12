import pandas as pd
from utils.database import queries
from utils.database.connection import cnxn
from datetime import datetime


def merged_query():
    vehicles_hires_customers = pd.read_sql(str(queries.af_vehicle_and_hire_and_customer_query), cnxn)
    addresses = pd.read_sql(str(queries.af_address_query), cnxn)
    #finance = pd.read_sql(str(queries.af_finance_query), cnxn)
    merged = vehicles_hires_customers.merge(
        right=addresses,
        how="left",
        left_on="supplier_ID",
        right_on="organisation_ID")
    #merged = merged.merge(
    #    right=finance,
    #    how="left",
    #    left_on="finance_agreement_number",
    #    right_on="finance_agreement_number")
    merged['Current_Contract_Expiry_Month'] = merged.apply(contract_expiry_month, axis=1)
    merged['Current_Contract_Expiry_Year'] = merged.apply(contract_expiry_year, axis=1)
    merged['Contract_Billing_Amount_Monthly'] = merged.apply(contract_billing_amount_monthly, axis=1)
    merged['Contract_Billing_Amount_Weekly'] = merged.apply(contract_billing_amount_weekly, axis=1)
    merged['Contract_Billing_Amount_Annually'] = merged.apply(contract_billing_amount_yearly,  axis=1)
    merged['Days_On_Rent'] = merged.apply(days_on_rent, axis=1)
    merged['mileage_difference'] = merged.apply(mileage_difference, axis=1)
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
    start_mileage = vehicle['hire_start_mileage']
    todays_date = datetime.now()
    current_mileage = vehicle['mileage']
    original_hire_date = vehicle['original_hire_date']
    original_hire_mileage = vehicle['original_hire_mileage']

    if pd.notnull(original_hire_date):
        start_date = original_hire_date

    if pd.notnull(original_hire_mileage):
        start_mileage = original_hire_mileage

    if not pd.notnull(current_mileage):
        current_mileage = 1

    if not pd.notnull(start_mileage):
        start_mileage = 1

    try:
        days_on_rent = abs(todays_date - start_date)
    except:
        days_on_rent = 1

    mileage_difference = current_mileage - start_mileage
    #daily_mileage = mileage_difference/days_on_rent
    return days_on_rent


def mileage_difference(vehicle):
    start_date = vehicle['hire_start_date']
    start_mileage = vehicle['hire_start_mileage']
    todays_date = datetime.now()
    current_mileage = vehicle['mileage']
    original_hire_date = vehicle['original_hire_date']
    original_hire_mileage = vehicle['original_hire_mileage']

    if pd.notnull(original_hire_date):
        start_date = original_hire_date

    if pd.notnull(original_hire_mileage):
        start_mileage = original_hire_mileage

    if not pd.notnull(current_mileage):
        current_mileage = 1

    if not pd.notnull(start_mileage):
        start_mileage = 1

    days_on_rent = todays_date - start_date
    mileage_difference = current_mileage - start_mileage

    return mileage_difference


def daily_mileage(vehicle):
    return vehicle['mileage_difference'] / vehicle['Days_On_Rent']
