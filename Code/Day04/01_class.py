class student(object):
        # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self, source_name):
        print("%s 正在学习 %s"%(self.name, source_name))
    
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看奥特曼.' % self.name)

def main():
    stu1 = student('小明', 38)
    stu1.study('Python程序设计')
    stu1.watch_movie()

    stu2 = student('小花', 15)
    stu2.study('思想品德')
    stu2.watch_movie()


if __name__ == '__main__':
    main()