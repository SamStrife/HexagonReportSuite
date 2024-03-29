import pandas as pd
from utils.database import queries
from utils.database.connection import cnxn
from datetime import date

single_vehicle_query = str(queries.vehicle_spend_query(vehicle=1406, from_date="01/01/2022", to_date="01/02/2022"))


def vehicle_spend():
    pd.read_sql(single_vehicle_query, cnxn)


def all_fleet_split(dataframe):
    all_fleet_split = str(queries.all_spend_split())
    all_spend = pd.read_sql(all_fleet_split, cnxn)
    all_spend['Months Between'] = all_spend.apply(calculate_months_between_today_and_job_date, axis=1)
    spend_split = calculate_all_spend(dataframe, all_spend)
    return spend_split


def calculate_months_between_today_and_job_date(vehicle):
    job_date = vehicle['job_date']
    today = date.today()
    months_between = (today.year - job_date.year) * 12 + today.month - job_date.month
    return months_between


def calculate_all_spend(dataframe, table):
    _vehicle_spend = {}
    for vehicle in dataframe.iterrows():
        vehicle_id = vehicle[1].loc['vehicle_id']
        _vehicle_spend[vehicle_id] = {'3': 0, '12': 0, 'Life': 0}
    for row in table.iterrows():
        vehicle_id = row[1][0]
        job_cost = row[1][2]
        months = row[1][3]
        if vehicle_id not in _vehicle_spend.keys():
            _vehicle_spend[vehicle_id] = {'3': 0, '12': 0, 'Life': 0}
        if 0 <= months < 3:
            _vehicle_spend[vehicle_id]['3'] += job_cost
            _vehicle_spend[vehicle_id]['12'] += job_cost
            _vehicle_spend[vehicle_id]['Life'] += job_cost
        elif 3 <= months < 12:
            _vehicle_spend[vehicle_id]['12'] += job_cost
            _vehicle_spend[vehicle_id]['Life'] += job_cost
        else:
            _vehicle_spend[vehicle_id]['Life'] += job_cost
    return _vehicle_spend
