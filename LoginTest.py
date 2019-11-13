import urllib.request
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '10688440'
API_KEY = 'li5ObCpnNGNGZq7BL6H6298V'
SECRET_KEY = 'LqzImHEIS6UGZIH5uu8M0Et9UsmFckah'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
url='http://wx2.sinaimg.cn/mw690/bfdcef89gy1ffimc8bgf3j20k802i3zn.jpg'
res=client.basicGeneralUrl(url)

for item in res['words_result']:
    print(item['words'])

# url='http://www.baidu.com'
# req=urllib.request.Request(url)
# response=urllib.request.urlopen(req)
# the_page=response.read()
