#随机生成1-10的数字，用户可输入三次数字猜出随机数
import random
data=random.randint(1,10)
guess=int(input('你猜是多少'))
print(data)
if data<guess:
    print('大了')
    guess=int(input('再猜'))
    if data==guess:
        print('猜中了')
    elif data<guess:
        print('还是大了')
        print(int(input('再猜，这是最后一次机会')))
        if data==guess:
            print('猜中了')
    else:
        print('小了')
        print(int(input('继续猜')))

elif data==guess:
   print('牛逼第一次就猜中了')
else:
    print('小了')
    print(int(input('继续猜')))
    if data==guess:
        print('对了')