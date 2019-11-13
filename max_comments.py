# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2018-03-31 19:29:21
# @Last Modified by:   Nessaj
# @Last Modified time: 2018-04-02 22:02:10

import requests
import json
import mysql.connector
from bs4 import BeautifulSoup
import re
from urllib.request import Request,urlopen
import time
from datetime import datetime

def get_bsObj(url):
    headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': 'aliyungf_tc=AQAAAGibi0U3zgsAiSn/cl6tZtaH0EeH',
                'Host': 'news.maxjia.com',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            }
    try:
        html=requests.get(url,headers=headers,timeout=4)
        bsObj=BeautifulSoup(html.content,'lxml')
        return bsObj
    except:
        return None

def get_json(url):
    headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'zh-CN,zh;q=0.9',
             'Cache-Control': 'max-age=0',
             'Connection': 'keep-alive',
             'Cookie': 'aliyungf_tc=AQAAAIMEez2zqwoAiSn/coiI/sFGJrUT',
             'Host': 'news.maxjia.com',
             'Upgrade-Insecure-Requests': '1',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            }
    try:
        html=requests.get(url,headers=headers,timeout=5000)
        c=html.text
        myjson=json.loads(c)
        return myjson
    except:
        return None

def get_news_id(offset,limit):
    url='http://news.maxjia.com/maxnews/app/list/?&offset=%s&limit=%s'%(offset,limit)
    newslistjson=get_json(url)
    newslist=newslistjson['result']
    for each in newslist:
        Dtime=re.split(' ',each['date'])
        date=Dtime[0]
        time=Dtime[1]
        content_type=each['content_type']
        click=each['click']
        newsid=each['newsid']
        linkid=each['linkid']
        title=each['title']
        newsurl=each['newUrl']
        bsObj=get_bsObj(newsurl)
        try:
            name=bsObj.find('div',{'class':'source'})
            try:
                author=name.find('div',{'class':'name'}).text
            except:
                author=name.text
            # author=re.sub('(.+?)[1-9]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\s?(20|21|22|23|[0-1]\d):[0-5]\d:(\s*|[0-5]\d)','',author)
            # '^[1-9]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\s+(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$'
            author=name.text.replace('\n','')
            author=author.replace('&nbsp','')
            author=author.replace(' ','')
            author=author.replace('\t','')
            author=re.sub('20.+:\d{2}','',author)
            author=author.replace("\u6765\u6e90\uff1a",'')#去掉'来源:'，但是中文报错，换成Unicode
            # print(author.encode('unicode_escape'))
            # 用unicode查看，原来空格占位符是\t
            # print(author)
            print(date,time,click,newsid,linkid,author,title,newsurl,content_type)
        except :
            print('网页连接超时')

def get_news_list(offset,limit):
    url='http://news.maxjia.com/maxnews/app/list/?&offset=%s&limit=%s'%(offset,limit)
    newslistjson=get_json(url)
    try:
        newslist=newslistjson['result']
        return newslist
    except Exception as e:
        print(e)
        return None


def get_comment_json(url):
    Maxjson=get_json(url)
    comments_box=Maxjson['result']['comments']
    for comment_box in comments_box:
        comments=comment_box['comment']
        for comment in comments:
            timestamp=comment['create_at']
            userid=comment['userid']
            username=comment['username']
            newsid=Maxjson['result']['newsid']
            up=comment['up']
            text=comment['text']

def get_comments_box(url):
    Maxjson=get_json(url)
    comments_box=Maxjson['result']['comments']
    return comments_box

# get_news_id(10000,3)
if __name__ == '__main__':
    print('开始时间:%s'%(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn=mysql.connector.connect(user='root',password='123456',database='maxplus')
    cursor=conn.cursor()
    try:
        cursor.execute('''create table news
                (id integer primary key auto_increment not null,
                date text not null,
                time text not null,
                click text not null,
                newsid text not null,
                linkid text not null,
                author text not null,
                title text not null,
                newsurl text not null,
                content_type text not null);''')
        conn.commit()
    except:
        print("表news已经存在，不需要重新创建，程序继续运行")
    offset=3666
    limit=30
    # global persent
    # persent=220
    while offset<10880:
        newslist=get_news_list(offset,limit)
        persent=0
        try:
            for each in newslist:
                lenth=len(newslist)
                persent+=1
                # sys.stdout.write('正在爬取max+新闻信息...已完成%.2f%%,当前offset:%s'%((100*(offset/5000+persent/lenth))),offset)
                print('正在爬取max+新闻信息...已完成%.2f%%,当前offset:%s'%((100*(offset/10880+30*persent/lenth/10880)),offset))
                # sys.stdout.write('\r')
                # sys.stdout.flush()
                Dtime=re.split(" ",each["date"])
                date=Dtime[0]
                time=Dtime[1]
                content_type=each["content_type"]
                click=each["click"]
                newsid=each["newsid"]
                linkid=each["linkid"]
                title=each["title"]
                title=title.replace('\"','\'')
                newsurl=each["newUrl"]
                bsObj=get_bsObj(newsurl)
                try:
                    name=bsObj.find("div",{"class":"source"})
                    try:
                        author=name.find("div",{"class":"name"}).text
                    except:
                        author=name.text
                    # author=re.sub('(.+?)[1-9]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\s?(20|21|22|23|[0-1]\d):[0-5]\d:(\s*|[0-5]\d)','',author)
                    # '^[1-9]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\s+(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$'
                    author=name.text.replace("\n","")
                    author=author.replace("&nbsp","")
                    author=author.replace(" ","")
                    author=author.replace("\t","")
                    author=re.sub("20.+:\d{2}","",author)
                    author=author.replace("\u6765\u6e90\uff1a","")#去掉'来源:'，但是中文报错，换成Unicode
                    # print(author.encode('unicode_escape'))
                    # 用unicode查看，原来空格占位符是\t
                    # print(author)

                    # print(date,time,click,newsid,linkid,author,title,newsurl,content_type)
                except :
                    # print('网页连接超时')
                    author="timeout"
                cursor.execute('''insert into news
                                (date,time,click,newsid,linkid,author,title,newsurl,content_type) values
                                 ("%s","%s","%s","%s","%s","%s","%s","%s","%s")
                                '''
                                %(date,time,click,newsid,linkid,author,title,newsurl,content_type)
                              )
                conn.commit()
        except Exception as e:
            print(e)
        offset+=30

    cursor.close()
    conn.close()
    print("爬取数据完成!")
    print("结束时间:%s"%(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
