#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-22 17:38:56
# @Author  : Nessaj (Fourierrr@gmail.com)
# @Link    : http://#
# @Version : $Id$
from urllib.request import urlopen,Request
from urllib import parse
from bs4 import BeautifulSoup

# url="http://www.btwhat.info/"
url="http://www.baidu.com/s"
values={"wd":"北邮"}
data=parse.urlencode(values)#.encode(encoding='UTF8')
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'Accept': '*/*',
         'Accept-Language':'zh-CN,zh;q=0.9',
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
         'Connection': 'keep-alive',
         'Referer': 'http://www.baidu.com/'

        }
addr=url+'?'+data
req=Request(addr,headers=headers)
html=urlopen(req)
# bsObj=BeautifulSoup(html,'lxml')
# results=bsObj.findAll('div',class_="result c-container ")
# for res in results:
#     print(res)
baiduRes=""
while 1:
    kuai=html.read(1024)
    if not len(kuai):
         break
    baiduRes+=str(kuai)
"在上边这个地方纠结了好久，总是出现编码问题以及str和byte问题，尝试过encode('utf-8') encode('GBK') decode('utf-8') decode('GBK') 结果都不对 最终发现需要转化成str 于是用str()解决"

# gbkTypeStr = unicodeTypeStr.encode("GBK", 'ignore');
with open('baidu.html','w') as fp:
    fp.write(baiduRes)
"上边的问题 在这里也尝试了 很久 "
"最终结果 只写入了html骨架 没有css js 看起来就完全不是个网页"
"参考的这片https://www.cnblogs.com/cynchanpin/p/7016141.html 原作者成功了 不知道是因为py版本问题 还是百度改了网页结构"

print('success')

