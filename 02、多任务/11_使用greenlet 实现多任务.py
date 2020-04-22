import time
from greenlet import greenlet

def task_1():
    while True:
        print("-----1-----")
        time.sleep(1)
        g2.switch()



def task_2():
    while True:
        print("-----2-----")
        time.sleep(1)
        g1.switch()







g1 = greenlet(task_1)
g2 = greenlet(task_2)





if __name__ == "__main__":

    g1.switch()