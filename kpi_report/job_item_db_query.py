import pandas as pd
from utils.database.connection import cnxn
from utils.database import databases as db
from datetime import datetime, timedelta

job_db = db.jobs
job_item_db = db.job_items
hire_db = db.hires


def get_spend_by_date(date, month_spend: bool = False):
    if month_spend:
        date_in_date_format = datetime.strptime(date, "%d-%m-%Y")
        start_of_month = date_in_date_format.replace(day=1).strftime("%d-%m-%Y")
        end_of_month = last_day_of_month(date_in_date_format).strftime("%d-%m-%Y")
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
    df['Spend'] = df.apply(calculate_spend_amount, axis=1)
    df['Revenue Stream'] = df.apply(calculate_revenue_stream, axis=1)
    df['Repair Category'] = df.apply(calculate_repair_category, axis=1)
    df.to_excel('test.xlsx', index=False)


def last_day_of_month(date):
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1, day=1) - timedelta(days=1)


def calculate_revenue_stream(vehicle):
    recharge_amount = vehicle['Recharge Amount']
    hire_type = vehicle['Hire Type Name']
    if recharge_amount > 0:
        return "Recharges"
    elif hire_type == "Spot Hire":
        return "Short Term"
    elif hire_type == "Admin":
        return "Fleet Management"
    elif hire_type == "Customer own Vehicle":
        return "Fleet Management"
    elif hire_type == "Contract Hire":
        return "Contract Hire"
    elif hire_type == "Fleet Management":
        return "Fleet Management"
    elif hire_type == "Captive Sub":
        return "Short Term"
    elif hire_type == "Replacement":
        return "Short Term"
    elif hire_type == "PAYG":
        return "Short Term"
    elif hire_type == "Contract":
        return "Contract Hire"
    elif hire_type == "Cross Hire":
        return "Short Term"
    else:
        return "Undefined"


def calculate_repair_category(vehicle):
    job_type = vehicle['Job Type']
    if job_type == "Estimate":
        return "Other"
    elif job_type == "Inspection":
        return "Routine"
    elif job_type == "Repair":
        return "Other"
    elif job_type == "Tyre":
        return "Tyres"
    elif job_type == "Defect/Repairs":
        return "Breakdowns"
    elif job_type == "Breakdown":
        return "Breakdowns"
    elif job_type == "Paintwork":
        return "Other"
    elif job_type == "Parts":
        return "Other"
    elif job_type == "Service":
        return "Routine"
    elif job_type == "Maintenance":
        return "Routine"
    elif job_type == "Tachograph":
        return "Routine"
    elif job_type == "MOT":
        return "MOT"
    elif job_type == "Fridge":
        return "Routine"
    elif job_type == "Administration":
        return "Other"
    elif job_type == "Tail Lift":
        return "Routine"
    elif job_type == "Recall":
        return "Other"
    elif job_type == "Vehicle Return Work":
        return "Other"
    elif job_type == "Fuel":
        return "Other"
    elif job_type == "Hire Desk":
        return "Other"
    elif job_type == "De Hire":
        return "Other"
    elif job_type == "R&M Collection And Delivery":
        return "Other"
    elif job_type == "Brake Test":
        return "Routine"
    elif job_type == "Recovery":
        return "Breakdowns"
    else:
        return "Undefined"


def calculate_spend_amount(vehicle):
    recharge_amount = vehicle['Recharge Amount']
    cost_amount = vehicle['Internal Cost']
    if recharge_amount > 0:
        return recharge_amount
    else:
        return cost_amount

get_spend_by_date('27-04-2022')