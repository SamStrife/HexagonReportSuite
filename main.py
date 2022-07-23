from utils.asset_file.asset_file import merged_query as mq

dataframe = mq()
dataframe.to_excel('output.xlsx', index=False)
