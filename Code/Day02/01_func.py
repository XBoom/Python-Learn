"""
输入 M和 N 计算 C(M,N)
"""

def fac(num):
    result = 1
    for n in range(1, num + 1):
        result += n
    return result

m = int(input("请输入 M:"))
n = int(input("请输入 N:"))
print(fac(m)//fac(n)//fac(m - n))