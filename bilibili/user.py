# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2019-04-12 10:32:37
# @Last Modified by:   Nessaj
# @Last Modified time: 2019-04-15 11:50:48
import random

import requests
import json
import mysql.connector
from bs4 import BeautifulSoup
import re
# from urllib.request import Request,urlopen
import time
from datetime import datetime

def get_bsObj(url):
    headers={
                # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                # 'Accept-Encoding': 'gzip, deflate, br',
                # 'Accept-Language': 'zh-CN,zh;q=0.9',
                # 'Cache-Control': 'max-age=0',
                # 'Connection': 'keep-alive',
                # 'Cookie': 'aliyungf_tc=AQAAAGibi0U3zgsAiSn/cl6tZtaH0EeH',
                'Referer': 'https://space.bilibili.com/777536/fans/fans',
                # 'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            }

    try:
        html=requests.get(url,headers=headers,timeout=4)
        bsObj=BeautifulSoup(html.content,'lxml')
        return bsObj
    except e:
        print (e)
        return None

def get_json(url):
    headers={
                # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                # 'Accept-Encoding': 'gzip, deflate, br',
                # 'Accept-Language': 'zh-CN,zh;q=0.9',
                # 'Cache-Control': 'max-age=0',
                # 'Connection': 'keep-alive',
                # 'Cookie': 'aliyungf_tc=AQAAAGibi0U3zgsAiSn/cl6tZtaH0EeH',
                'Referer': 'https://space.bilibili.com/777536/fans/fans',
                # 'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            }
    PostData={
            'vmid': '777536',
            'pn': '1',
            'ps': '50',
            'order': 'desc',
            'jsonp': 'jsonp',
            'callback':' __jp5'
    }
    try:
        c=requests.post(url,headers=headers,data=PostData,timeout=4)
        # bsObj=BeautifulSoup(html.content,'lxml')
        # c_json=json.loads(c.text.replace("__jp5(",""))
        return c
    except e:
        print (e)
        return None



def load50():
    URL='https://api.bilibili.com/x/relation/followers?vmid=777536&pn=1&ps=50&order=desc&jsonp=jsonp&callback=__jp5'
    BSobj=get_bsObj(URL)
    # print(BSobj.get_text())
    b_json=BSobj.get_text()
    b_json=b_json.replace("__jp5(","")
    b_json=b_json.replace(")","")
    b_json=json.loads(b_json)

    # b_json=get_json(URL)
    # print(b_json)
    userlist=b_json['data']['list']
    print(len(userlist))
    for i in userlist:
        print(i['uname'])

# URL='https://api.bilibili.com/x/relation/followers?vmid=777536&pn=6&ps=50&order=desc&jsonp=jsonp'

# BSobj=get_bsObj(URL)
# # print(BSobj.get_text())
# b_json=BSobj.get_text()
# b_json=b_json.replace("__jp5(","")
# b_json=b_json.replace(")","")
# b_json=json.loads(b_json)
# userlist=b_json['data']['list']
# print(len(userlist))
# for i in userlist:
#     print(i['uname'])

def get_follow_numbers(uid='253176068'):
    my_fans=get_bsObj("https://api.bilibili.com/x/relation/stat?vmid="+uid+"&jsonp=jsonp").get_text()
    my_json=json.loads(my_fans)
    # print(my_fans)
    follower=my_json['data']['follower']
    following=my_json['data']['following']

    print("follower:",follower)
    print("following:",following)


def datetime_to_timestamp_in_milliseconds(d):
    def current_milli_time(): return int(round(time.time() * 1000))

    return current_milli_time()

def get_source():
    url='https://space.bilibili.com/7915478'
    payload = {
            '_': datetime_to_timestamp_in_milliseconds(datetime.now()),
            'mid': url.replace('https://space.bilibili.com/', '')
            }
    head={
                'Referer': 'https://space.bilibili.com/777536/fans/fans',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            }
    jsoncontent=requests.post('http://space.bilibili.com/ajax/member/GetInfo',headers=head,data=payload).text
    jsDict = json.loads(jsoncontent)
    return jsDict

# print(get_source())

def get_following():
    head={
                    'Referer': 'https://space.bilibili.com/777536/fans/fans',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
                }
    res = requests.get('https://api.bilibili.com/x/relation/stat?vmid=' + str(521476) + '&jsonp=jsonp').content.decode('utf-8')
    viewinfo = requests.get('https://api.bilibili.com/x/space/upstat?mid=' + str(10737339) + '&jsonp=jsonp',headers=head).content.decode('utf-8')

    js_fans_data = json.loads(res)
    js_viewdata = json.loads(viewinfo)
    following = js_fans_data['data']['following']
    fans = js_fans_data['data']['follower']
    archiveview = js_viewdata['data']['archive']['view']
    article = js_viewdata['data']['article']['view']
    print(following)
    print(fans)












def LoadUserAgents(uafile):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[:-1])
    random.shuffle(uas)
    return uas


uas = LoadUserAgents("user_agents.txt")




i=122
payload = {
            '_': datetime_to_timestamp_in_milliseconds(datetime.now()),
            # 'mid': url.replace('https://space.bilibili.com/', '')
            'mid':i
        }


ua = random.choice(uas)

head = {
    'User-Agent': ua,
    'Referer': 'https://space.bilibili.com/' + str(i) + '?from=search&seid=' + str(random.randint(10000, 50000)),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'space.bilibili.com',
    'cookie':'buvid3=0DE68AF6-8888-46F3-BFBF-C05CA162C94040768infoc; UM_distinctid=16a1f0257614b-02138f6e223ff28-11676f4a-1fa400-16a1f02576223a'
}

jscontent = requests.session().post(
                'http://space.bilibili.com/ajax/member/GetInfo',
                headers=head,
                data=payload,
                # proxies=proxies
                ) .content.decode('utf-8')
# jsDict = json.loads(jscontent)
# print(jsDict)
print(jscontent)