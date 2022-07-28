from utils.asset_file.asset_file import asset_file_generation as afg
import pandas as pd
from utils.asset_file.excel_cell_formats import cell_format


def export_af_to_excel():
    # Create the dataframe by running the asset file query (uses tidynames to format the cell headers in advance)
    dataframe = afg(tidy_names=True)

    # Get the shape of the dataframe
    (max_row, max_col) = dataframe.shape

    # Sets up the writer and destination
    writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter', datetime_format='dd/mm/yyyy')

    # Convert the dataframe to Excel Format
    dataframe.to_excel(writer, header=False, index=False)

    # Sets up the workbook
    workbook = writer.book

    # Creates the worksheet
    worksheet = writer.sheets['Sheet1']

    # Formats the sheet
    for col_num, header_value in enumerate(dataframe.columns.values):
        header_text = header_value
        if header_text[-1] == '2':
            header_text = header_text[:-2]
        header_format = workbook.add_format(get_header_format(header_value))
        data_format = workbook.add_format(get_data_format(header_value))
        worksheet.write(0, col_num, header_text, header_format)
        worksheet.set_column(col_num, col_num, 30, data_format)
        worksheet.data_validation(1, col_num, max_row - 1, col_num, get_data_validation(header_value))

    # Add the filter to the sheet
    worksheet.autofilter(0, 0, max_row - 1, max_col - 1)

    # Save and close the document
    writer.save()


def get_header_format(header):
    if header in cell_format.keys():
        return cell_format[header]['header_format']
    else:
        return None


def get_data_format(header):
    if header in cell_format.keys():
        return cell_format[header]['data_format']
    else:
        pass


def get_data_validation(header):
    if header in cell_format.keys():
        try:
            return cell_format[header]['data_validation']
        except:
            pass
    else:
        pass
