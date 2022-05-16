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
    data.rename(columns={
                 "job_date": "Job Date",
                 "registration": "Registration",
                 "vehicle_type": "Vehicle Type",
                 "job_type": "Job Type",
                 "vehicle_mileage": "Vehicle Mileage",
                 "job_status": "Job Status",
                 "supplier": "Supplier",
                 "customer": "Customer",
                 "job_description": "Job Description",
                 "recharge": "Recharge",
                 "labour_cost": "Labour Cost",
                 "parts_cost": "Parts Cost",
                 "total_cost": "Total Cost"}, inplace=True)
    return data


def derby_yard_sheet():
    data = pd.read_sql(queries.vehicle_query, cnxn)
    vehicles_marked_at_derby = data[data["Location"].str.contains("Derby", na=False)]
    vehicles_outside_of_derby = not data[data["Location"].str.contains("Derby", na=False)] and \
                                data[data["Customer"] == "Not On Hire"]
    return {vehicles_marked_at_derby, vehicles_outside_of_derby}
