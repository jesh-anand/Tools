import calendar
import os
from datetime import *

import xlsxwriter

"""test_replicate_worksheet.py: IT on Income Statement Excel workbook"""

__author__ = "Prajesh Ananthan"


def test_create_XLSheet():
    workbook = None
    tablerange = 'B3:D7'
    filename = getfilename()
    success = False
    data = get_mock_columns_with_data()
    options = {'data': data,
               'columns':
                   [
                       {'header': 'ITEM'},
                       {'header': 'COST'},
                       {'header': 'STATUS'}
                   ]
               }

    try:
        workbook = xlsxwriter.Workbook('output/{}'.format(filename))
        monthlist = test_get_list_months()

        for month in monthlist:
            worksheet = workbook.add_worksheet(name=month)
            worksheet.set_column(1, 3, 15)
            worksheet.add_table(tablerange, options)
        success = True
        print("INFO: {} created!".format(workbook.filename))

    except Exception as e:
        print(e, "Unable to write onto {}!".format(filename))
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


def test_get_list_months():
    date1 = datetime.strptime("2017-01-01", "%Y-%m-%d")
    date2 = datetime.strptime("2018-01-12", "%Y-%m-%d")
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


def get_mock_columns_with_data():
    data = [
        ['PTPTN', 10000],
        ['Rent', 2000],
        ['Car Loan', 6000],
        ['Unifi', 500]
    ]
    return data


def run_test_cases():
    [success, filename] = test_create_XLSheet()
    if success == True:
        launchFileInWindows(filename)


if __name__ == '__main__':
    run_test_cases()
