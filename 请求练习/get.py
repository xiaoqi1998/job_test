import requests


def get(url, parmals):
    res = requests.get(url, parmals)
    reszult = res.json()  # 获取
    status = res.status_code
    header = res.headers
