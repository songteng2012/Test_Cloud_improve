import xlrd
from utils.path_config import FILE_PATH


class OperationExcel:

    def __init__(self,sheet_num):
        self.sheet_num = sheet_num

    # 获取table数据
    def get_data(self):
        data = xlrd.open_workbook(FILE_PATH)
        tables = data.sheets()[self.sheet_num]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.get_data()
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self,row,col):
        return self.get_data().cell_value(row,col)

    #获取第一行的列数
    def cols_count(self):
        title = self.get_data().row_values(0)
        return len(title)

"""
if __name__ == '__main__':
    s = OperationExcel(0)
    s.cols_count()
"""

