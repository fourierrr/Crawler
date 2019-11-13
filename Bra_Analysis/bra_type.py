# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2018-03-18 22:47:47
# @Last Modified by:   Nessaj
# @Last Modified time: 2018-03-31 14:29:39
from matplotlib.pyplot import *
from pandas import *
# import mysql
import sqlalchemy
import numpy

# engine=sqlalchemy.create_engine('jdbc:mysql://localhost:3306/bra.sql?user=root&password=123456')
engine=sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost:3306/bra")
rcParams['font.sans-serif']=['SimHei']

sales = read_sql('select source,size1,size2 from t_sales',engine)
size1size2Count = sales.groupby(['size1','size2'])['size1'].count()
# print(type(size1size2Count))
size1size2Total = size1size2Count.sum()
print(size1size2Total)
size1size2 = size1size2Count.to_frame(name='销量')
n = 500
# 过滤出销量小等于500的组，并统计这些组的总销量，将统计结果放到DataFrame中
others = DataFrame([size1size2[size1size2['销量'] <=
     n].sum()],index=MultiIndex(levels=[[''],['其他']],labels=[[0],[0]]))

# 将“其他”销量放到记录集的最后
size1size2 = size1size2[size1size2['销量']>n].append(others)
# size1size2 = size1size2.append(others)
print(type(size1size2))
# print(size1size2)

size1size2 = size1size2.sort_values(['销量'],ascending=[0])
size1size2.insert(0,'比例',100 * size1size2Count / size1size2Total)

print(size1size2)
labels = size1size2.index.tolist()
newLabels = []
# 生成饼图外侧显示的每一部分的表示（如75B、80A等）
for label in labels:
    newLabels.append(label[1] + label[0])
pie(size1size2['销量'],labels=newLabels,autopct='%.2f%%')
legend()
axis('equal')
title('罩杯+上胸围销售比例')
tight_layout()
show()