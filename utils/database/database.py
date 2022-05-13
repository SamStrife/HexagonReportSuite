import pyodbc
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

connection = {
    "server": os.getenv("SERVER"),
    "database": os.getenv("DATABASE"),
    "username": os.getenv("USER"),
    "password": os.getenv("PASSWORD")
}

database = {
    "postalAddresses": "soAddresses_PostalAddress_Report",
    "authorisation": "soAuthorisation_Authorisation_Report",
    "notes": "soNote_Note_Report",
    "notesCustom": "soNote_NoteCustom_Report",
    "purchaseOrders": "soPurchaseOrder_PurchaseOrder_Report",
    "purchaseOrderItems": "soPurchaseOrder_PurchaseOrderItem_Report",
    "customers": "soRelationshipManagement_Customer_Report",
    "suppliers": "soRelationshipManagement_Supplier_Report",
    "hires": "soVehicle_Hire_Report",
    "rfl": "soVehicle_RoadFundLicence_Report",
    "vehicles": "soVehicle_Vehicle_Report",
    "jobs": "soWorkshop_Job_Report"
}

query = {
    "vehicle_query": f"Select * from {database['vehicles']};",
    "purchase_order_query": f"Select * from {database['purchaseOrders']};",
    "job_query": f"Select * from {database['jobs']};",
    "hire_query": f"Select * from {database['hires']};"
}

wanted_columns = "\"Manufacturer Name\" as manufacturer,\
                    \"Model Name\"  as model,\
                    \"Vehicle Type Name\" as vehicleType,\
                    \"Vehicle Status Name\" as status,\
                    \"Vehicle Sub Status Name\" as subStatus,\
                    \"Customer Name\" as customer,\
                    \"Current Mileage\" as mileage,\
                    \"Next Inspection Date\" as inspectionDue,\
                    \"Next MOT Date\" as motDue,\
                    \"Next Tacho Calibration Date\" as tachoDue,\
                    \"Location\" as location"


def get_vehicle_details(registration):
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + connection['server'] + ';DATABASE=' + connection['database'] + ';UID=' + connection['username'] + ';PWD=' + connection['password'])
    data = pd.read_sql(
        f"Select {wanted_columns}  from {database['vehicles']} where \"Vehicle Registration\" = '{registration}';",
        cnxn)
    return data
