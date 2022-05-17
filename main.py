from utils.derby_yard_sheet import derby_yard_sheet as dys
from sqlalchemy import create_engine

test = dys.derby_yard_sheet()

database_username = 'sam'
database_password = 'garden79'
database_ip = '139.59.171.54'
database_name = 'derby_yard_sheets'
database_connection = create_engine(
    f"mysql://{database_username}:{database_password}@{database_ip}/{database_name}")

test.to_sql('yard_sheets', con=database_connection, if_exists='append')
