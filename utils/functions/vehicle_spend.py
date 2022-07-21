import pandas as pd
from utils.database import queries
from utils.database.connection import cnxn
from datetime import date

single_vehicle_query = str(queries.vehicle_spend_query(vehicle=1406, from_date="01/01/2022", to_date="01/02/2022"))
vehicle_spend = pd.read_sql(single_vehicle_query, cnxn)


def spend_splitter(vehicle, table):
    job_date = vehicle['job_date']
    today = date.today()
    months_between = (today.year - job_date.year) * 12 + today.month - job_date.month
    return months_between


all_fleet_split = str(queries.all_spend_split())
all_spend = pd.read_sql(all_fleet_split, cnxn)
all_spend['Months Between'] = all_spend.apply(spend_splitter, args=(all_spend,), axis=1)
all_spend['3'] = None
all_spend['12'] = None
all_spend['Lifetime'] = None
