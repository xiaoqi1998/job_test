import requests  # 导包
from id import get_id


def oneday():
    url = 'https://www.mxnzp.com/api/daily_word/recommend'
    key = {'app_id': 'xormnrfmlu8ku9sb', 'app_secret': 'FIv7MkheiglAjHjU2YHNpNR5EZ5T08Xg',
           'idcard': '513822199803402345',
           'encoding': 'utf-8'}
    res = requests.get(url, key)  # 输入地址和请求参数
    reszult = res.json()  # 获取
    status = res.status_code
    header = res.headers
    reszult = reszult['data'][0]['content']
    print('请求连接：%s \n请求头：%s \n  请求状态：%s  \n 返回结果%s' % (url, header, status, reszult))
    return reszult
    res.close()  # 断开连接


oneday()
