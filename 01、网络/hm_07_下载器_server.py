import socket

def main():
    # 1、创建监听套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2、绑定本地信息
    tcp_server_socket.bind(("",7788))

    # 3、使套接字处于被动listen
    tcp_server_socket.listen(128)
    while True:
        # 4、等待客户端接入
        new_socket, new_addr = tcp_server_socket.accept()

        # 5、接受客户要下载的文件名
        down_file_name = new_socket.recv(1024).decode("utf-8")

        print("客户 (%s) 要下载的文件是 %s " % (str(new_addr) , down_file_name ))
        down_context = None
        # 6、尝试打开文件read
        try:
            f = open(down_file_name,'rb')
            down_context = f.read()
            f.close()

        except Exception as ret:
            print("没有要下载的文件")
        # 7、发送数据
        if down_context:
            new_socket.send (down_context)
        print("发送完毕")

        # 8、关闭客户套接字
        new_socket.close()
    tcp_server_socket.close()

if __name__ == "__main__" :
    main()