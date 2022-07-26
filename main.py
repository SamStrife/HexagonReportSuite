from utils.asset_file.asset_file import asset_file_generation as afg

dataframe = afg(tidy_names=True)
dataframe.to_excel('output.xlsx', index=False)
