# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2018-04-06 16:18:40
# @Last Modified by:   Nessaj
# @Last Modified time: 2018-04-06 19:20:47

from bs4 import BeautifulSoup
import requests

# url = 'http://ip.chinaz.com/'
# proxies = {
#     # 'http': 'http://223.241.119.138:18118',
#     'https': '223.241.118.147:18118'
#     }
# headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
# }
# r = requests.get(url, headers=headers,proxies=proxies)
# soup = BeautifulSoup(r.text, 'lxml')
# parent_node = soup.find(class_="IpMRig-tit")
# for i in parent_node.find_all('dd'):
#     print(i.get_text())

url = 'https://music.douban.com/subject/26480723/'
proxies = {
    # 'http': 'http://223.241.119.138:18118',
    'https': '61.143.16.161:40301'
    }
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
r = requests.get(url, headers=headers,proxies=proxies)
# r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
# name=soup.find('div',{'id':'wrapper'})
# print(name.get_text())
print(r)
print(soup.encode('utf-8'))
# meta={'proxy': 'https://221.229.252.98:9797'},