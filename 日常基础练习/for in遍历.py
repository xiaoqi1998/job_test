i = [1, 2, 3, 4, 5, 6]
sum = []
print(type(sum))
for sum in i:  # 从i依次遍历到sum中
    print(f'当前的数为:{sum}')
    print(type(sum))
    sum = sum.append(sum)
