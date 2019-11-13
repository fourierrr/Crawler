# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2018-03-15 16:09:43
# @Last Modified by:   Nessaj
# @Last Modified time: 2018-03-16 18:21:52

import requests
from urllib.request import urlopen,Request
import mysql.connector
from bs4 import BeautifulSoup
import re
import json
from urllib3 import *
import sys
import time

class bra(object):
    """docstring for bra"""
    def __init__(self, arg):
        super(bra, self).__init__()
        self.arg = arg


"妈的鸡，没用代理池，被天猫反爬了，有机会试试x-follow-for代理，现在先用urllib3的PoolManager试试"
http = PoolManager()
# req=Request(url,headers=headers)
# req=requests.get(url,headers=headers)
# http = PoolManager()
# req = http.request('GET',url,headers = headers)
# c = req.data.decode('GB18030')
# html=urlopen(req)
# bsObj=BeautifulSoup(html.text,'lxml')
# ratelist=bsObj.find('ratelist')
# tmalljson = json.loads(c)
# c = req.text
# c = c.replace('jsonp862(','')
# c = c.replace(')','')
# c = c.replace('false','"false"')
# c = c.replace('true','"true"')
# hjson=json.loads(c)
# "狗比，！！！不是标准格式的json，浪费了；劳资一个小时解析"
# rateList = hjson['rateDetail']['rateList']
# for each in rateList:
#     auctionSku=each['auctionSku']
#     m=re.split('[:;]',auctionSku)
#     Dtime=each['rateDate']
#     color=m[1]
#     size=m[3]
#     print(color+' '+size+' '+Dtime)
# print(box.attrs['data-id'])
# https://rate.tmall.com/list_detail_rate.htm?itemId=15620105540&spuId=385196899&sellerId=1813097055&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvr9vnvRQvUvCkvvvvvjiPPFzhQjibPLMO0jYHPmPZ6ji2nLsvQjlnRLFUtjlbRphvCvvvvvmjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvvEvpCW2Cghvvw0afmxfXkOjo2UlnoO%2Bul1pc7QD70OVC69%2FXxr1EkKfvDr1WBl5dUf8r1leE7rejvr%2BExr1CkKNpRxfwLhd3ODNKBlKWVTKfyCvm9vvvvvphvvvvvvvQCvpvC4vvv2vhCv2UhvvvWvphvWgvvvvQCvpvs9kphvC99vvOC0puyCvv9vvUv14nyyvphCvvOvUvvvphvPvpvhvv2MMghCvvswMUiJ7rMwznswxxItvpvhvvvvvUhCvvswjVHJkaMwznAwSxI%3D&isg=BISEdD5Ggt0zijbXUNPHv3knVQJ8V6LObbbu3J4lHs8SySaTxq9_l58LDWERUeBf&needFold=0&_ksTS=1521101116012_861&callback=jsonp862

