# -!- coding: utf-8 -!-
import xlrd
import jieba
import xlwt
from gensim import corpora,models,similarities


path = r'E:\新建文件夹\提取数据\相似度匹配\法制宣传日\find_similar.xls'
workbook1 = xlrd.open_workbook(path)
sheet1 = workbook1.sheet_by_name('寻找所有发送量')
row_num1 = sheet1.nrows
col_num1 = sheet1.ncols
template_list = []
for i in range(1,row_num1):
    template_list.append(sheet1.cell_value(i,2))
max_hits = []


def sililar_fun(target_content):
    doc_test = target_content
    all_doc = template_list
    all_doc_list = []
    for doc in all_doc:
        doc_list = [word for word in jieba.cut(doc,cut_all=True)]
        all_doc_list.append(doc_list)
    doc_test_list = [word for word in jieba.cut(doc_test,cut_all=True)]

    doc_test_list = list(filter(None,doc_test_list))

    print(doc_test_list)
    dictionary = corpora.Dictionary(all_doc_list)

    corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]

    doc_test_vec = dictionary.doc2bow(doc_test_list)

    tfidf = models.TfidfModel(corpus)

    tfidf[doc_test_vec]

    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
    sim = index[tfidf[doc_test_vec]]
    hits = sorted(enumerate(sim), key=lambda item: -item[1])
    results = []
    index_num = 0
    for hit in hits:
        hit_num = hit[0]
        hit_score = hit[1]
        if hit_score > 0.5:
            results.append([sheet1.cell_value(hit_num+1,0),
                                sheet1.cell_value(hit_num+1,1),
                                sheet1.cell_value(hit_num+1,2),
                                sheet1.cell_value(hit_num+1,3),
                                sheet1.cell_value(hit_num+1,4),hit_score])
    return results




target_path = r'E:\新建文件夹\提取数据\相似度匹配\法制宣传日\附件2：司法局法制宣传日短信模板.xlsx'

write_book = xlwt.Workbook()
result_sheet = write_book.add_sheet("匹配结果")
fields = ['EC客户','集团客户编码','短信内容','发送时间','发送量','匹配到的模板内容','文本相似度']
for i in range(len(fields)):
    result_sheet.write(0,i,fields[i])
row_index = 1

workbook2 = xlrd.open_workbook(target_path)
sheet2 = workbook2.sheets()[0]
row_num2 = sheet2.nrows
col_num2 = sheet2.ncols
for i in range(1,row_num2):

    target_content = sheet2.cell_value(i,0)
    results = sililar_fun(target_content)
    if results is not None:
        for line in results:
            result_sheet.write(row_index, 0, line[0])
            result_sheet.write(row_index, 1, line[1])
            result_sheet.write(row_index, 2, line[2])
            result_sheet.write(row_index, 3, line[3])
            result_sheet.write(row_index, 4, line[4])
            result_sheet.write(row_index, 5, target_content)
            result_sheet.write(row_index, 6, str(line[5]))
            row_index += 1
write_book.save(r'E:\新建文件夹\提取数据\相似度匹配\法制宣传日\相似度匹配.xls')
    #print(hit,most_score)
#     if most_hit is not None:
#         result_sheet.write(row_index, 0, sheet2.cell_value(i, 0))
#         result_sheet.write(row_index, 1, sheet2.cell_value(i, 1))
#         result_sheet.write(row_index, 2, sheet2.cell_value(i, 2))
#         result_sheet.write(row_index, 3, sheet2.cell_value(i, 3))
#         result_sheet.write(row_index, 4, sheet2.cell_value(i, 4))
#         result_sheet.write(row_index, 5, most_hit)
#         result_sheet.write(row_index, 6, str(most_score))
#         row_index += 1
# write_book.save(r'E:\新建文件夹\提取数据\相似度匹配\2\相似度匹配.xls')
