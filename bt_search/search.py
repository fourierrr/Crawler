# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2018-03-06 20:57:46
# @Last Modified by:   Nessaj
# @Last Modified time: 2018-05-04 13:18:25


from urllib.request import Request,urlopen
from urllib import parse
from bs4 import BeautifulSoup
import requests
import re
import base64

# proxies={
# "181.15.177.156:3128",
# "183.159.87.78:18118",
# "121.237.139.93:18118",
# "223.145.228.51:6666",
# "218.93.167.58:6666",
# "112.91.218.21:9000",
# "31.23.59.30:8080",
# "218.72.108.50:18118",
# "223.241.117.20:18118",
# "223.241.117.42:18118",
# "122.243.59.246:22917",
# "103.80.36.174:8080",
# "60.177.229.10:18118",
# "183.136.120.136:61234",
# "113.86.221.252:61234",
# "223.241.119.53:18118",
# "110.77.159.131:65205",
# "123.53.119.113:34888",
# "119.5.1.22:1133",
# "165.84.167.54:8080"
# }



"正确的传入参数需要对kw进行base64编码后再进行url编码（其实只要base64结尾的=换成%3d就行）"

def get_search_url(kw,page=1,rule=1):
    "kw是搜索关键字,page是搜索结果的页数"
    "rule是搜过结果的排序方式： 1.按create time排序  2.按File Size排序  3.按Hot排序 4.按Relevance排序"
    "默认搜索第一页，且按照create time排序"
    server="http://www.btwhat.info/search/b-"
    kw_bs64=str(base64.b64encode(kw.encode("utf-8")),'utf-8')
    keyword=kw_bs64.replace('=','%3d')
    "这里就得到了最终所需要的url中keyword部分"
    url=server+keyword+'/'+str(page)+'-'+str(rule)+'.html'
    return url

def get_bsObj(url):
    headers={'Accept': '*/*',
            'Accept-Language':'zh-CN,zh;q=0.9',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Connection': 'keep-alive',
            'Referer':'http://www.btwhat.info/'
            }
    # req=Request(url,headers=headers)
    # html=urlopen(req)
    proxies={
    'http': '223.241.118.147:18118',
    }
    # html=requests.get(url,headers=headers,proxies=proxies)
    html=requests.get(url,headers=headers)
    # bsObj=BeautifulSoup(html,'lxml')
    bsObj=BeautifulSoup(html.content,'lxml')
    return bsObj

def get_htmlcode(url):
    headers={'Accept': '*/*',
            'Accept-Language':'zh-CN,zh;q=0.9',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Connection': 'keep-alive',
            'Referer':'http://www.btwhat.info/'
            }
    # req=Request(url,headers=headers)
    # html=urlopen(req)
    html=requests.get(url,headers=headers)
    return html.status


def get_resource(bsObj):
    try :
        search_statu=bsObj.find('div',{'class':"search-statu"}).find('span').text
        print(search_statu)
        if bsObj.find('div',{'class':'bottom-pager'}).find('span') is not None:
            page=bsObj.find('div',{'class':'bottom-pager'}).find('span').text
        else:
            page='1'
        sort=bsObj.find('div',{'id':'sort-bar'}).find('b').text
        print("page:"+page+"    sort by:"+sort)
    except:
        print("无法搜索该关键字")
        "emmm，测试时发现这个网站搜索‘苍井空’会弹出404，但是搜索‘仓井 空’或者‘仓井’都能出结果，所以加了一个异常处理"
    print("------------------------------------------------------------------------------------------")
    resource_box=bsObj.findAll('h3')
    for each in resource_box :
        js_URIencode=each.find('a').text
        # decode=re.search("\(.*\?)",js_URIencode)
        # 开始准备用正则表达式匹配，但是因为小括号太多，匹配表达式不好写，会报错，无法处理小括号情形，所以放弃了
        js_URIencode=js_URIencode.replace('document.write(decodeURIComponent(','')
        js_URIencode=js_URIencode.replace('"+"','')
        js_URIencode=js_URIencode.replace('));','')
        "用replace函数取出URIencode的部分"
        "用paese.unquote解析出js_URIencode"
        resource_name=parse.unquote(js_URIencode)
        "到这里发现，名字中间会莫名穿插<b>和</b>，不知道是什么原因，删除掉就好"
        resource_name=resource_name.replace('<b>','').replace('</b>','')
        print(resource_name)
        resource_url='http://www.btwhat.info'+each.find('a').attrs['href']
        resource_bsObj=get_bsObj(resource_url)
        try:
            resource_hash=resource_bsObj.find('div',{'class':'panel-body'}).text
            "之前在这里选择是直接打印hash，后来发现上边那个韩语的页面404了，所以才加了一个异常处理"
            print(resource_hash.replace('\n',''))
            "有个小问题，为什么会空出上下各一行？？？用replace去掉换行,下边同理"
            resource_info=resource_bsObj.findAll('td')
            print ("File Type: "+resource_info[0].text.replace('\n',''),end=" ")
            "最后加个end=" "是为了输出不换行，排版美观"
            print ("||Create Time: "+resource_info[1].text.replace('\n',''),end=" ")
            print ("||Hot: "+resource_info[2].text.replace('\n',''),end=" ")
            print ("||File Size: "+resource_info[3].text.replace('\n',''),end=" ")
            print ("||File Count: "+resource_info[4].text.replace('\n','')+'\n')
        except:
            print("该资源已失效"+'\n')




if __name__ == "__main__":
    kw="头号玩家"
    url=get_search_url(kw=kw,page=1,rule=1)
    bsObj=get_bsObj(url)
    get_resource(bsObj)






