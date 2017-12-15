#!/user/bin/env python
#coding: utf-8
'''
created on 2017-11-27
@author: XiaoYaoYou
'''
import urllib2
import os
import re

class Spider():
    def __init__(self):
        self.url = 'http://www.maiziedu.com/course/teachers/?page=%s'
        self.user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
        self.headers = {'User-Agent': self.user_agent}

    def get_page(self,page_index):
        request = urllib2.Request(url=self.url % str(page_index), headers=self.headers)
        response = urllib2.urlopen(request)
        content = response.read()
        return content
        pass
    def analysis(self, content):
        pattern = re.compile(r'(a title=".*?").*?(简介：</span>.*?)</p>', re.S)
        items = re.findall(pattern, content)
        return items

    def save(self, items):
        for item in items:
            t = (item[0].replace('a title="','',6)).replace('"','',6)
            # t = ((item[0].replace('a title="', '', 6)).replace('"', '', 6)).encode("GBK")
            print(t)

            # for m in item:

            path='teachers'
            if not os.path.exists(path):
                os.makedirs(path)
            file_path = path + '/' + 'teachers' + '.txt'
            f = open(file_path,'a+')
            f.write((item[0].replace('a title="','',6)).replace('"','',6) +' ' + item[1])
            f.close()
    def run(self):
        for i in range(1,2):
            content = self.get_page(i)
            item = self.analysis(content)
            self.save(item)
        print(item)

s=Spider()
s.run()