def getjson(itemid,currentpage):
    url="https://rate.tmall.com/list_detail_rate.htm?itemId="+itemid+"&spuId=385196899&sellerId=1813097055&order=3&currentPage="+str(currentpage)+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvr9vnvRQvUvCkvvvvvjiPPFzhQjibPLMO0jYHPmPZ6ji2nLsvQjlnRLFUtjlbRphvCvvvvvmjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvvEvpCW2Cghvvw0afmxfXkOjo2UlnoO%2Bul1pc7QD70OVC69%2FXxr1EkKfvDr1WBl5dUf8r1leE7rejvr%2BExr1CkKNpRxfwLhd3ODNKBlKWVTKfyCvm9vvvvvphvvvvvvvQCvpvC4vvv2vhCv2UhvvvWvphvWgvvvvQCvpvs9kphvC99vvOC0puyCvv9vvUv14nyyvphCvvOvUvvvphvPvpvhvv2MMghCvvswMUiJ7rMwznswxxItvpvhvvvvvUhCvvswjVHJkaMwznAwSxI%3D&isg=BISEdD5Ggt0zijbXUNPHv3knVQJ8V6LObbbu3J4lHs8SySaTxq9_l58LDWERUeBf&needFold=0&_ksTS=1521101116012_861&callback=jsonp862"

    headers={'Accept': '*/*',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        # 'Connection': 'keep-alive',
        'referer':'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.5db27ba4m5LhwD&id=522608622465&skuId=3750867506726&areaId=110100&user_id=1813097055&cat_id=2&is_b=1&rn=d4065dd632f0d0b7f568128b6f92bf56',
        'authority':'rate.tmall.com',
        'method':'GET',
        'scheme':'https',
        'cookie':'hng=CN%7Czh-CN%7CCNY%7C156; cna=fz7uEg1JLDgCAWp4zoiqQOmC; _med=dw:1536&dh:864&pw:1920&ph:1080&ist:0; cq=ccp%3D1; uss=; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; enc=fOuvy2uG1X0Obmd%2BzWs9pIUHmRAoLQbvv6J7xH8z06VMhhRjw73%2F7U93Ug7YQylFPEiJUyHRdzOl3k4W5bmkMA%3D%3D; tk_trace=1; t=454ba56cbff59f40d1ada6edf95a9cdc; uc3=nk2=o7DQahuPFp4c%2BNKeVFs%3D&id2=UU6lRD6a3mOPCw%3D%3D&vt3=F8dBz4TTKM3rwEa0h%2F0%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; tracknick=%5Cu62C9%5Cu683C%5Cu6717%5Cu65E5%5Cu7684%5Cu8511%5Cu89C6; lgc=%5Cu62C9%5Cu683C%5Cu6717%5Cu65E5%5Cu7684%5Cu8511%5Cu89C6; _tb_token_=f4eb336ee1e6b; cookie2=136e594b3554db301029fd5bda69dc4c; res=scroll%3A1506*6097-client%3A1506*716-offset%3A1506*6097-screen%3A1536*864; swfstore=52041; pnm_cku822=098%23E1hvC9vUvbpvUpCkvvvvvjiPPFzhzjimPLMv1jivPmPptjl8n2dwsjrmR2FZ0jEvRsyCvvpvvvvvmphvLvQ6vvvj4OmDYE7rVC63D7zWaBw0EZKa64jGjEDspRFhAnQwHFXXiXVvQE01Ux8x9WLyjLyDZacEKOmAdch%2BYExr18TxOy%2Fn3feUHdotvpvIvvvvvhCvvvvvvUEtphvUWQvvvQCvpvACvvv2vhCv2RvvvvWvphvWvOyCvvOUvvVvay8ivpvUvvmvW7AbolUCvpvVvvpvvhCv2QhvCvvvvvm5vpvhvvmv99%3D%3D; isg=BJ2drJsDm5d2-H980dROpChYrHmdcNvF3Jnnd19i6fQjFr1IJwrh3GuERAoQ1unE'

        }


    # r = http.request('GET',url,headers = headers)
    # c = r.data.decode('GB18030')
    proxy={'https':'123.206.75.213:8080',}
    req=requests.get(url,headers=headers)
    c=req.text
    c = c.replace('jsonp862(','')
    c = c.replace(')','')
    c = c.replace('false','"false"')
    c = c.replace('true','"true"')
    Tmalljson=json.loads(c)
    "狗比，！！！不是标准格式的json，浪费了；劳资一个小时解析"
    return Tmalljson

