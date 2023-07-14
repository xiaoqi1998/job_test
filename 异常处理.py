#写一个判断获取商
def Seeking_business(x,y):
    try:
        sum=x/y
        print(sum)
    except ZeroDivisionError:
        print('0不能被除')

x=int(input('输入除数'))
y=int(input('输入被除数'))
Seeking_business(x,y)