# -!- coding: utf-8 -!
import jieba
from gensim import corpora,models,similarities

doc0 = "欢迎进入提醒您：绿水青山就是金山银山！进入林区，请注意森林防火，严禁一切野外用火；保护森林资源，共建生态！"
doc1 = "共享森林美景，严防森林火灾。温馨提示您：您已进入林区，请注意森林防火，保护森林资源，携手共建美丽。"
#doc2 = "欢迎进入提醒您：绿水青山就是金山银山！进入林区，请注意森林防火，严禁一切野外用火；保护森林资源，共建生态！"
# doc3 = "(1/2)各工商企业电力用户：国家能源局南方监管局“2019年用电营商环境监管评价工作调查”正式启动，并已抽取部分用户寄出邀请公函。(2/2)请收到公函的企业用户按公函操作指引参与调查答题。如已答题请忽略。感谢参与。联系人齐盼盼，18928922716"
# doc4 = "(1/2)各工商企业电力用户：国家能源局南方监管局“2019年用电营商环境监管评价工作调查”正式启动，并已抽取部分用户寄出邀请公函。(2/2)请收到公函的企业用户按公函操作指引参与调查答题。如已答题请忽略。感谢参与。联系人齐盼盼，18928922716"
# doc5 = "(1/2)各工商企业电力用户：国家能源局南方监管局“2019年用电营商环境监管评价工作调查”正式启动，并已抽取部分用户寄出邀请公函。(2/2)请收到公函的企业用户按公函操作指引参与调查答题。如已答题请忽略。感谢参与。联系人齐盼盼，18928922716"
# doc6 = "(1/2)各工商企业电力用户：国家能源局南方监管局“2019年用电营商环境监管评价工作调查”正式启动，并已抽取部分用户寄出邀请公函。(2/2)请收到公函的企业用户按公函操作指引参与调查答题。如已答题请忽略。感谢参与。联系人齐盼盼，18928922716"
# doc7 = "(1/2)各工商企业电力用户：国家能源局南方监管局“2019年用电营商环境监管评价工作调查”正式启动，并已抽取部分用户寄出邀请公函。(2/2)请收到公函的企业用户按公函操作指引参与调查答题。如已答题请忽略。感谢参与。联系人齐盼盼，18928922716"
# doc8 = "(1/2)各工商企业电力用户：国家能源局南方监管局“2019年用电营商环境监管评价工作调查”正式启动，并已抽取部分用户寄出邀请公函。(2/2)请收到公函的企业用户按公函操作指引参与调查答题。如已答题请忽略。感谢参与。联系人齐盼盼，18928922716"



doc_test="【马鞍山消防支队】【马鞍山市消防员招录办】：您已通过消防员招录政治审查，被列为待拟录用对象，请耐心等待通知。【马鞍山市消防员招录办】：您已通过消防员招录政治审查，被列为待拟录用对象，请耐心等待通知。"

all_doc = []
all_doc.append(doc0)
all_doc.append(doc1)
#all_doc.append(doc2)
# all_doc.append(doc3)
# all_doc.append(doc4)
# all_doc.append(doc5)
# all_doc.append(doc6)
# all_doc.append(doc7)
# all_doc.append(doc8)


all_doc_list = []
for doc in all_doc:
    doc_list = [word for word in jieba.cut(doc,cut_all=True)]
    all_doc_list.append(doc_list)

doc_test_list = [word for word in jieba.cut(doc_test,cut_all=True)]

dictionary = corpora.Dictionary(all_doc_list)

corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]

doc_test_vec = dictionary.doc2bow(doc_test_list)

tfidf = models.TfidfModel(corpus)
tfidf[doc_test_vec]

index = similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=len(dictionary.keys()))
sim = index[tfidf[doc_test_vec]]
hits = sorted(enumerate(sim),key=lambda item:-item[1])
print(all_doc_list)
print(doc_test_list)
print(hits)