import xlwt,xlrd


book1_path = r'E:\新建文件夹\提取数据\云MAS投诉\201910\10月投诉短信对应发送记录.xlsx'
book2_path = r'E:\新建文件夹\提取数据\云MAS投诉\201910\201910V2.xls'

workbook1 = xlrd.open_workbook(book1_path)
workbook2 = xlrd.open_workbook(book2_path)
workbook3 = xlwt.Workbook()
sheet1 = workbook1.sheet_by_index(0)
sheet2 = workbook2.sheet_by_index(0)
sheet3 = workbook3.add_sheet("新增列")



row_num1 = sheet1.nrows
col_num1 = sheet1.ncols
row_num2 = sheet2.nrows
col_num2 = sheet2.ncols

target_dict = {}
for i in range(1,row_num1):
    if sheet1.cell_value(i,5) is not '':
        target_dict[sheet1.cell_value(i,0)] = sheet1.cell_value(i,5)

index = 0
for i in range(1,row_num2):
    complaint_id = sheet2.cell_value(i,0)

    for id in target_dict:
        if str(id) == str(complaint_id):
            for j in range(6):
                sheet3.write(i,j,sheet2.cell_value(i,j))
            sheet3.write(i,6,target_dict[id])

workbook3.save("新增一列.xls")
