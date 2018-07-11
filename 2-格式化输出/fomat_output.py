# # 填入多个数据时，填入的内容组成一个元祖
# name = input("name:")
# age = input("age:")
# job = input("job:")
# town = input("town:")
# info = '''
# -------------info of %s-----------------
# name:           %s
# age:            %s
# job:            %s
# town:           %s
# -------------end------------------------
# ''' % (name, name, age, job, town)
#
# print(info)

# # 要填入的数据只有一个时，不需要元祖了，直接把内容放到%后面就行了
# print('my name is %s' % 'jack')

# # 没有对齐的格式
# vs = [('jack', 8756), ('patrick', 10000)]
# fs = """
# %s salary: %d $
# %s salary: %d $
# """
# print(fs % (vs[0][0], vs[0][1], vs[1][0], vs[1][1]))

# # 指定最小宽度，不足则左侧补空格，右对齐
# vs = [('jack', 8756), ('patrick', 10000)]
# fs = """
# %10s salary: %10d $
# %10s salary: %10d $
# """
# print(fs % (vs[0][0], vs[0][1], vs[1][0], vs[1][1]))

# # 加减号，指定最小宽度，不足则右侧补空格，左对齐
# vs = [('jack', 8756), ('patrick', 10000)]
# fs = """
# %-10s salary: %10d $
# %-10s salary: %10d $
# """
# print(fs % (vs[0][0], vs[0][1], vs[1][0], vs[1][1]))

# # 用0补齐，此处只能用%d，用%s实现不了效果
# vs = [('jack', 8756), ('patrick', 10000)]
# fs = """
# %-10s salary: %010d $
# %-10s salary: %010d $
# """
# print(fs % (vs[0][0], vs[0][1], vs[1][0], vs[1][1]))

# # 浮点数，可以控制小数点后保留的位数，还可以控制小数点前的位数，不足用空格或0补足
# data = 1234.567890
# print('%.2f' % data)
# print('%10.2f' % data)
# print('%010.2f' % data)

# # 第二种字符串格式化方法，用字符串的format()内置函数格式化，用{}占位
# print('my name is {}'.format('xiaobai'))
# print('my name is {}, i am {} years old'.format('xiaobai', 18))
# print('my name is {1}, i am {0} years old'.format(16, 'xiaobai'))  # 可以不按次序填入
# print('{0}-{1} | {1}-{0}'.format('xiaobai', 18))  # 节省输入
# print('my name is {name}, i am {age} years old'.format(age=16, name='xiaobai'))  # 关键字参数

# # 用字符串的format()内置函数格式化时指定宽度
# print('my name is {:10}, i am {:10} years old'.format('xiaobai', 18))
# print('my name is {:10}, i am {:<10} years old'.format('xiaobai', 18))
# print('my name is {:10}, i am {:010} years old'.format('xiaobai', 18))

# # 字符串内本身就有花括号时，要用两个花括号
# print('{:.2f} {{你好}}'.format(1234.567890))

# python 3.6 以后的新格式化方法
age = 18
print(f'my age is {age}')
print(f'my age is {age:10}')

