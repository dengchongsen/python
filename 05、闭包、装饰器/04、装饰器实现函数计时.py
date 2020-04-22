import time


def count_time(f):
    def count():
        print("------start to count -------")
        start_time = time.time()
        f()
        time.sleep(1)
        stop_time = time.time()
        print("time is %d " % (stop_time-start_time))

    return count

@count_time
def  fun():
    print("----test-----")
    for i in range(100):
        pass


fun()