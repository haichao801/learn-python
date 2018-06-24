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

# # 9.S.index(sub[, start[, end]]) -> int 查找指定字符的索引，找不到报错，可以指定查找的范围。与s.find类似
# """
#         S.index(sub[, start[, end]]) -> int
#
#         Return the lowest index in S where substring sub is found,
#         such that sub is contained within S[start:end].  Optional
#         arguments start and end are interpreted as in slice notation.
#         Raises ValueError when the substring is not found.
# """
# s = 'Hello World!'
# print(s.index('o'))
# print(s.find('o'))

# # 10.S.isalnum() -> bool 判断字符串的字符是否都是字母和数字，不包含特殊字符
# """
#        S.isalnum() -> bool
#
#         Return True if all characters in S are alphanumeric
#         and there is at least one character in S, False otherwise.
# """
# print('22d'.isalnum())
# print('22d!'.isalnum())

# # 11.S.isalpha() -> bool 判断字符串中字符是否都是阿拉伯字母，不包含数字和特殊符号
# # """
# #         S.index(sub[, start[, end]]) -> int
# #
# #         Return the lowest index in S where substring sub is found,
# #         such that sub is contained within S[start:end].  Optional
# #         arguments start and end are interpreted as in slice notation.
# #         Raises ValueError when the substring is not found.
# # """
# # print('222'.isalpha())
# # print('abc'.isalpha())

# # 12. S.isdigit() -> bool 判断字符串中字符是否都是数字
# # """
# #        S.isdigit() -> bool
# #
# #         Return True if all characters in S are digits
# #         and there is at least one character in S, False otherwise.
# # """
# # print('2234'.isdigit())
# # print('abc'.isdigit())

# # 13. S.islower() -> bool 判断字符串中字符是否都是小写
# """
#        S.islower() -> bool
#
#         Return True if all cased characters in S are lowercase and there is
#         at least one cased character in S, False otherwise
# """
# print('aab3'.islower())
# print('aBc'.islower())

# # 14. S.istitle() -> bool 判断字符串中单词是否都以大写字母开头
# """
#        S.istitle() -> bool
#
#         Return True if S is a titlecased string and there is at least one
#         character in S, i.e. upper- and titlecase characters may only
#         follow uncased characters and lowercase characters only cased ones.
#         Return False otherwise.
# """
# print('Hello world'.istitle())
# print('Hello World'.istitle())

# # 15. S.isupper() -> bool 判断字符串中字符是否都是大写
# """
#        S.isupper() -> bool
#
#         Return True if all cased characters in S are uppercase and there is
#         at least one cased character in S, False otherwise.
# """
# print('ABCD'.isupper())
# print('abcD'.isupper())

# # 16. S.join(iterable) -> str 将序列中元素返回字符串，用S做为分隔符
# """
#        S.join(iterable) -> str
#
#         Return a string which is the concatenation of the strings in the
#         iterable.  The separator between elements is S.
# """
# names = ['tom', 'cat', 'jack']
# print(' '.join(names))
# print(','.join(names))

# # 17. S.ljust(width[, fillchar]) -> str 将字符串从左开始填充至width个字符，不足用指定字符填充
# """
#        S.ljust(width[, fillchar]) -> str
#
#         Return S left-justified in a Unicode string of length width. Padding is
#         done using the specified fill character (default is a space).
# """
# print('abcd'.ljust(20, '-'))
# print(len('abcd'.ljust(20, '-')))
# print('abdc'.rjust(20, '-'))  # s.rjust从右到左填充

# # 18. S.lower() -> str 全变成小写，和S.casefold()相同  S.upper(),全变成大写
# S = 'Hello World'
# print(S.lower())
# print(S.upper())

# # 19. S.strip 去掉空格，换行和tab键，S.lstrip，去掉左边空格，S.rstrip
# S = 'Hello World'
# S += ' '
# print(S)
# print(S.strip())
# S = '\n Hello World'
# print(S)
# print(S.lstrip())

# # 20. S.replace(old, new[, count]) -> str:  字符的替换，count是替换几个
# """
# S.replace(old, new[, count]) -> str
#
# Return a copy of S with all occurrences of substring
# old replaced by new.  If the optional argument count is
# given, only the first count occurrences are replaced.
# """
# s = 'hello world'
# print(s.replace('h', 'H'))

# # 21. S.split(sep=None, maxsplit=-1) -> list of strings: 将字符串以指定字符分割，分割的元素组成一个列表，按那个分，哪个字符就没了
# """
# S.split(sep=None, maxsplit=-1) -> list of strings
#
# Return a list of the words in S, using sep as the
# delimiter string.  If maxsplit is given, at most maxsplit
# splits are done. If sep is not specified or is None, any
# whitespace string is a separator and empty strings are
# removed from the result.
# """
# S = 'hello world'
# print(S.split('o'))

# # 22. S.title() -> str:  单词首字母变成大写
# """
# S.title() -> str
#
# Return a titlecased version of S, i.e. words start with title case
# characters, all remaining cased characters have lower case.
# """
# S = 'hello world'
# print(S.title())
