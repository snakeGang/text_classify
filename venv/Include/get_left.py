import xlrd,xlwt


book1_path = r'E:\PycharmProjects\text_classify\venv\Include\two_month.xlsx'
book2_path = r'E:\新建文件夹\提取数据\云MAS投诉\201910\10月投诉短信对应发送记录.xlsx'

workbook1 = xlrd.open_workbook(book1_path)
workbook2 = xlrd.open_workbook(book2_path)

sheet1 = workbook1.sheet_by_index(0)
sheet2 = workbook2.sheet_by_index(0)

row_num1 = sheet1.nrows
col_num1 = sheet1.ncols
row_num2 = sheet2.nrows
col_num2 = sheet2.ncols

index = 0
with open('left_id','w') as f:
    for i in range(row_num1):
        for j in range(1, row_num2):
            if sheet1.cell_value(i, 0) == sheet2.cell_value(j, 0):
                if sheet1.cell_value(i, 3) != sheet2.cell_value(j, 5):
                    f.write(sheet1.cell_value(i,0))
                    f.write('|')
                    f.write(sheet1.cell_value(i,1))
                    f.write('|')
                    f.write(sheet2.cell_value(j,5))
                    f.write('|')
                    f.write(sheet1.cell_value(i,4))
                    f.write('|')
                    f.write(sheet2.cell_value(j,6))
                    f.write('|')
                    f.write('\n')
    f.flush()
    f.close()


