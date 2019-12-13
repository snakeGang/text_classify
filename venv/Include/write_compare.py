import xlrd,xlwt


origin_file = r'E://新建文件夹/提取数据/云MAS投诉/19年云MAS投诉/云MAS各省10月百万投诉比.xlsx'
file_7 = r'E:\PycharmProjects\text_classify\venv\Include\7days.txt'
file_month = r'E:\PycharmProjects\text_classify\venv\Include\one_month.txt'
file_two_month = r'E:\PycharmProjects\text_classify\venv\Include\two_month.txt'

workbook = xlrd.open_workbook(origin_file)
sheet = workbook.sheet_by_name('10月云MAS全部投诉')
row_num = sheet.nrows
col_nul = sheet.ncols

complaint_list = []
for i in range(row_num):
    if i > 0:
        complaint_list.append(tuple((sheet.cell_value(i, 0),sheet.cell_value(i, 2),sheet.cell_value(i, 7),sheet.cell_value(i, 9))))

seven_day_dict = {}
with open(file_7,'r',encoding='utf-8') as f:
    while True:
        line = f.readline()
        line_arr = line.split(r"|")
        if line_arr.__len__() == 1 :
            break
        com_id = line_arr[0]
        content = line_arr[3]
        billtime = line_arr[5]
        score = line_arr[6]
        seven_day_dict[com_id] = tuple((content,billtime,score))


one_month_dict = {}
with open(file_month,'r',encoding='utf-8') as f:
    while True:
        line = f.readline()
        line_arr = line.split(r"|")
        if line_arr.__len__() == 1 :
            break
        com_id = line_arr[0]
        content = line_arr[3]
        billtime = line_arr[5]
        score = line_arr[6]
        one_month_dict[com_id] = tuple((content,billtime,score))

two_month_dict = {}
with open(file_two_month,'r',encoding='utf-8') as f:
    while True:
        line = f.readline()
        line_arr = line.split(r"|")
        if line_arr.__len__() == 1 :
            break
        com_id = line_arr[0]
        content = line_arr[3]
        billtime = line_arr[5]
        score = line_arr[6]
        two_month_dict[com_id] = tuple((content,billtime,score))

out_workbook = xlwt.Workbook()
out_sheet = out_workbook.add_sheet("result")
fields = ['投诉编号', 'EC名称', '手机号', '投诉内容', '7天匹配内容','7天匹配发送时间','7天匹配相似度',
          '30天匹配内容','30天匹配发送时间','30天匹配相似度', '60天匹配内容','60天匹配发送时间','60天匹配相似度']
for field in range(0, len(fields)):
    out_sheet.write(0, field, fields[field])
rowIndex = 1


result_list = []
for i in range(complaint_list.__len__()):
    complaint_id = complaint_list[i][0]
    out_sheet.write(rowIndex, 0, complaint_id)
    out_sheet.write(rowIndex, 1, complaint_list[i][1])
    out_sheet.write(rowIndex, 2, complaint_list[i][2])
    out_sheet.write(rowIndex, 3, complaint_list[i][3])
    result = str(complaint_id)+"|"
    if seven_day_dict.get(complaint_id) is not None:
        hit = seven_day_dict.get(complaint_id)
        result = result + "seven_days|" + str(hit[0]) + "|" + str(hit[1]) + "|" + str(hit[2]) + "|"
        out_sheet.write(rowIndex, 4, hit[0])
        out_sheet.write(rowIndex, 5, hit[1])
        out_sheet.write(rowIndex, 6, hit[2])
    if one_month_dict.get(complaint_id) is not None:
        hit = one_month_dict.get(complaint_id)
        result = result+"one_month|"+str(hit[0])+"|"+str(hit[1])+"|"+str(hit[2])+"|"
        out_sheet.write(rowIndex, 7, hit[0])
        out_sheet.write(rowIndex, 8, hit[1])
        out_sheet.write(rowIndex, 9, hit[2])
    if two_month_dict.get(complaint_id) is not None:
        print(complaint_id)
        hit = two_month_dict.get(complaint_id)
        result = result+"two_month|"+str(hit[0])+"|"+str(hit[1])+"|"+str(hit[2])+"|"
        out_sheet.write(rowIndex, 10, hit[0])
        out_sheet.write(rowIndex, 11, hit[1])
        out_sheet.write(rowIndex, 12, hit[2])
        print(hit[0])
    result_list.append(result)
    rowIndex += 1
out_workbook.save('对比结果.xls')


