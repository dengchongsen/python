import socket
def main():
    # 1、买个手机   创建套接字  socket
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2、插入手机卡   绑定本地信息  bind
    tcp_server_socket.bind(("",7788))

    # 3、将手机设置为正常的响铃模式   让默认的套接字由主动变为被动(listen)
    tcp_server_socket.listen(12)
    print("*****1*****")

    while True:
        print("等待新的客户到来")
        # 4、等待别人的电话的到来   accept
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("一个新的客户已经到来")

        #  循环为同一客户循环多次
        while True:
            # 5、接受客户端发送过来的信息
            recv_data = new_client_socket.recv(1024)
            print("客户端发来的信息 %s" % recv_data.decode("utf-8"))
            #  recv 解堵塞有两种方式
            #  1、客户端发送过来数据
            #  2、客户端调用close 导致了这里解堵塞
            #  判断客户是否自动关闭客户端

            #6、响应
            if recv_data:
                new_client_socket.send("hahahah".encode("utf-8"))
            else:
                break

        #  关闭监听套接字
    tcp_server_socket.close()
if __name__ == "__main__":
    main()