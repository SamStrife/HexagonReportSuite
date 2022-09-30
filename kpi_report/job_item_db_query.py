import pandas as pd
import helper_functions as hf
from utils.database.connection import cnxn
from utils.database import databases as db
from datetime import datetime

job_db = db.jobs
job_item_db = db.job_items
hire_db = db.hires


def get_spend_by_date(date, month_spend: bool = False):
    if month_spend:
        date_in_date_format = datetime.strptime(date, "%d-%m-%Y")
        start_of_month = date_in_date_format.replace(day=1).strftime("%d-%m-%Y")
        end_of_month = hf.last_day_of_month(date_in_date_format).strftime("%d-%m-%Y")
        job_item_query = f"SELECT * FROM {job_item_db} where\"Required Date\" between '{start_of_month}' and '{end_of_month} 23:59:59'"
    else:
        job_item_query = f"SELECT * FROM {job_item_db} where\"Required Date\" between '{date}' and '{date} 23:59:59'"
    hire_query = f"SELECT * FROM {hire_db}"
    job_query = f"SELECT * FROM {job_db}"
    job_item_df = pd.read_sql(job_item_query, cnxn)
    hire_df = pd.read_sql(hire_query, cnxn)
    job_df = pd.read_sql(job_query, cnxn)
    df = job_item_df.merge(job_df[["Unique ID", "Hire Unique ID"]], how="left", left_on="Job Unique ID", right_on="Unique ID")
    df = df.merge(hire_df[["Unique ID", "Hire Type Name"]], how="left", left_on="Hire Unique ID", right_on="Unique ID")
    df['Spend'] = df.apply(hf.calculate_spend_amount, axis=1)
    df['Revenue Stream'] = df.apply(hf.calculate_revenue_stream, axis=1)
    df['Repair Category'] = df.apply(hf.calculate_repair_category, axis=1)
    df.to_excel('test.xlsx', index=False)


get_spend_by_date('27-04-2022', True)
