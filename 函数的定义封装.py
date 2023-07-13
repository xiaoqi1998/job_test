# 用户输入两个整数，通过函数调用计算并返回和
def sum(x, y):
    z = x + y
    print('和为 %d' % z)
    return z


x = int(input('输入第一位数'))
y = int(input('输入第二位数'))
z = sum(x, y)
print(z)
