def set_func(func):
    print("开始装饰")
    def call_func( *args,**kwargs ):
        print("----1----")
        print(args,kwargs)
        print("----2----")
        # 返回解包类型，即数据的结构
        return func(*args,**kwargs) 

    return call_func

@set_func
def test(*args,**kwargs):
    print("----teat1-----")
    return (args,kwargs)


ret = test(5,2,0,wo=1)
print(ret)