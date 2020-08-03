# 获取excel中各个常量（行号，project_name,industry_category,Networking_Solution）的值


from utils.opera_excel import OperationExcel

class GetData:
    def __init__(self,sheet_num):
        self.opera_excel = OperationExcel(sheet_num)

    # 获取所有数据
    def data(self):
        arr_data1 = []
        rows_count = self.opera_excel.get_lines()
        #行数循环
        for i in range(1,rows_count):
            #列数循环
            arr_data0 = []
            for j in range(0,self.opera_excel.cols_count()):
                row_col_data = self.opera_excel.get_cell_value(i,j)
                arr_data0.append(row_col_data)
            arr_data1.append(arr_data0)
        return arr_data1

"""
if __name__ == '__main__':
    s = GetData(0)
    s.data()
"""

