# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2018-03-17 16:12:11
# @Last Modified by:   Nessaj
# @Last Modified time: 2018-03-31 14:30:38

from matplotlib.pyplot import *
from pandas import *
# import mysql
import sqlalchemy
import numpy

# engine=sqlalchemy.create_engine('jdbc:mysql://localhost:3306/bra.sql?user=root&password=123456')
engine=sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost:3306/bra")
rcParams['font.sans-serif']=['SimHei']
sales=read_sql('select size1,size2 from t_sales',engine)
TmallSize1Count=sales.groupby('size1')['size1'].count()
TmallSize2Count=sales.groupby('size2')['size2'].count()
TmallSize1Total=TmallSize1Count.sum()
# TmallSize2Total=TmallSize2Count.sum()
print(TmallSize1Total)
Tmallsize1=TmallSize1Count.to_frame(name='销量')
Tmallsize1.insert(0,'比例',100*TmallSize1Count/TmallSize1Total)
Tmallsize1.index.names=['罩杯']
print(Tmallsize1)

Tmallsize2=TmallSize2Count.to_frame(name='销量')
Tmallsize2 = Tmallsize2.sort_values(['销量'], ascending=[0])
Tmallsize2.insert(0,'比例',100*TmallSize2Count/TmallSize1Total)
Tmallsize2.index.names=['胸围']
print(Tmallsize2)


labels1=[]
labels2=[]
labels1=Tmallsize1.index.tolist()
labels2=Tmallsize2.index.tolist()
for i in range(len(labels1)):
    labels1[i]=labels1[i]+'罩杯'
for i in range(len(labels2)):
    labels2[i]=labels2[i]+'胸围'

fig,(ax1,ax2)=subplots(1,2,figsize=(12,5))
ax1.pie(Tmallsize1['销量'],labels=labels1,autopct='%.2f%%')
ax2.pie(Tmallsize2['销量'],labels=labels2,autopct='%.2f%%')

ax1.legend()
ax2.legend()
ax1.axis('equal')
tight_layout()
ax2.axis('equal')
tight_layout()
show()

















































# "假的sql语句，喵的，骗我"

# select 'A' as 罩杯, printf("%.2f%%",(100.0*count(*)/(select count(*)from bra.t_sales where size is not null) ))
# as 比例, count(*) as 销量 from bra.t_sales where size1='A'
# union all
# select 'B' , printf("%.2f%%",(100.0*count(*)/(select count(*)from bra.t_sales where size is not null) )),
# count(*) as c from bra.t_sales where size1='B'
# union all
# select 'C' , printf("%.2f%%",(100.0*count(*)/(select count(*)from bra.t_sales where size is not null) )),
# count(*) as c from bra.t_sales where size1='C'
# union all
# select 'D' , printf("%.2f%%",(100.0*count(*)/(select count(*)from bra.t_sales where size is not null) )),
# count(*) as c from bra.t_sales where size1='D'
# union all
# select 'E' , printf("%.2f%%",(100.0*count(*)/(select count(*)from bra.t_sales where size is not null) )),
# count(*) as c from bra.t_sales where size1='E'
# union all
# select 'F' , printf("%.2f%%",(100.0*count(*)/(select count(*)from bra.t_sales where size is not null) )),
# count(*) as c from bra.t_sales where size1='F'
# union all
# select 'G' , printf("%.2f%%",(100.0*count(*)/(select count(*)from bra.t_sales where size is not null) )),
# count(*) as c from bra.t_sales where size1='G'
# order by 销量 desc
print('123')