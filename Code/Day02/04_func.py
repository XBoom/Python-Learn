
# 由于Python没有函数重载的概念，那么后面的定义会覆盖之前的定义
def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')


# 下面的代码会输出什么呢？
foo()