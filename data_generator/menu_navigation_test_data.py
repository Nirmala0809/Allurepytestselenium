import os
from utilities import XLUtil as Excel


def get_menuNavigation_testdata():
    workbook = os.path.join(os.path.dirname(__file__), '..', 'resources', 'TestData.XLSX')
    sheet = "Menu_Navigation_Data"
    Excel.open_wb(workbook, sheet)

    _data = []
    for row in range(2, Excel.get_max_rows() + 1):

        run = Excel.get_cell_data(row, 2)

        if run == "Y":
            navigation = Excel.get_cell_data(row, 3)
            expected_url = Excel.get_cell_data(row, 4)
            _data.append((navigation, expected_url))

    else:
        Excel.close_wb()

    data = {"menu_navigation_data": _data}
    return data
