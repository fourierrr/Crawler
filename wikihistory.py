# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2018-03-05 20:50:45
# @Last Modified by:   Nessaj
# @Last Modified time: 2018-03-05 21:34:03

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json

server="https://en.wikipedia.org/w/index.php?"
kw="python"
# url=server+"title="+kw+"&limit=500"+"&action=history"
url=server+"title="+kw+"&action=history"

html=urlopen(url)
bsObj=BeautifulSoup(html,'lxml')
users=bsObj.findAll('a',{'class':'mw-userlink mw-anonuserlink'})
ips=set()
for user in users:
    ip=user.attrs['title'].replace('Special:Contributions/','')
    ips.add(ip)

for ip in ips:
    jsonstr=urlopen("http://freegeoip.net/json/"+ip).read()
    jsonObj=json.loads(jsonstr)
    print(ip+'    is from  :'+jsonObj.get("country_name"))

