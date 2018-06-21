# # 1.s.swapcase，大写变小写，小写变大写
# """
#        S.swapcase() -> str
#        Return a copy of S with uppercase characters converted to lowercase
#        and vice versa.
# """
# s = 'Hello World!'
# print(s.swapcase())

# # 2.S.capitalize()，返回一个首字母大写，其它小写的字符串
# """
#        S.capitalize() -> str
#        Return a capitalized version of S, i.e. make the first character
#        have upper case and the rest lower case.
# """
# s = 'Hello World!'
# print(s.capitalize())

# # 3.S.casefold()，把大小写去掉，统一的变成小写，便于比较
# """
#         S.casefold() -> str
#         Return a version of S suitable for caseless comparisons.
# """
# s = 'Hello World!'
# print(s.casefold())

# # 4.S.center(width[, fillchar])，字符串位于中间，两边用指定字符填充够指定位数
# """
#         S.center(width[, fillchar]) -> str
#         Return S centered in a string of length width. Padding is
#         done using the specified fill character (default is a space)
# """
# s = 'Hello World!'
# print(s.center(50, '-'))

# # 5.S.count(sub[, start[, end]]) -> int，查找字符串中有多少个指定字符，可以从指定位置查找
# """
#         S.center(width[, fillchar]) -> str
#         Return S centered in a string of length width. Padding is
#         done using the specified fill character (default is a space)
# """
# s = 'Hello World!'
# print(s.count('o'))
# print(s.count('o', 0, 5))

# # 6.S.endswith(suffix[, start[, end]]) -> bool，判断字符串是否以指定字符结尾
# """
#         S.endswith(suffix[, start[, end]]) -> bool
#         Return True if S ends with the specified suffix, False otherwise.
#         With optional start, test S beginning at that position.
#         With optional end, stop comparing S at that position.
#         suffix can also be a tuple of strings to try.
# """
# s = 'Hello World!'
# print(s.count('o'))
# print(s.endswith('ld!'))
# print(s.endswith('abc'))

# # 7.S.find(sub[, start[, end]]) -> int，查找字符的索引，找不到就返回-1,也可以从指定位置查找
# """
#         S.find(sub[, start[, end]]) -> int
#         Return the lowest index in S where substring sub is found,
#         such that sub is contained within S[start:end].  Optional
#         arguments start and end are interpreted as in slice notation.
#         Return -1 on failure.
# """
# s = 'Hello World!'
# print(s.find('o'))
# print(s.find('oabc'))
# print(s.find('o', 0, 3))
# print(s.find('o', 0, 5))

# # 8.S.format(*args, **kwargs) -> str，查找字符的索引，找不到就返回-1,也可以从指定位置查找
# """
#         S.format(*args, **kwargs) -> str
#         Return a formatted version of S, using substitutions from args and kwargs.
#         The substitutions are identified by braces ('{' and '}').
# """
# s2 = 'my name is {0}, i am {1} years old'
# print(s2.format('lhc', 22))
# s2 = 'my name is {0}, i am {0} years old'
# print(s2.format('lhc', 22))
# s2 = 'my name is {name}, i am {age} years old'
# print(s2.format(name='lhc', age=22))

# 9.
"""
        S.format(*args, **kwargs) -> str
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
"""

