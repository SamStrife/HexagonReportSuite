import pandas as pd
from utils.database.connection import cnxn
from utils.database import databases as db
from datetime import datetime, timedelta

auth_db = db.authorisation
job_db = db.jobs


def get_spend_by_date(date):
    auth_query = f"SELECT * FROM {auth_db} where\"Authorisation Date\" between '{date}' and '{date} 23:59:59'"
    jobs_query = f"SELECT * FROM {job_db}"
    auth_df = pd.read_sql(auth_query, cnxn)
    job_df = pd.read_sql(jobs_query, cnxn)
    df = auth_df.merge(job_df[['Unique ID', 'Hire Unique ID', 'Job Type']], left_on='Job Number', right_on='Unique ID')
    df.to_excel('test.xlsx')


def get_month_spend_by_date(date):
    date_in_date_format = datetime.strptime(date, "%d-%m-%Y")
    start_of_month = date_in_date_format.replace(day=1).strftime("%d-%m-%Y")
    end_of_month = last_day_of_month(date_in_date_format).strftime("%d-%m-%Y")
    auth_query = f"SELECT * FROM {auth_db} where\"Authorisation Date\" between '{start_of_month}' and '{end_of_month} 23:59:59'"
    jobs_query = f"SELECT * FROM {job_db}"
    auth_df = pd.read_sql(auth_query, cnxn)
    job_df = pd.read_sql(jobs_query, cnxn)
    df = auth_df.merge(job_df[['Unique ID', 'Hire Unique ID', 'Job Type']], left_on='Job Number', right_on='Unique ID')
    df.to_excel('test.xlsx')


def last_day_of_month(date):
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1, day=1) - timedelta(days=1)


get_month_spend_by_date('27-04-2022')
