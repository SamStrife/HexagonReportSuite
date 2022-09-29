import pandas as pd
from utils.database.connection import cnxn
from utils.database import databases as db
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.today().date()
yesterday = today - relativedelta(days=1)
last_month = today - relativedelta(months=1)
yesterday_for_sql_query = yesterday.strftime("%d-%m-%Y")
last_month_for_sql_query = last_month.strftime("%d-%m-%Y")

auth_db = db.authorisation
job_db = db.jobs

auth_query = f"SELECT * FROM {auth_db} where\"Authorisation Date\" between '{yesterday_for_sql_query}' and '{yesterday_for_sql_query} 23:59:59'"
jobs_query  = f"SELECT * FROM {job_db}"

auth_df = pd.read_sql(auth_query, cnxn)
job_df = pd.read_sql(jobs_query, cnxn)
df = auth_df.merge(job_df, left_on='Job Number', right_on='Unique ID')

df.to_excel('test.xlsx')