import socket
def main():
    # 1、买个手机   创建套接字  socket
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2、插入手机卡   绑定本地信息  bind
    tcp_server_socket.bind(("",7788))

    # 3、将手机设置为正常的响铃模式   让默认的套接字由主动变为被动(listen)
    tcp_server_socket.listen(12)
    print("*****1*****")
    # 4、等待别人的电话的到来   accept
    new_client_socket, client_addr = tcp_server_socket.accept()
    print("******2*****")
    print(client_addr)

    # 5、接受客户端发送过来的信息
    recv_data = new_client_socket.recv(1024)
    print(recv_data)

    #6、响应
    new_client_socket.send("hahahah".encode("utf-8"))
if __name__ == "__main__":
    main()