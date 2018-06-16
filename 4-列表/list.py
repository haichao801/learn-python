# 定义列表
L = ['a', 'b', 'c', 'd', 'a', 'e', 1, 2, ]
print('L=', L)

# # 列表的查询
# print(L[2])  # 通过索引取值
# print(L[-1])  # 通过索引从列表右边开始取值
# print(L.index('a'))  # 返回指定元素的索引值，从左到右查找，找到第一个匹配值，则返回
# print(L[L.index('a')])  # 查找指定元素的索引值，并用此索引值找到此元素
# print(L.count('a'))  # 统计指定元素的个数

# # 列表的切片,总是从左到右的
# print('L=', L)
# print('L[0:3], ', L[0:3])  # 返回从索引0至3的元素，但不包括3
# print('L[3:6], ', L[3:6])
# print('L[3:], ', L[3:])  # 返回从索引3至最后的所有值
# print('L[:3], ', L[:3])  # 返回从索引0至3的值，不包括3
# print('L[1:6:2], ', L[1:6:2])  # 返回索引1至6的值，不包括6，但是步长为2,（每隔一个元素，取一个值
# print('L[:], ', L[:])  # 返回所有的值
# print('L[::2], ', L[::2])  # 按步长为2，返回所有的值
# print('L[::-1], ', L[::-1])  # 倒序输出
# print('L[3:0:-1], ', L[3:0:-1])  # 从右到左

# # 列表的元素的增加和修改
# L.append('A')  # 列表最后面追加A
# print(L)
# L.insert(3, 'B')  # 在索引为3的地方插入一个值'B'
# print(L)
#
# L[3] = 'boy' # 修改索引为3的元素为'boy'
# print(L)
# L[4:6] = 'haichao'  # 把索引4-6的元素修改为'haichao'，不够的元素自动增加
# print(L)

# # 删除列表元素或整个列表
# L.pop()  # 删除列表最后一个元素
# print(L)
# pop3 = L.pop(3)  # 删除索引为3的元素
# print('pop3, ', pop3)  # pop方法可以取到被删除的值
# print(L)
# L.remove('h')  # 不知道元素的索引时，根据元素的值删除，删除从左到右找到的第一个元素
# print(L)
# del L[3]  # 用python全局的删除方法删除指定位置的元素
# print(L)
# del L[3:7]  # 删除多个元素
# print(L)
# # L2 = [1, 2, 3]
# # print(L2)
# # del L2
# # print(L2)  # 删除整个列表

# # 循环遍历列表
# for i in L:
#     print(i, end=',')

# # 列表排序
# # L.sort()  # 不能对包含了int和str的列表进行排序
# L2 = ['I', 'A', 'a', 'b', 'c', 'e']
# print('L2=', L2)
# L2.sort()  # 排序
# print(L2)
# L2.reverse()  # 反序
# print(L2)

# 列表其他方法
Lcopy = L.copy()  # 复制列表
print(Lcopy)
L.extend([1, 2, 3, ])  # 扩展列表
print(L)
L.clear()  # 清空列表
print(L)


