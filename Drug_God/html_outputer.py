#coding:utf-8


'''
Title: I am not Drug God
Author:Haijun Ma
Time:2018/11/19
'''

import pymysql
import jieba.analyse

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        res_datas = set()

        if data is None:
            return
        for d in data:
            self.datas.append(d)

    def process_data(self):
        #print(len(self.datas))
        file_object = open('./drug_god/str.txt', 'w',encoding='utf-8',errors='ignore')
        data_str = ''
        for data in self.datas:
            #data_str += data
            file_object.write(data)

        #print(data_str)
        file_object.close()



    def cut_str(self):
        content = open('./drug_god/str.txt',encoding='utf-8',errors='ignore').read()
        jieba.analyse.set_stop_words("./drug_god/stop_words.txt")
        tags = jieba.analyse.extract_tags(content, topK=1000,withWeight=True)
        file_object = open('./drug_god/cut_str.txt', 'w')
        for v, n in tags:
            #权重是小数，为了凑整，乘了一万
            #print(v + '\t' + str(int(n * 10000)))
            data_str = v + '\t' + str(int(n * 10000)) + '\n'
            file_object.write(data_str)
        file_object.close()
