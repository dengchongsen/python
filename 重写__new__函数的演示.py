class MusicPlay (object):
    def __init__(self):
        print("播放器初始化")

    def __new__(cls, *args, **kwargs):
        print ("创建对象、分配空间")
        return super().__new__(cls)


fun = MusicPlay()
print(fun)
