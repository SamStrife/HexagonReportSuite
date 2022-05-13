import pandas as pd
from utils.database import queries
from utils.database.connection import cnxn


def supplier_spend(supplier=None, final_costs=False, styling=None):
    data = pd.read_sql(queries.supplier_spend, cnxn, index_col="job_number")
    supplier_group_query = pd.read_sql(queries.supplier_query, cnxn)
    data = data.merge(supplier_group_query[['Trading Name', 'Organisation Group Name']],
                      left_on="supplier",
                      right_on="Trading Name",
                      how='left')
    data.drop("Trading Name", axis=1, inplace=True)
    data = data[["job_date",
                 "registration",
                 "vehicle_type",
                 "job_type",
                 "vehicle_mileage",
                 "job_status",
                 "supplier",
                 "Organisation Group Name",
                 "customer",
                 "job_description",
                 "recharge",
                 "labour_cost",
                 "parts_cost",
                 "total_cost"]]
    if supplier:
        data = data[data['supplier'].str.contains(supplier, na=False)]
    if final_costs:
        data = data[data['job_status'] == 'Complete']
    if styling:
        pass
    return data
