# -!- coding: utf-8 -!-
import xlrd
import jieba
import xlwt
from gensim import corpora,models,similarities


def sililar_fun(target_content,tmp_list):
    doc_test = target_content
    all_doc = []
    ex_line = tmp_list[0]
    ex_line = (ex_line[0],ex_line[1],ex_line[2],ex_line[3],"测试内容",ex_line[5])
    tmp_list.append(ex_line)
    for i in range(tmp_list.__len__()):
        all_doc.append(tmp_list[i][4])

    all_doc_list = []
    for doc in all_doc:
        doc_list = [word for word in jieba.cut(doc)]
        all_doc_list.append(doc_list)
    doc_test_list = [word for word in jieba.cut(doc_test)]

    dictionary = corpora.Dictionary(all_doc_list)

    corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]

    doc_test_vec = dictionary.doc2bow(doc_test_list)

    tfidf = models.TfidfModel(corpus)
    tfidf[doc_test_vec]

    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
    sim = index[tfidf[doc_test_vec]]
    hits = sorted(enumerate(sim), key=lambda item: -item[1])
    date_list = []
    if hits.__len__()>1:
        if (hits[0][1]>0 and hits[0][1] == hits[1][1]):
            for hit in hits:
                date_list.append(tmp_list[hit[0]][5])
            #print(tmp_list[hits[0][0]])
            #print(tmp_list[hits[1][0]])
            #print(target_content)
            #print(hits[0][1])
            #print(hits[1][1])
            #print(list(set(date_list)))
    most_hit = hits[0][0]
    most_score = hits[0][1]
    if most_score==0:
        return None
    #print(most_score)
    return tuple((tmp_list[most_hit][0],tmp_list[most_hit][1],tmp_list[most_hit][2],tmp_list[most_hit][3],tmp_list[most_hit][4],tmp_list[most_hit][5],str(most_score),target_content))


path = r'E:\新建文件夹\提取数据\云MAS投诉\201901\201901.xls'
target_path = 'E://新建文件夹/提取数据/云MAS投诉/19年云MAS投诉/云MAS各省1月百万投诉比.xlsx'
sheet_name1 = '1月云MAS全部投诉'
save_path = 'E://新建文件夹/提取数据/云MAS投诉/201901/201901相似度匹配结果.xls'

workbook1 = xlrd.open_workbook(path)

sheet1  = workbook1.sheets()[0]
row_num1 = sheet1.nrows
col_num1 = sheet1.ncols
content_list = []
for i in range(row_num1):
    rowlist = []
    for j in range(col_num1):
        rowlist.append(sheet1.cell_value(i,j))
    content_list.append(rowlist)
repeat_dic = {}
for i in range(1,row_num1):
    if repeat_dic.keys().__contains__(content_list[i][0]):
        repeat_dic.get(content_list[i][0]).append((content_list[i][0],content_list[i][1],content_list[i][2],content_list[i][3],content_list[i][4],content_list[i][5]))
    else:
        repeat_dic[content_list[i][0]] = (list(''))
        repeat_dic.get(content_list[i][0]).append((content_list[i][0],content_list[i][1],content_list[i][2],content_list[i][3],content_list[i][4],content_list[i][5]))




workbook2 = xlrd.open_workbook(target_path)
sheet2 = workbook2.sheet_by_name(sheet_name=sheet_name1)
row_num2 = sheet2.nrows
col_num2 = sheet2.ncols
target_dic = {}
for i in range(row_num2):
    target_dic[sheet2.cell_value(i,0)] = sheet2.cell_value(i,7)

result_list1 = []
result_list2 = []
index = 0
for i in range(repeat_dic.keys().__len__()):
    item = repeat_dic.popitem()
    if item[1].__len__()>1:
        item_code = item[0]
        item_list = item[1]
        tmp_list = []
        for j in range(item_list.__len__()):
            tmp_list.append(item_list[j])
        target_content = target_dic.get(item_code)
        result = sililar_fun(target_content,tmp_list)
        if result is not None:
            result_list1.append(result)
    else:
        item_code = item[0]
        result_list2.append(tuple((item[1][0][0],item[1][0][1],item[1][0][2],item[1][0][3],item[1][0][4],item[1][0][5],target_dic.get(item_code))))

print(result_list1.__len__())
print(len(result_list2))
new_workbook = xlwt.Workbook(encoding='utf-8')
new_sheet = new_workbook.add_sheet('结果')
fields = ['投诉编号','ecid','ec名称','投诉号码','发送内容','模板id','相似度','投诉内容']
for field in range(0, len(fields)):
    new_sheet.write(0, field, fields[field])
rowIndex = 1

for item in result_list1:
    new_sheet.write(rowIndex, 0, item[0])
    new_sheet.write(rowIndex, 1, item[1])
    new_sheet.write(rowIndex, 2, item[2])
    new_sheet.write(rowIndex, 3, item[3])
    new_sheet.write(rowIndex, 4, item[4])
    new_sheet.write(rowIndex, 5, item[5])
    new_sheet.write(rowIndex, 6, item[6])
    new_sheet.write(rowIndex, 7, item[7])
    rowIndex += 1


for item in result_list2:
    new_sheet.write(rowIndex, 0, item[0])
    new_sheet.write(rowIndex, 1, item[1])
    new_sheet.write(rowIndex, 2, item[2])
    new_sheet.write(rowIndex, 3, item[3])
    new_sheet.write(rowIndex, 4, item[4])
    new_sheet.write(rowIndex, 5, item[5])
    new_sheet.write(rowIndex, 7, item[6])
    rowIndex += 1
new_workbook.save(save_path)
