# -!- coding: utf-8 -!-
import sys
import difflib


def read_file(file_name):
      with open(file_name,'r',encoding='utf-8') as f:
         return f.readlines()


def compare(file1,file2,out_path):
    file1_content = read_file(file1)
    file2_content = read_file(file2)
    d = difflib.HtmlDiff()
    result = d.make_file(file1_content,file2_content,charset='gbk')
    with open(out_path,'w') as f:
        f.writelines(result)


if __name__ == '__main__':
    compare(r'E:\PycharmProjects\text_classify\venv\Include\7days.txt',r'E:\PycharmProjects\text_classify\venv\Include\one_month.txt','compare.html')