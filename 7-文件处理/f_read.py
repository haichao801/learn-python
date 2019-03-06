"""
语法格式：
f = open(file='d:/练习方式.txt', mode='r', encoding='utf-8')
data = f.read()
f.close

* f = open(file='d:/练习方式.txt', mode='r', encoding='utf-8')  表示文件路径
* mode='r'表示只读（可修改为其它）
* encoding='utf-8'表示将硬盘上的010101按照utf-8的规则去断句，再将断句后的每一段010101转换成Unicode的010101，Unicode对照表中有010101和字符的对应关系
* f.read()表示读取所有内容，内容是已经转换完毕的字符串
* f.close()表示关闭文件
"""

# 文件是以GB2312编码，此时以utf-8编码读取，会报错
f = open(file='联系方式.txt', mode='r', encoding='utf-8')
data = f.read()
print(data)
f.close()
