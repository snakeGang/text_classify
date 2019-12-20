# -!- coding: utf-8 -!
import xlrd,xlwt
import collections

# path1 = r'E:\PycharmProjects\text_classify\venv\Include\two_month.xlsx'
path2 = r'E:\新建文件夹\提取数据\云MAS投诉\find_real_send.xlsx'

workbook2 = xlrd.open_workbook(path2)
sheet2 = workbook2.sheet_by_index(0)
row_num = sheet2.nrows

print("开始读取")
print(row_num)
ec_name_list = []


# with open('find_real_send.txt','w') as f:
#     for i in range(1, row_num):
#         complaint_id = sheet2.cell_value(i, 0)
#         ecid = sheet2.cell_value(i, 1)
#         ec_name = sheet2.cell_value(i, 2)
#         mobile = sheet2.cell_value(i, 3)
#         content = sheet2.cell_value(i, 4)
#         templateid = sheet2.cell_value(i, 5)
#         if templateid == '':
#             templateid = '普通短信'
#         score = sheet2.cell_value(i, 6)
#         complaint_content = sheet2.cell_value(i, 7)
#         target_list = []
#         target_list.append(complaint_id)
#         target_list.append(ecid)
#         target_list.append(ec_name)
#         target_list.append(content)
#         target_list.append(templateid)
#         for j in target_list:
#             f.write(j)
#             f.write('|')
#         f.write('\n')
#     f.flush()


for i in range(1,row_num):
    ec_name = sheet2.cell_value(i,2)
    ec_name_list.append(ec_name)

c = collections.Counter(ec_name_list)

with open('count.txt','w') as f:
    for i in sorted(c,key=c.__getitem__,reverse=True):
        f.write(i)
        f.write('\t')
        f.write(str(c[i]))
        f.write('\n')

    f.flush()
