import calendar
import os
from datetime import *

import xlsxwriter

"""generate_annual_income_worksheet.py: Automates my personal Income Statement Excel workbook"""

__author__ = "Prajesh Ananthan 2016"


def create_excel_sheet(year):
    workbook = None
    table_position = 'B3:D7'
    filename = getfilename()
    success = False
    [header_title, item_list] = get_data()
    options = {'data': item_list, 'columns': header_title}

    try:
        workbook = xlsxwriter.Workbook('output/{}'.format(filename))
        monthlist = getListofMonths(year)

        for month in monthlist:
            worksheet = workbook.add_worksheet(name=month)
            worksheet.set_column(1, 3, 15)
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


# TODO: Insert more items
# TODO: Parse content into json file
def get_data():
    title_list = [
        {'header': 'ITEM'},
        {'header': 'COST'},
        {'header': 'STATUS'}
    ]

    item_list = [
        ['Car Monthly Installement', 481],
        ['House Rent', 450],
        ['PTPTN', 105.42],
        ['Rapid KL', 500],
        ['Touch \'N Go', 64],
        ['Unifi', 200]
    ]
    return [title_list, item_list]


def main():
    year = 2017
    [success, filename] = create_excel_sheet(year)
    if success == True:
        launchFileInWindows(filename)


if __name__ == '__main__':
    main()
