import os
from utilities import XLUtil as Excel


def get_login_testdata():
    workbook = os.path.join(os.path.dirname(__file__), '..', 'resources', 'TestData.XLSX')
    sheet = "Login_Data"
    Excel.open_wb(workbook, sheet)

    fail_data = []
    pass_data = []
    for row in range(2, Excel.get_max_rows() + 1):
        scenario = Excel.get_cell_data(row, 6)
        run = Excel.get_cell_data(row, 2)

        if run == "Y":
            username = Excel.get_cell_data(row, 3)
            password = Excel.get_cell_data(row, 4)
            expected_msg = Excel.get_cell_data(row, 5)

        if scenario == "Login_Fail":
            fail_data.append((username, password, expected_msg))
        elif scenario == "Login_Pass":
            pass_data.append((username, password, expected_msg))
    else:
        Excel.close_wb()

    data = {"login_pass_data": pass_data, "login_fail_data": fail_data}
    return data
