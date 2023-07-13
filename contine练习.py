# 写一个循环当遍历到o时跳过这次循环
a = 'python'
b = []
for c in a:
    b.append(c)
    print(c)
    if c == 'p':
        print('遍历到o了此次循环跳过')
        continue
print(b)