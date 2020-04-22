class A:
    count = 0

    def __init__(self):
        print("这是一个构造函数")
        A.count += 1

    # 定义一个类方法
    @classmethod
    def show_A_count(cls):
        print(cls.count)


a = A()
b = A()
# A.show_A_count()
print(A.count)
