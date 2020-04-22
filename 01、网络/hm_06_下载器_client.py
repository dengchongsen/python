import socket

def main():
    # 1、创建套接字
    tcp_socket = socket.socket( socket.AF_INET ,socket.SOCK_STREAM )

    # 2、获取服务器IP
    desk_ip = input("请输入服务端的IP地址：")

    # 3、获取服务器端口
    desk_port = int(input("请输入服务端的端口： "))

    # 4、连接服务器
    tcp_socket.connect((desk_ip,desk_port))

    # 5、发送要下载的文件名
    download_file_name = input("请输入要下载的文件名： ")

    tcp_socket.send(download_file_name.encode("utf-8"))
    # 6、获取数据
    recv_data = tcp_socket.recv(1024)
    if recv_data:
        # 7、保存
        with open("[新]"+ download_file_name, "wb") as f:
            f.write(recv_data)

    # 8、关闭套接字
    tcp_socket.close()

if __name__ == "__main__" :
    main()