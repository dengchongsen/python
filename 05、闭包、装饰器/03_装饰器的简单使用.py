

def func(f):
    def fun_1():
        print("这是一个装饰器")
        f()
    return fun_1



def test_1():
    print("---------text_1---------")


test_1()
print("-"*20)
print("以下进行装饰器的示例")


@func
def test_2():
    print("---------test_2---------")


test_2()

