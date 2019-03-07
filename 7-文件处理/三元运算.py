# 非三元运算
a = 1
b = 2
if a > b:
    s = a - b
elif a < b:
    s = a + b
print(s)

# 三元运算，节省代码，看起来简洁
a = 1
b = 2
s = a -b if a > b else a + b
print(s)
