def xxx1(func):
    print("start to decorate xxx1")
    def xxx2():
        print("-----xx2-----")
        func()
    return xxx2

def xxx3(func):
    print("start to decorate xxx3")
    def xxx4():
        print("----xxx4----")
        func()

    return xxx4

@xxx1
@xxx3
def test():
    print("-----test----")
    

test()