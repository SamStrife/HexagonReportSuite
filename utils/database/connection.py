from dotenv import load_dotenv
import pyodbc
import os

load_dotenv()

driver = "ODBC Driver 17 for SQL Server"
server = os.getenv("SERVER")
database = os.getenv("DATABASE")
username = os.getenv("USER")
password = os.getenv("PASSWORD")

cnxn = pyodbc.connect(
    f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}")
