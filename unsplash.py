# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2018-03-06 15:38:56
# @Last Modified by:   Nessaj
# @Last Modified time: 2018-03-10 11:12:02


# from urllib.request import urlopen,Request
import requests,json
from bs4 import BeautifulSoup
import re
"learn to use 'requests' module"

def get_bsObj(url):
    headers={'Accept': '*/*',
            'authority':'unsplash.com',
            'Accept-Language':'zh-CN,zh;q=0.9',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Connection': 'keep-alive',
            'Referer':'https://www.baidu.com/link?url=xdvkpPC4aAmAFSXrZJ_Xu0PkPVilBM-th0kKkIuQHNS&wd=&eqid=b351f4a800003262000000025aa28dba'
            }
    req=requests.get(url,headers=headers,verify=True)
    bsObj=BeautifulSoup(req.text,'lxml')
    return bsObj


def get_download_links(bsObj):
    download_box=bsObj.findAll('a',{'title':'Download photo'})

    for each in download_box:
        download_link=each.attrs['href']
        print(download_link)

if __name__ == '__main__':
    url="https://unsplash.com/search/photos/women"
    bsObj=get_bsObj(url)
    get_download_links(bsObj=bsObj)
