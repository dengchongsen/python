# 创建动物类
class Animal(object):
    # 统计创建的对象
    # 类的属性：姓名，体重
    # 构造函数
    def __init__(self, new_name, new_weight):
        self.name = new_name
        self.weight = new_weight
        self.__age=18
        print("创建了%s 体重 %d " % (self.name, self.weight))

    def __del__(self):
        print("%s的生命结束，主人再见了" % self.name)

    def __str__(self):
        return "GoodBye"
    def age (self):
        print(self.__age)
title_1 = Animal("Amy", 50)
print(title_1)

# 私有属性无法在外界直接访问
# print (title_1.__age)
title_1.age()
print (title_1._Animal__age)
print("*" * 50)
