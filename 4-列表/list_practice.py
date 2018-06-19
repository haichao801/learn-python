# 1.创建一个空列表，命名为names,往里面添加old_driver,rain,jack,shanshan,peiqi,black_girl 元素
names = ['old_driver', 'rain''', 'jack', 'shanshan', 'peiqi', 'black_girl']
print(names)

# 2.往names列表里black_girl前面插入一个lihc
names.insert(names.index('black_girl'), 'lihc')
print(names)

# 3.把shanshan的名字改成中文，姗姗
names[names.index('shanshan')] = '姗姗'
print(names)

# 4.往names列表里rain的后面插入一个子列表，[oldboy, oldgirl]
names.insert(names.index('rain')+1, ['oldboy', 'oldgirl'])
print(names)

# 5.返回peiqi的索引值
print(names.index('peiqi'))

# 6.创建新列表[1,2,3,4,2,5,6,2],合并入names列表
names.extend([1, 2, 3, 4, 5, 6, 2])
print(names)

# # 7.取出names列表中索引4-7的元素
# print(names[4:8])
#
# # 8.取出names列表中索引2-10的元素，步长为2
# print(names[2:11:2])
#
# # 9.取出names列表中最后3个元素
# print(names[-3:])


