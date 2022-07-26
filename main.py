from utils.asset_file.asset_file import asset_file_generation as afg
import pandas as pd

dataframe = afg(tidy_names=True)
(max_row, max_col) = dataframe.shape
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
dataframe.to_excel(writer, header=False, index=False)
workbook = writer.book
worksheet = writer.sheets['Sheet1']


cell_format = \
    {
        'Customer Group': {'header_colour': '#383837', 'header_text_colour': '#ffffff'},
        'Account Manager': {'header_colour': '#383837', 'header_text_colour': '#ffffff'},
        # 'Vehicle Type': '',
        # 'Registration': '',
        # 'Hire End Date': '',
        # 'Customer Status': '',
        # 'In Scope?': '',
        # 'Engagement Level': '',
        # 'Current View': '',
        # 'Expected Return Date': '',
        # '2nd Decision': '',
        # 'Plan View': '',
        # 'Product manager View': '',
        # 'Product Manager Return Date': '',
        # 'Mileage banding': '',
        # 'Up Priced': '',
        # 'Latest Increase': '',
        # 'Effective Date': '',
        # 'Customer Account Number': '',
        # 'Customer Name': '',
        # 'Segment': '',
        # 'Customer Powered Fleet': '',
        # 'Customer Trailer Fleet': '',
        # 'Customer Ancillary Fleet': '',
        # 'Customer Undefined Fleet': '',
        # 'Total Hexagon Fleet': '',
        # 'Power Type': '',
        # 'Vehicle On Fleet Date': '',
        # 'Years In Service': '',
        # 'Manufacturer': '',
        # 'Model': '',
        # 'Parent vehicle Type': '',
        # 'Fridge?': '',
        # 'Supplier name': '',
        # 'Supplier Post Code': '',
        # 'Current Mileage': '',
        # 'Mileage Reading Date': '',
        # 'Daily Mileage': '',
        # 'Project Mileage At Contract End': '',
        # 'Contract Annual Mileage Allowance': '',
        # 'Rated Mileage @ Reading Date': '',
        # 'Over/Under Rated Mileage @ Reading Date': '',
        # 'Over/Under Rated Mileage % @ Reading Date': '',
        # 'Financer': '',
        # 'Capital': '',
        # 'NBV': '',
        # 'Residual': '',
        # 'Finance End Date': '',
        # 'Monthly Depreciation': '',
        # 'Hire Start Date': '',
        # 'Original Hire Start Date': '',
        # 'Contract Billing Amount(Monthly)': '',
        # 'Contract Billing Amount(Annually)': '',
        # 'Contract Billing Amount(Weekly)': '',
        # 'Billing Frequency': '',
        # 'Current Contract Expiry Month': '',
        # 'Current Contract Expiry Year': '',
        # 'Contract Status': '',
        # '3 Month Revenue': '',
        # '3 Month Expenditure': '',
        # '3 Month Margin': '',
        # '3 Month Margin %': '',
        # '12 Month Revenue': '',
        # '12 Month Expenditure': '',
        # '12 Month Margin': '',
        # '12 Month Margin %': '',
        # 'Life Revenue': '',
        # 'Life Expenditure': '',
        # 'Life Margin': '',
        # 'Life Margin %': '',
    }


def determine_header_color(cell_value):
    if cell_value in cell_format.keys():
        return {
            'cell': cell_format[cell_value]['header_colour'],
            'text': cell_format[cell_value]['header_text_colour']
        }
    else:
        return {
            'cell': '#000000',
            'text': '#000000'
        }


for col_num, value in enumerate(dataframe.columns.values):
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': determine_header_color(value)['cell'],
        'color': determine_header_color(value)['text'],
        'border': 1})
    worksheet.write(0, col_num, value, header_format)

writer.save()
