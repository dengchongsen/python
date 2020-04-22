from multiprocessing  import Pool
import os , random , sys
import time



def fun(msg):
    t_start = time.time()
    print("{}开始执行，进程号为{}" .format(msg,os.getpid() ))

    # 使用random.random()随机生成0~1的浮点数
    time.sleep(random.random()*2)

    t_stop = time.time()
    print( msg, "执行完毕，耗时 %0.2f" % (t_stop-t_start) )




def main():
    po = Pool(3)
    for i in range(10):
        #Pool().apply_async(要调用的目标，（传递给目标函数的参数元组）)

        po.apply_async(fun , (i,))


    print("----start----")

    po.close() # 关闭进程池，po不在接收新的请求
    po.join()  # 等待po中所有子进程执行完毕，必须在close()之后

    print("----end----")


if __name__ == "__main__":

    main()