def getitemids():
    url='https://list.tmall.com/search_product.htm?q=bra'
    headers={'Accept': '*/*',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        # 'Connection': 'keep-alive',
        'referer':'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.5db27ba4m5LhwD&id=522608622465&skuId=3750867506726&areaId=110100&user_id=1813097055&cat_id=2&is_b=1&rn=d4065dd632f0d0b7f568128b6f92bf56',
        'authority':'rate.tmall.com',
        'method':'GET',
        'scheme':'https',
        'cookie':'hng=CN%7Czh-CN%7CCNY%7C156; cna=fz7uEg1JLDgCAWp4zoiqQOmC; _med=dw:1536&dh:864&pw:1920&ph:1080&ist:0; cq=ccp%3D1; uss=; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; enc=fOuvy2uG1X0Obmd%2BzWs9pIUHmRAoLQbvv6J7xH8z06VMhhRjw73%2F7U93Ug7YQylFPEiJUyHRdzOl3k4W5bmkMA%3D%3D; tk_trace=1; t=454ba56cbff59f40d1ada6edf95a9cdc; uc3=nk2=o7DQahuPFp4c%2BNKeVFs%3D&id2=UU6lRD6a3mOPCw%3D%3D&vt3=F8dBz4TTKM3rwEa0h%2F0%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; tracknick=%5Cu62C9%5Cu683C%5Cu6717%5Cu65E5%5Cu7684%5Cu8511%5Cu89C6; lgc=%5Cu62C9%5Cu683C%5Cu6717%5Cu65E5%5Cu7684%5Cu8511%5Cu89C6; _tb_token_=f4eb336ee1e6b; cookie2=136e594b3554db301029fd5bda69dc4c; res=scroll%3A1506*6097-client%3A1506*716-offset%3A1506*6097-screen%3A1536*864; swfstore=52041; pnm_cku822=098%23E1hvC9vUvbpvUpCkvvvvvjiPPFzhzjimPLMv1jivPmPptjl8n2dwsjrmR2FZ0jEvRsyCvvpvvvvvmphvLvQ6vvvj4OmDYE7rVC63D7zWaBw0EZKa64jGjEDspRFhAnQwHFXXiXVvQE01Ux8x9WLyjLyDZacEKOmAdch%2BYExr18TxOy%2Fn3feUHdotvpvIvvvvvhCvvvvvvUEtphvUWQvvvQCvpvACvvv2vhCv2RvvvvWvphvWvOyCvvOUvvVvay8ivpvUvvmvW7AbolUCvpvVvvpvvhCv2QhvCvvvvvm5vpvhvvmv99%3D%3D; isg=BJ2drJsDm5d2-H980dROpChYrHmdcNvF3Jnnd19i6fQjFr1IJwrh3GuERAoQ1unE'
        }

    proxy={'https':'123.206.75.213:8080',}
    html=requests.get(url,headers=headers)
    bsObj=BeautifulSoup(html.content,'lxml')
    # r = http.request('GET',url,headers = headers)
    # c = r.data.decode('GB18030')
    # bsObj=BeautifulSoup(c,'lxml')
    # bsObj=BeautifulSoup(bsObj,'lxml')
    box=bsObj.findAll('div',{'class':"product"})
    # print(bsObj)
    itemids=[]
    for each in box:
        itemid=each.attrs['data-id']

        itemids.append(itemid)
    return itemids

def getdata(json):
    rateList = json['rateDetail']['rateList']
    for each in rateList:
        auctionSku=each['auctionSku']
        m=re.split('[:;]',auctionSku)
        Dtime=each['rateDate']
        color=m[1]
        size=m[3]
        # print('天猫 '+color+' '+size+' '+Dtime)

def getpagenum(itemid):
    Tmalljson=getjson(itemid,1)
    pagenum=Tmalljson['rateDetail']['paginator']['lastPage']
    return pagenum

conn=mysql.connector.connect(user='root',password='123456',database='bra')
cursor=conn.cursor()
# 之前已经创建过表了，现在注释掉
cursor.execute('''create table t_sales
            (id integer primary key auto_increment not null,
            source text not null,
            color text not null,
            size text not null,
            time text not null);''')
conn.commit()

itemids=getitemids()
print(itemids)
for x in range(1,len(itemids)):
    try:
        pagenum=getpagenum(itemids[x])
        count=0
        print('success get itemid')
        for num in range(0,pagenum):
            try:
            # "可能跑到某些页面的时候，rateDetail会报错，可能是最后一页没有？直接continue"
                Tmalljson=getjson(itemids[x],num)
                rateList = Tmalljson['rateDetail']['rateList']
                for each in rateList:
                    auctionSku=each['auctionSku']
                    m=re.split('[:;]',auctionSku)
                    Dtime=each['rateDate']
                    color=m[1]
                    size=m[3]
                    cursor.execute('''insert into t_sales(source,color,size,time) values('%s','%s','%s','%s')
                               ''' %('天猫',color,size,Dtime))
                    conn.commit()
                    time.sleep(0.1)
                    count+=1
                    sys.stdout.write('正在爬取第%s/%s个商品信息...     '%(x,len(itemids))+'第%s个商品已完成: %.1f%%' % (x,100*count/(pagenum*20) ) )
                    sys.stdout.write('\r')
                    sys.stdout.flush()
            except Exception as e:
                continue
    except Exception as e:
        print(e)

cursor.close()
conn.close()




