from utils.asset_file.asset_file import asset_file_generation as afg
import pandas as pd
from utils.asset_file.excel_cell_formats import cell_format


def export_af_to_excel():
    # Create the dataframe by running the asset file query (uses tidynames to format the cell headers in advance)
    dataframe = afg(tidy_names=True)

    # Get the shape of the dataframe
    (max_row, max_col) = dataframe.shape

    # Sets up the writer and destination
    writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

    # Convert the dataframe to Excel Format
    dataframe.to_excel(writer, header=False, index=False)

    # Sets up the workbook
    workbook = writer.book

    # Creates the worksheet
    worksheet = writer.sheets['Sheet1']

    # Formats the sheet
    for col_num, header_value in enumerate(dataframe.columns.values):
        header_format = workbook.add_format({
            'bold': True,
            'text_wrap': False,
            'valign': 'top',
            'fg_color': determine_format(header_value)['header_cell_colour'],
            'color': determine_format(header_value)['header_text_colour'],
            'border': 1})
        data_format = workbook.add_format({
            'text_wrap': False,
            'border': 1})
        worksheet.write(0, col_num, header_value, header_format)

    # Add the filter to the sheet
    worksheet.autofilter(0, 0, max_row - 1, max_col - 1)

    # Save and close the document
    writer.save()


def determine_format(header_name) -> {}:
    """
    Looks up the column name in cell format and returns the formatting details to be passed to XLSX Writer
    :param header_name: The column name.
    :return: {header_cell_colour: The cell colour for the column header, header_text_colour: The text colour for the
    column header}
    """
    if header_name in cell_format.keys():
        return {
            'header_cell_colour': cell_format[header_name].get('header_colour', None),
            'header_text_colour': cell_format[header_name].get('header_text_colour', None),
            'data_text_colour':   cell_format[header_name].get('data_text_colour', None)
        }
    else:
        return {
            'header_cell_colour': '#000000',
            'header_text_colour': '#000000'
        }