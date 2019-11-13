# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2018-03-18 22:47:47
# @Last Modified by:   Nessaj
# @Last Modified time: 2018-05-22 23:38:29
from matplotlib import pyplot as plt
from pandas import DataFrame
import pandas as pd
import sqlalchemy
import numpy as np


engine=sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost:3306/bra")
plt.rcParams['font.sans-serif']=['SimHei']

sales = pd.read_sql('select size1,size2 from t_sales',engine)


def bra1():
    size1size2=sales.groupby(['size1','size2'])['size1'].count()
    size1size2=size1size2.to_frame(name='count')
    others = DataFrame([size1size2[size1size2['count'] <=
         200].sum()],index=pd.MultiIndex(levels=[[''],['other']],labels=[[0],[0]]))
    final=pd.concat([size1size2[(size1size2['count']>200)],others])

    most10=final.sort_values(['count'])[-10:]
    labels=most10.index.tolist()
    mylabels=[]
    for label in labels:
        mylabels.append(label[1]+label[0])
    explode=[0,0,0,0,0,0,0,0,0,0.1]
    plt.figure(figsize=(10,13))
    ax1=plt.subplot()
    patches,l_text,p_text=ax1.pie(most10,labels=mylabels,autopct='%.1f%%',shadow=True,explode=explode,startangle=270,labeldistance=1.1)
    for t in l_text:
        t.set_size(20)
    for t in p_text:
        t.set_size(20)
    ax1.set_title('胸围罩杯分布',fontsize=20)
    plt.axis('equal')
    plt.tight_layout()
    legend = plt.legend( loc=(0.8,0.5),title='legend', shadow=True,fontsize=20)
    # legend.get_frame().set_facecolor('#00FFCC')
    legend.get_title().set_fontsize(fontsize = 20)
    plt.show()

def bra2():
    type=sales.groupby('size1')['size2'].count()
    type=type.to_frame(name='count')
    other=DataFrame([type[type['count']<500].sum()],index=['other'])
    finaltype=type[type['count']>=500].append(other)
    ran=finaltype.ix[['A','B','C','other','D','E']]
    plt.figure(figsize=(10,10))
    ax2=plt.subplot()
    explode=[0,0.1,0,0,0,0]
    f,l_text,p_text=ax2.pie(ran,shadow=True,startangle=90,autopct='%.1f%%',labels=ran.index,labeldistance=1.04,explode=explode)
    for t in p_text:
        t.set_size(20)
    for t in l_text:
        t.set_size(20)
    plt.axis('equal')
    ax2.set_title('罩杯分布',fontsize=20)
    plt.show()
# bra1()
# bra2()
