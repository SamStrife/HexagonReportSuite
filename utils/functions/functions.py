import pandas as pd
from utils.database import queries, column_selectors, databases
from utils.database.connection import cnxn


def get_vehicle_details(registration):
    data = pd.read_sql(
        f"Select {column_selectors.vehicle_details_for_hexreports}  "
        f"from { databases.vehicles} "
        f"where \"Vehicle Registration\" = '{registration}';", cnxn)
    return data


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


def determine_vehicle_power_type(vehicle):
    match vehicle['parent_type']:
        case "Tractorunit" \
             | "Tonne 2 6 0 0 0kgs" \
             | "Fridge" \
             | "Tonne 1 8 0 0 0kgs" \
             | "Van Or Minibus"\
             | "Tonne 7 5 0 0kgs"\
             | "Rigid"\
             | "Car"\
             | "Van Low Loader"\
             | "Tonne 3 5 0 0kgs"\
             | "Tonne 1 2 0 0 0kgs"\
             | "Tonne 7 2 0 0kgs":
            return "Power Fleet"
        case"Trailer" | "Triaxle Fridge Trailer":
            return "Trailer Fleet"
        case "Forklift":
            return "Ancillary Unit"
        case _:
            return "Undefined"

















