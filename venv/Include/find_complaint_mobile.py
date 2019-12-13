# -!- coding: utf-8 -!-
import xlwt
import xlrd


path1 = 'E://新建文件夹/提取数据/云MAS投诉/all_mobile.xlsx'
path2 = 'E://新建文件夹/提取数据/云MAS投诉/投诉汇总.xlsx'
workbook1 = xlrd.open_workbook(path1)
workbook2 = xlrd.open_workbook(path2)
sheet1 = workbook1.sheets()[0]
sheet2 = workbook2.sheets()[0]
col_num1 = sheet1.ncols
row_num1 = sheet1.nrows
col_num2 = sheet2.ncols
row_num2 = sheet2.nrows

target_list = []
for i in range(1,row_num2):
    target_list.append(sheet2.cell_value(i,3))

data_list = []
for i in range(row_num1):
    data_list.append(sheet1.cell_value(i,0))

b =0
with open('test2.txt','w') as f:
    for mobile in target_list:
        b += 1
        if b > 2000:
            break
        a = 0
        for data in data_list:
            if str(mobile)==str(int(data)):
                print(b)
                a += 1
                print(str(int(data)))
                print(mobile)
                print(data == mobile)
        if a > 0:
            f.write(mobile)
            f.write(',')
            f.write(str(a))
            f.write('\n')
            a = 0
    f.flush()
    f.close()




