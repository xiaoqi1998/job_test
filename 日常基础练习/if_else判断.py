sex = input('输入你的性别')  # 判断男生才能进入的场合，切年龄大于18小于40可行
if sex == '男':
    age = int(input('输入你的年龄'))
    if 40 > age > 18:
        print('满足18可以进入')
    elif age < 18:
        print('未年龄不能进入')
    else:
        print('哥别闹多大了还玩')
elif sex == '女':
    print('你是女生，不能进入')
else:
    print('你看下你输入的什么')
