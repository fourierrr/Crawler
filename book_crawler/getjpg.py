# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2019-11-02 15:26:46
# @Last Modified by:   Nessaj
# @Last Modified time: 2019-11-02 17:05:18

import requests
import os
import time



# 随时登录https://book.duxiu.com/书籍频道查询修改baseurl
BaseURL="http://img.sslibrary.com/n/b98f6f5789b7ddb777497c61e37495a4MC248823616304/img0/78A34B1A6A0BB0BAB85BD8B2332F1ED285C556354C372BD5AD8DF3068ADE4EB2259AEAD571C520A1E1FFC5020FA4907489F15D29B672544D86294FE49B6F74507BE71A72956E767666A4063DDDFB068DCA13A39E203C69050AFFE34D12F0401FFF02A25F1051D881FDB3E8CD8345ADEBDC13/bf1/qw/10828210/C7D62FB548F143BE84AD34E36DE74CA1/"
# 封面
BookCoverURL=[]
BookCoverURL.append("bok001")
# 出版信息
LegURL=[]
LegURL.append("leg001")
# 前言
FowURL=[]
for i in range(3):
    i=i+1
    i=str(i)
    FowURL.append("fow00%s"%i)
# 目录
IndexURL=[]
for i in range(9):
    i=i+1
    i=str(i)
    if len(i)==1:
        i="00"+i
    elif len(i)==2:
        i="0"+i
    IndexURL.append("!00%s"%i)
# 正文
ContentURL=[]
for i in range(304):
    i=i+1
    i=str(i)
    if len(i)==1:
        i="00"+i
    elif len(i)==2:
        i="0"+i
    ContentURL.append("000%s"%i)

def get_png(URL):
    for url in URL:
        r=requests.get(BaseURL+url)
        path="D:/book/"+url+".png"
        time.sleep(0.5)
        with open(path, "wb") as f:
            f.write(r.content)
            print("finish png :"+url)

get_png(ContentURL)

# urls=[]

# def get_content(page_num):
#     for i in range(page_num):
#         i=str(i+1)
#         path="D:/book/"+i+".png"
#         if len(i)==1:
#             i="00"+i
#         elif len(i)==2:
#             i="0"+i
#         url="http://img.sslibrary.com/n/90079dbb9a25ac7b39642507ec436571MC248821408738/img0/2B4F9E38A7B17CC79B0B4190DF18CBF1AD93E7BD1AB04625F90CB3A50BF04BAEF34131F83498080A38A0F6B3C4B748203ECF2DBD3E13D328A9ACBF1E9F5074633078A23564DB39364978BC6BD93DD5E628C162D4F84115160D93A186830E412717B5AEB6C67C707501B9CCDDC3ED0E980153/bf1/qw/10828210/C7D62FB548F143BE84AD34E36DE74CA1/000%s?zoom=0"%(i)

#         # print(url)

#         r=requests.get(url)
#         time.sleep(0.6)
#         with open(path, "wb") as f:
#             f.write(r.content)
#             print("finish png NO."+i)





# r=requests.get("http://img.sslibrary.com/n/90079dbb9a25ac7b39642507ec436571MC248821408738/img0/2B4F9E38A7B17CC79B0B4190DF18CBF1AD93E7BD1AB04625F90CB3A50BF04BAEF34131F83498080A38A0F6B3C4B748203ECF2DBD3E13D328A9ACBF1E9F5074633078A23564DB39364978BC6BD93DD5E628C162D4F84115160D93A186830E412717B5AEB6C67C707501B9CCDDC3ED0E980153/bf1/qw/10828210/C7D62FB548F143BE84AD34E36DE74CA1/bok001")
# with open("D:/bookcover.png", "wb") as f:
#         f.write(r.content)
#         print("finish png")
# # print(r.content)