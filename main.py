from utils.asset_file.asset_file import merged_query as mq
import pandas as pd
from utils.functions.vehicle_spend import all_spend

dataframe = all_spend
dataframe.to_excel('output.xlsx', index=False)


