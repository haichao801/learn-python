# 10.循环names列表，打印每个元素的索引值，和元素
# count = 0
# for i in names:
#     # print(names.index(i), i)  #  index只能返回找到的第一个值的索引
#     print(count, i)
#     count += 1

# 另一种做法：
for (index, i) in enumerate(names):
    print(index, i)

# # 11.循环names列表，打印每个元素的索引值，和元素，当索引值 为偶数时，把对应的元素改成-1
# for i in names:
#     print(names.index(i), i)
#     if names.index(i) % 2 == 0:
#         names[names.index(i)] = -1
# print(names)

