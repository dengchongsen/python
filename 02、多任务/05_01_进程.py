import time
import multiprocessing


def sing():
    while True:
        print("正在唱歌")
        time.sleep(1)

def dance():
    while True :
        print("正在跳舞")
        time.sleep(1)


def main():
    p1 = multiprocessing.Process( target = sing )
    p2 = multiprocessing.Process( target = dance)
    p1.start()
    p2.start()




if __name__ == "__main__" :
    main()