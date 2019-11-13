# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2018-03-08 14:46:32
# @Last Modified by:   Nessaj
# @Last Modified time: 2018-03-08 18:03:11

from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import base64
from urllib import parse

kw="python3"
kw_bs64=str(base64.b64encode(kw.encode("utf-8")),'utf-8')
keyword=kw_bs64.replace('=','%3d')
server='http://www.btwhat.info/search/b-'
url=server+keyword+'.html'

headers={'Accept': '*/*',
            'Accept-Language':'zh-CN,zh;q=0.9',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Connection': 'keep-alive',
            'Referer':'http://www.btwhat.info/'
            }
req=Request(url,headers=headers)
html=urlopen(req)
bsObj=BeautifulSoup(html,'lxml')
resource_box=bsObj.findAll('h3')
for each in resource_box :
    js_URIencode=each.find('a').text
    js_URIencode=js_URIencode.replace('document.write(decodeURIComponent(','')
    js_URIencode=js_URIencode.replace('"+"','')
    js_URIencode=js_URIencode.replace('));','')
    resource_name=parse.unquote(js_URIencode)
    resource_name=resource_name.replace('<b>','').replace('</b>','')
    print(resource_name)
    resource_url='http://www.btwhat.info'+each.find('a').attrs['href']
    print(resource_url)

    resource_req=Request(resource_url,headers=headers)
    resource_html=urlopen(resource_req)
    resource_bsObj=BeautifulSoup(resource_html,'lxml')
    resource_hash=resource_bsObj.find('div',{'class':'panel-body'}).text
    print(resource_hash.replace('\n',''))
    resource_info=resource_bsObj.findAll('td')
    print ("File Type: "+resource_info[0].text.replace('\n',''),end=" ")
    print ("||Create Time: "+resource_info[1].text.replace('\n',''),end=" ")
    print ("||Hot: "+resource_info[2].text.replace('\n',''),end=" ")
    print ("||File Size: "+resource_info[3].text.replace('\n',''),end=" ")
    print ("||File Count: "+resource_info[4].text.replace('\n','')+'\n')


