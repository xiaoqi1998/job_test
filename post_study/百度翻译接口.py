import random
import requests
from _md5 import *
from hashlib import md5


def fanyi(q:str, to_language:str):
    url = 'http://fanyi-api.baidu.com/api/trans/vip/translate'
    form = 'auto'
    appid = "20230712001742388"
    salt = str(random.randint(32768, 65536))
    key = 'Q2q97ZNaZNIYuRT45jo2'
    sign = appid + q + salt + key
    sign = md5(sign.encode('utf-8')).hexdigest()  # 转为MD5
    headers = {"Content-Type": "application/x-www-form-urlencoded"}  # 定义请求头
    payload = {"q": q, "from": form, "to": to_language, "appid": appid, "salt": salt, "sign": sign}  # 定义参数
    try:
        req = requests.post(url, params=payload, headers=headers)
        rz = req.json()
        print(rz['trans_result'][0]['dst'])
        return rz['trans_result'][0]['dst']
    except BaseException:
        error_info = ''
        if rz['error_code'] == 52001:
            error_info = '请求超时了'
            return error_info
        if rz['error_code'] == 52002:
            error_info = '系统错误'
            return error_info
        if rz['error_code'] == 52003:
            error_info = '未授权用户'
            return error_info
        if rz['error_code'] == 54000:
            error_info = '必填参数未填'
            return error_info
        print(error_info)
        return error_info
