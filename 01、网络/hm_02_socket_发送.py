import socket

def main():
    # 1、创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2、绑定一个本地信息
    localaddr = ('',8081)  #''使用本机的任何一个ip
    udp_socket.bind(localaddr)
    # 3、发送数据
    udp_socket.sendto(b"hello",('192.168.1.7',8081))
    # 4、打印发送的数据
    print()
    # 5、关闭套接字e
    udp_socket.close()


if __name__ == "__main__":
    main()