"""
输入半径计算圆的周长面积
"""
radius = float(input("请输入圆的半径: "))
perimeter = 2 * 3.14156 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' ,perimeter) # 周长: %.2f 628.312
print('周长: %.2f' %perimeter) # 周长: 628.31
print('面积: %.2f' ,area)      # 面积: %.2f 31415.999999999996
print('面积: %.2f' %area)      # 面积: 31416.00