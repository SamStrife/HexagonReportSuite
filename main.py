from utils.asset_file.asset_file import merged_query as mq
import pandas as pd

dataframe = mq()
dataframe.to_excel('output.xlsx')
