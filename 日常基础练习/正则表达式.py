import re  # 导入正则的库

str = '测试正则匹配，Aa'
txt='测试正则匹配，aa'
print(re.findall(str,'测试正则匹配，AA', re.IGNORECASE))#re.IGNORECASE为忽略大小模式
print(re.match(str,'测试',))


