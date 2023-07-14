# 写一个判断获取商
def seeking_business(x, y):
    try:
        sum = x / y
        print(sum)
    except Exception:
        print('报错了')


x = int(input('输入除数'))
y = int(input('输入被除数'))
seeking_business(x, y)
