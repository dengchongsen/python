import multiprocessing



def wait_data(q):
    """模拟接收数据"""

    # 创建新列表
    data = list()
    while q.empty() is not True:
        data.append(q.get())

    print(data)

def download_from_web(q):
    '''模拟从网上下载东西'''
    data = [11,22,33]
    for temp in data :
        q.put(temp)



    print("下载完毕")



def main():
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target = download_from_web ,  args = (q,) )
    p2 = multiprocessing.Process(target=wait_data , args=(q , ) )
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()