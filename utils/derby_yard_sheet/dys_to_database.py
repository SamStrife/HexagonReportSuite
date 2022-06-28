from dotenv import load_dotenv
import os
import derby_yard_sheet as dys
from sqlalchemy import create_engine

load_dotenv()

data = dys.derby_yard_sheet()

database_username = os.getenv("MYSQLUSERNAME")
database_password = os.getenv("MYSQLPASSWORD")
database_ip = os.getenv("MYSQLIP")

database_connection = create_engine(
    f"mysql://{database_username}:{database_password}@{database_ip}/'derby_yard_sheets'")

data.to_sql('yard_sheets', con=database_connection, if_exists='append')
