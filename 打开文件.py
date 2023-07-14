# 操作打开一个txt文档然后再关闭
txt = open(r'C:\Users\pc-11\Desktop\转正述职报告.txt', mode='r', encoding='utf-8',
           errors=None)  # 第一个必填输入文档绝对或者相对路径，mode,指模式具体看源代码，encoding是编码格式
txt = txt.read()  # 阅读文档
print(txt)  # 输入文档
