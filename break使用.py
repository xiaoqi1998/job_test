#写一个循环，从python找到o后停止循环
a='python'
b=[]
for c in a:
    print('当前的字符是'+c)
    b.append(c)
    print(b)
    if c=='o':
        break
