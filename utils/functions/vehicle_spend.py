import pandas as pd
from utils.database import queries
from utils.database.connection import cnxn
from datetime import date

single_vehicle_query = str(queries.vehicle_spend_query(vehicle=1406, from_date="01/01/2022", to_date="01/02/2022"))
vehicle_spend = pd.read_sql(single_vehicle_query, cnxn)


def all_fleet_split():
    all_fleet_split = str(queries.all_spend_split())
    all_spend = pd.read_sql(all_fleet_split, cnxn)
    all_spend['Months Between'] = all_spend.apply(calculate_months, axis=1)

    spend_split = calculate_all_spend(all_spend)

    all_spend['3'] = all_spend.apply(calculate_three_month_spend, args=(spend_split,), axis=1)
    return all_spend


def calculate_months(vehicle):
    job_date = vehicle['job_date']
    today = date.today()
    months_between = (today.year - job_date.year) * 12 + today.month - job_date.month
    return months_between


def calculate_all_spend(table):
    _vehicle_spend = {}
    for row in table.iterrows():
        vehicle_id = row[1][0]
        job_cost = row[1][2]
        months = row[1][3]
        if vehicle_id in _vehicle_spend.keys():
            _vehicle_spend[vehicle_id]['spend'] += job_cost
        else:
            _vehicle_spend[vehicle_id] = {}
            _vehicle_spend[vehicle_id]['spend'] = job_cost
    return _vehicle_spend


def calculate_three_month_spend(vehicle, lookup_table):
    vehicle_id = vehicle['vehicle_id']
    try:
        return lookup_table[vehicle_id]['spend']
    except:
        return None
