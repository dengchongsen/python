def set_level(level_num):
    print("保存权限级别",level_num)

    def set_func(func):
        print("开始函数装饰")

        def call_func(*args, **kwargs):
            if level_num == 1:
                print("--------权限验证1---------")

            elif level_num == 2:
                print("--------权限验证2----------")
            return func()
        return call_func
    return set_func
            
@set_level(1)
def test1():
    print("hahaha")

@set_level(2)
def test2():
    print("hhhhhh")



test1()
test2()
