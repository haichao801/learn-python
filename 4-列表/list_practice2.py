# 10.循环names列表，打印每个元素的索引值，和元素
# names = ['alex', 'jack', 2, 'rain', 'mack', 2, 'racheal', 'shanshan', 2, 'longting']
# count = 0
# for i in names:
#     # print(names.index(i), i)  #  index只能返回找到的第一个值的索引
#     print(count, i)
#     count += 1

# 另一种做法：
# for (index, i) in enumerate(names):
#     print(index, i)

# 11.循环names列表，打印每个元素的索引值，和元素，当索引值 为偶数时，把对应的元素改成-1
# names = ['alex', 'jack', 2, 'rain', 'mack', 2, 'racheal', 'shanshan', 2, 'longting']
# for (index, i) in enumerate(names):
#     print(index, i)
#     if index % 2 == 0:
#         names[index] = -1
# print(names)

# # 12.names里有3个2，请返回第2个2的索引值。不要人肉数，要动态找(提示，找到第一个2的位置，在此基础上再找第2个)
# names = ['alex', 'jack', 'peiqi', 2, 'rain', 'mack', 2, 'racheal', 'shanshan', 2, 'longting']
# firs_index = names.index(2)
# new_list = names[firs_index+1:]
# second_index = new_list.index(2)
# second_val = firs_index + second_index + 1
# print('second_val:', second_val)

# 13.
"""
现有商品列表如下:
    products = [ ['Iphone8',6888],['MacPro',14800], ['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799] ]
    需打印出这样的格式：

    ---------商品列表----------
    0. Iphone8    6888
    1. MacPro    14800
    2. 小米6    2499
    3. Coffee    31
    4. Book    80
    5. Nike Shoes    799
"""
# products = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]
# print("--------商品列表---------")
# for index, p in enumerate(products):
#     print('%s. %s   %s' % (index, p[0], p[1]))

# 14.写一个循环，不断的问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里， 最终用户输入q退出时，打印购物车里的商品列表
products = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]
shopping_cart = []
exit_flag = False
while not exit_flag:
    print('------商品列表------')
    for index, p in enumerate(products):
        print('%s. %s   %s' % (index, p[0], p[1]))
    choice = input('输入想买的商品编号：')
    if choice.isdigit():
        choice = int(choice)
        if choice >= 0 and choice < len(products):
            shopping_cart.append(products[choice])
        else:
            print('商品不存在')
    elif choice == 'q':
        if len(shopping_cart) > 0:
            print('------您已购买过以下商品：------')
            for index, p in enumerate(shopping_cart):
                print('%s. %s   %s' % (index, p[0], p[1]))
        exit_flag = True
