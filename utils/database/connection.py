from dotenv import load_dotenv
import pyodbc
import os

load_dotenv()

driver = "ODBC Driver 17 for SQL Server"
server = os.getenv("SERVER")
database = os.getenv("DATABASE")
username = os.getenv("MSSQLUSER")
password = os.getenv("MSSQLPASSWORD")

cnxn = pyodbc.connect(
    f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}")
