import calendar
import json
import os
from datetime import *

import xlsxwriter

"""generate_annual_income_worksheet.py: Automates my personal Income Statement Excel workbook"""

__author__ = "Prajesh Ananthan 2016"


def create_excel_sheet(year):
    workbook = None
    table_position = 'B3:D13'
    merge_range = 'B2:D2'
    column_header_title = 'MONTHLY CASHFLOW'
    output_path = 'output/{}'
    filename = getfilename()
    success = False

    [header_title, item_list] = get_data()
    options = {'data': item_list, 'columns': header_title}

    try:
        workbook = xlsxwriter.Workbook(output_path.format(filename))
        merge_format = workbook.add_format({
            'bold': 2,
            'border': 2,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'yellow'})

        monthlist = getListofMonths(year)

        for month in monthlist:
            worksheet = workbook.add_worksheet(name=month)
            worksheet.set_column(1, 3, 20)
            worksheet.merge_range(merge_range, column_header_title, merge_format)
            worksheet.add_table(table_position, options)
        success = True
        print("INFO: {} created!".format(workbook.filename))

    except Exception as e:
        print(e, "ERROR: Unable to write onto {}!".format(filename))
    finally:
        workbook.close()

    return [success, workbook.filename]


def launchFileInWindows(unixpath):
    win32path = os.path.normcase(unixpath)
    try:
        if os.path.exists(win32path):
            print("INFO: Launching {}...".format(win32path))
            os.system(win32path)
    except Exception as e:
        print(e)


def getListofMonths(year):
    date1 = datetime.strptime("{}-01-01".format(year), "%Y-%m-%d")
    date2 = datetime.strptime("{}-01-12".format(year + 1), "%Y-%m-%d")
    months_str = calendar.month_name
    months = []
    while date1 < date2:
        month = date1.month
        year = date1.year
        month_str = months_str[month][0:3]
        months.append("{0}-{1}".format(month_str, str(year)[-2:]))
        next_month = month + 1 if month != 12 else 1
        next_year = year + 1 if next_month == 1 else year
        date1 = date1.replace(month=next_month, year=next_year)

    return months


def getfilename():
    prefix = "ANNUAL_CASHFLOW"
    year = "2017"
    extension = ".xlsx"

    return "{}--{}{}".format(prefix, year, extension)


def load_json():
    path = 'resources/data.json'
    content = json.load(open(path))
    return content


def get_data():
    title_list = [
        {'header': 'ITEM'},
        {'header': 'COST'},
        {'header': 'STATUS'}
    ]

    content = load_json()

    item_list = []
    for data_type in content:
        for item_name in content[data_type]:
            cost = content[data_type][item_name]
            current_item_list = [item_name, cost]
            item_list.append(current_item_list)

    return [title_list, item_list]


def main():
    year = 2017
    [success, filename] = create_excel_sheet(year)
    if success == True:
        launchFileInWindows(filename)


if __name__ == '__main__':
    main()
