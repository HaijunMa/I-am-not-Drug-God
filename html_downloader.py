#coding:utf-8


'''
Title: I am not Drug God
Author:Haijun Ma
Time:2018/11/19
'''

import urllib.request

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        request = urllib.request.Request(url)
        request.add_header("user-agent", "Mozilla/5.0")
        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()