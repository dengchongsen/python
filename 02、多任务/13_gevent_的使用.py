from gevent import monkey
import gevent
import time

monkey.patch_all()

def fun(name, n):
    for i in range (n):
        print(name)
        print(gevent.getcurrent(), i)
        time.sleep(0.5)




gevent.joinall([
    gevent.spawn(fun, "love", 5),
    gevent.spawn(fun, "you", 6)
])