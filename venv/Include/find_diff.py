import xlrd


path1 = r'E:\新建文件夹\提取数据\云MAS投诉\201910\201910V2_1.xlsx'
path2 = r'E:\新建文件夹\提取数据\云MAS投诉\201910\10月投诉短信对应发送记录.xlsx'

workbook1 = xlrd.open_workbook(path1)
workbook2 = xlrd.open_workbook(path2)
sheet1 = workbook1.sheet_by_index(0)
sheet2 = workbook2.sheet_by_index(0)
row_num1 = sheet1.nrows
col_num1 = sheet1.ncols
row_num2 = sheet2.nrows
col_num2 = sheet2.ncols

index = 0
complaint_list = []
for i in range(1,row_num2):
    if sheet2.cell_value(i,5) != '':
        complaint_list.append(sheet2.cell_value(i,0))

large_list = []
for i in range(1,row_num1):
    large_list.append(sheet1.cell_value(i,0))

real_list = list(set(large_list))

list1_have = [x for x in real_list if x not in complaint_list]
list2_have = [x for x in complaint_list if x not in real_list]
print(list1_have)
print(list2_have)





