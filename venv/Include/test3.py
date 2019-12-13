# -!- coding: utf-8 -!
import xlrd,xlwt


path1 = r'E:\PycharmProjects\text_classify\venv\Include\two_month.xlsx'
path2 = r'E:\新建文件夹\提取数据\云MAS投诉\201910\201910V2_1.xlsx'

workbook1 = xlrd.open_workbook(path1)
workbook2 = xlrd.open_workbook(path2)
sheet1 = workbook1.sheet_by_index(0)
sheet2 = workbook2.sheet_by_index(0)

row_num1 = sheet1.nrows
row_num2 = sheet2.nrows

item_dict = {}
for i in range(0,row_num1):
    item_dict[sheet1.cell_value(i,0)] = i

newbook = xlwt.Workbook()
sheet3 = newbook.add_sheet("aa")

cm_list = []
for i in range(1,row_num2):
    complaint_id = sheet2.cell_value(i,0)
    ecid = item_dict[complaint_id]
    sheet3.write(i,0,sheet2.cell_value(i,0))
    sheet3.write(i, 1, sheet1.cell_value(item_dict[complaint_id],1))
    sheet3.write(i, 2, sheet2.cell_value(i, 2))
    sheet3.write(i, 3, sheet2.cell_value(i, 3))
    sheet3.write(i, 4, sheet2.cell_value(i, 4))
    sheet3.write(i, 5, sheet2.cell_value(i, 5))

newbook.save("测试xls.xls")