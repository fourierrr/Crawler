# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2017-11-25 17:18:23
# @Last Modified by:   Nessaj
# @Last Modified time: 2017-11-25 23:12:28
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    target="http://www.biqudu.com/31_31729/2170175.html"
    req=requests.get(url=target)
    req.encoding='utf-8'
    html=req.text
    soup=BeautifulSoup(html,"lxml")
    texts=soup.find_all('div',id='content')
    print (texts[0].text.replace('　　','\n\n     '))
