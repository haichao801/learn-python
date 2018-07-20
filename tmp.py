# str1 = "How are you"
# l = str1.split(' ')
# print(l)
# for s in l[::-1]:
#     print(s, end=' ')

# str1 = 'aabb@cc.com'
# print('@' in str1 and (str1.endswith('.org') or str1.endswith('.com')))

# for i in range(0, 6):
#     for j in range(0, 6-i):
#         print(' ', end="")
#     s = '* ' * i
#     print(s)


# li = [1, 2, 3, 4, 5]
# new_li = []
# for i in li:
#     if i % 2 == 0:
#         new_li.append(i+1)
# print(new_li)

# s = 'a, b, c, d, e, f'
# print(s.replace(',', ';', 5))


# li = [1, 2, 3, 4, 5, 6]
# li.reverse()
# tmp = li[0]
# li[0] = li[len(li)-1]
# li[len(li)-1] = tmp
# print(li)

# def reverse_list(li):
#     li.reverse()
#     li[0], li[len(li) - 1] = li[len(li) - 1], li[0]
#     print(li)
#
#
# li = [1, 2, 3, 4, 5, 6]
# reverse_list(li)

# 题目10
# li = ['a', 'b', 'b', 'c', 'c', 'c']
# str1 = ','.join(li)
# print(str1)
# count = {}
# for i in li:
#     count[i] = li.count(i)
# print(count)

# 题目13
# class Sum():
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         c = self.a + self.b
#         return c
#
#
# instance = Sum(1, 2)
# print(f'属性a和b的值是{instance.a}, {instance.b}')
# print(instance.add())

# def append_to(element, to=[]):
#     to.append(element)
#     return to
#
#
# list1 = append_to(12)
# print(list1)
#
# list2 = append_to(42)
# print(list2)

# def foo(a, b):
#     print (a, b)
#
#
# args = [1, 2]
# foo(*args)

# def foo(*args):
#     print(args[0], args[1])
#
#
# args = [1, 2]
# foo(*args)

# def bar(**kwargs):
#     print(kwargs["a"], kwargs["b"])
#
#
# bar(a=1, b=2)
#
# di = {"a": 1, "b": 2}
# bar(**di)

# def bar(**kwargs):
#     print(kwargs["a"], kwargs["b"])
#
# bar(1, 2)


# def foobar(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# foobar(1, 2, a=1)

# def foobar(a, b, *args, **kwargs):
#     print(a, b)
#     print(args)
#     print(kwargs)
#
#
# foobar(1, 2, 3, 4, c=5, d=6)

# a = [2, 4, 5, 6]
# for i in a:
#     if not i % 2:
#         a.remove(i)
# print(a)

y = [1, 2, 3, 4]
for idx, value in enumerate(y):
    if value == 'a':
        break

print(idx)
