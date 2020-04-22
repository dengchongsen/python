# 定义一个父类

class Animal:
    def eat (self):
        print("吃")

    def drink (self):
        print("喝")

    def play(self):
        print("玩")

    def sleep(self):
        print("睡")


# 定义一个子类
class Dog(Animal):
    def bark(self):
        print('小狗汪汪叫')


class XiaoTianQuan(Dog):
    # 方法重写的方式
    # 1、直接覆盖重写
    # def bark(self):
    #     print("像神一样叫。。。")
    # 2、对父类方法进行扩展
    # python3.0使用super().
    def bark(self):
        print("像神一样叫")
        super().bark()
        # python2.0
        Dog.bark(self)


fun = XiaoTianQuan()
fun.eat()
fun.drink()
fun.play()
fun.sleep()
fun.bark()
