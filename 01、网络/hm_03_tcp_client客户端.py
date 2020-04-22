import socket

def main():
    # 1、创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2、连接服务器
    server_ip = input("请输入服务器的IP")
    server_port = int(input("请输入要连接的服务器端口："))
    server_addr = (server_ip , server_port)
    tcp_client_socket.connect(server_addr)

    # 3、发送/接受数据
    send_data = input("请输入要发送的数据：")
    tcp_client_socket.send( send_data.encode("gbk") )
    # 4、关闭套接字
    tcp_client_socket.close()



if __name__ == "__main__":
    main()