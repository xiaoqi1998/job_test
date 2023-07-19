import requests  # 导包
from id import get_id

url = 'https://www.mxnzp.com/api/daily_word/recommend'
key = {'app_id': 'xormnrfmlu8ku9sb', 'app_secret': 'FIv7MkheiglAjHjU2YHNpNR5EZ5T08Xg', 'idcard': '513822199803402345',
       'encoding': 'utf-8'}
res = requests.get(url, key)  # 输入地址和请求参数
print('url', res.request.url)  # 获取请求的地址
reszult = res.json()  # 获取
reszult = reszult['data'][0]['content']
print('返回的参数', reszult)
