# # 定义字典
# info = {
#     'stu001': 'jack',
#     'stu002': 'mike',
#     'stu003': 'tom',
# }
# print(info)

# # 增加
# info = {
#     'stu001': 'jack',
#     'stu002': 'mike',
#     'stu003': 'tom',
# }
# info['stu004'] = 'xiaobai'
# print(info)

# # 修改
# info = {
#     'stu001': 'jack',
#     'stu002': 'mike',
#     'stu003': 'tom',
# }
# info['stu001'] = 'jack2'
# print(info)

# # 判断元素是否在字典中，用in
# info = {
#     'stu001': 'jack',
#     'stu002': 'mike',
#     'stu003': 'tom',
# }
# print('stu001' in info)
# print('stu005' in info)
# print('mike' in info)

# # 查找获取元素
# info = {
#     'stu001': 'jack',
#     'stu002': 'mike',
#     'stu003': 'tom',
# }
# print(info.get('stu001'))
# print(info['stu001'])
# print(info.get('stu004'))  # key值不存在时，返回none
# print(info['stu004'])      # key值不存在时，报错，所以，一般用info.get()方法

# # 删除
# info = {
#     'stu001': 'jack',
#     'stu002': 'mike',
#     'stu003': 'tom',
# }
# for i in range(1, 11):
#     info[i] = i * i
# print(info)
#
# print(info.pop(1))  # 删除指定元素并返回key值
# print(info)
#
# print(info.popitem())  # 随机删
# print(info)
#
# del info[6]  # 全局删法
# print(info)

# # 清空字典
# info = {
#     'stu001': 'jack',
#     'stu002': 'mike',
#     'stu003': 'tom',
# }
# info.clear()
# print(info)

# # 复制字典
# info = {
#     'stu001': 'jack',
#     'stu002': 'mike',
#     'stu003': 'tom',
# }
# info2 = info.copy()
# print(info2)

# # keys,values,items
# info = {'jack': [24, 'IT'], 'tom': [22, 'HR'], 'rain': 23}
# print(info)
# print(info.keys())  # key放到一个列表里
# print(info.values())  # value放到一个列表里
# print(info.items())  # 把字典的key，value变成一个元祖，整个放到一个列表里

# # update方法，类似列表的extend方法，把两个字典合成一个，没有对应的key，就添加，原字典有对应的key，则覆盖原字典的value
# info = {'jack': [24, 'IT'], 'tom': [22, 'HR'], 'rain': 23}
# dict2 = {1: 2, 2: 3, 'rain': 88}
# info.update(dict2)
# print(info)

# # setdefault方法，如果字典中有，则返回value值，没有则添加，并返回添加的value
# info = {'jack': [24, 'IT'], 'tom': [22, 'HR'], 'rain': 23}
# print(info.setdefault('rain'))
# print(info.setdefault('mk', 66))
# print(info)

# # 字典的循环
# info = {'jack': [24, 'IT'], 'tom': [22, 'HR'], 'rain': 23}
# for key in info:
#     print(key)
# for key in info:
#     print(key, info[key])
#
# for k, v in info.items():  # 这种是低效的方法
#     print(k, v)
