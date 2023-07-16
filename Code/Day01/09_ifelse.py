"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""

x = int(input("请输入："))
if x > 1:
    print(3 * x - 5)
elif x >= -1 and x <= 1:
    print(x + 2)
else:
    print(5 * x + 3)           