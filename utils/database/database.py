import pyodbc
import pandas as pd
from dotenv import load_dotenv
import os
import utils.database.column_selectors as cols
import utils.database.queries as query

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


def get_vehicle_details(registration):
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + connection['server'] + ';DATABASE=' + connection['database'] + ';UID=' + connection['username'] + ';PWD=' + connection['password'])
    data = pd.read_sql(
        f"Select {cols.vehicle_details}  from {database['vehicles']} where \"Vehicle Registration\" = '{registration}';",
        cnxn)
    return data


def test():
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + connection['server'] + ';DATABASE=' + connection['database'] + ';UID=' + connection['username'] + ';PWD=' + connection['password'])
    data = pd.read_sql(
        f"Select {cols.supplier_spend_columns} from {database['jobs']};",
        cnxn)
    return data
