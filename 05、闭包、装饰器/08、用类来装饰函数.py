
class Test(object):
    def __init__(self,func):
        self.func = func 
    def __call__(self, *args, **kwargs):
        print("这是装饰器添加的功能")
        return self.func()

@Test   #相当于 get_str = Test(get_str)
def get_str():
    return "hahaha"


print(get_str())