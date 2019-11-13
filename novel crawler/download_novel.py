# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2017-11-25 23:12:23
# @Last Modified by:   Nessaj
# @Last Modified time: 2017-11-26 10:52:33

from bs4 import BeautifulSoup
import requests,sys

class download(object):
    def __init__(self):
        self.server="http://www.dingdian.me"
        self.target='http://www.dingdian.me/105194'
        self.title=[]   #每一章节的名称
        self.url=[]    #每一章节的网址
        self.length=0  #总章节数

    def getTitleUrlLength(self):   #获得每一章节的名称、网址以及总章节数
        req=requests.get(url=self.target)
        req.encoding="utf-8"
        soup=BeautifulSoup(req.text,"lxml")
        div=soup.find_all('div',id='list')
        a_bf=BeautifulSoup(str(div),"lxml")
        a=a_bf.find_all('a')
        for x in a[6:]:
            self.title.append(x.string)
            self.url.append(self.server+x.get("href"))
            self.length=  self.length+1        #长度怎么写的？？？？

    def gettext(self,targeturl):   #获得参数所指的网址的章节的正文内容
        req=requests.get(url=targeturl)
        req.encoding="utf-8"
        soup=BeautifulSoup(req.text,'lxml')
        div=soup.find_all('div',id='content')
        texts=div[0].text.replace('　　','\n\n     ')
        return texts

    def gowrite(self,path,title,text):     # 写入.text 文件的路径、写入的当前章节标题、写入的当前章节正文
        write_flag=True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(title+'\n')
            f.writelines(text)
            f.write('\n\n\n\n\n\n')


if __name__ == '__main__':
    dl=download()
    dl.getTitleUrlLength()
    print("开始下载 凡人修仙仙界篇.txt")
    for x in range(dl.length-1):
        dl.gowrite('凡人修仙仙界篇.txt',dl.title[x],dl.gettext(dl.url[x]))
        sys.stdout.write('已完成: %.3f%%' % (100*x/dl.length) + '\r')
        sys.stdout.flush()
    print('卧槽牛逼 ，这么快就下完了')