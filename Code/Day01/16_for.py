"""
输入一个正整数判断它是不是素数
"""
from math import sqrt
num = int(input("请输入一个正整数"))
end = int(sqrt(num))

is_prime = True
if num < 2:
    is_prime = False
else:
    end = int(sqrt(num)) + 1
    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break
if is_prime:
    print("%d 是素数" % num)
else:
    print("%d 不是素数" % num)