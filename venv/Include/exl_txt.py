import xlrd


orig_path = r"E:\PycharmProjects\text_classify\venv\Include\two_month.xlsx"
workbook = xlrd.open_workbook(orig_path)
sheet = workbook.sheet_by_index(0)
row_num = sheet.nrows
col_num = sheet.ncols

for i in range(1, row_num):
    print(int(sheet.cell_value(i,5)))

# with open('excel_txt_with_template.txt','w') as f:
#     for i in range(1, row_num):
#         if sheet.cell_value(i, 5) is not '':
#             f.write(sheet.cell_value(i, 0))
#             f.write('|')
#             f.write(sheet.cell_value(i, 1))
#             f.write('|')
#             f.write(sheet.cell_value(i, 3))
#             f.write('|')
#             f.write(sheet.cell_value(i, 4))
#             f.write('|')
#             f.write(str(sheet.cell_value(i, 5)))
#             f.write('|')
#             f.write('\n')
#     f.flush()
#     f.close()
