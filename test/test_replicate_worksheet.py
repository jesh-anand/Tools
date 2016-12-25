import calendar
from datetime import *

import xlsxwriter


def test_create_XLSheet():
    print(getfilename())
    workbook = xlsxwriter.Workbook('resources/{}'.format(getfilename()))
    monthslist = test_get_list_months()
    for month in monthslist:
        worksheet = workbook.add_worksheet(name=month)
        data = get_mock_columns_with_data()
        worksheet.add_table('B3:F7', {'data': data})
        # worksheet1.write(month, "123")
    workbook.close()


def test_get_list_months():
    date1 = datetime.strptime("2016-01-01", "%Y-%m-%d")
    date2 = datetime.strptime("2017-01-12", "%Y-%m-%d")
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
    filename = "{}--{}{}".format(prefix, year, extension)

    return filename


def get_mock_columns_with_data():
    data = [
        ['Item', 'Cost'],
        ['Apples', 10000, 5000, 8000, 6000],
        ['Pears', 2000, 3000, 4000, 5000],
        ['Bananas', 6000, 6000, 6500, 6000],
        ['Oranges', 500, 300, 200, 700],

    ]
    return data


def run_test_cases():
    test_create_XLSheet()
    # test_get_list_months()


if __name__ == '__main__':
    run_test_cases()
