import pandas as pd
from utils.database.connection import cnxn
import utils.database.databases as db

customer_df = pd.read_sql(f"SELECT * FROM {db.customers}", cnxn)
df = pd.read_excel('Sales by Customer YTD.xlsx', sheet_name="Sales - Fleet Management Tra...", header=4)
df = df.merge(customer_df[['Full Name', 'Organisation Group Name']], how="left", left_on="Contact", right_on="Full Name")
df.to_excel("test.xlsx", index=False)
