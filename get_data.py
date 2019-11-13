from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen("https://baike.baidu.com/item/Python/407313")
bsObj=BeautifulSoup(html,'lxml')

for link in bsObj.findAll("a",href=re.compile(r"/item/.*")):
    if "href" in link.attrs:
        print (link.attrs["href"])
