import socket
import threading

def recv_msg( udp_socket ):
    """接受数据并显示"""

    while True:
        recv_data = udp_socket.recvfrom(1024)

        print("接收到的数据：")
        # 对接收到的元组第一个数据进行解码
        print(recv_data[0].decode("gbk"))


def send_msg( udp_socket , dest_ip , dest_port ):
    """发送数据"""

    while True:
        send_data = input("请输入要发送的信息：")
        # 编码
        
        udp_socket.sendto(send_data.encode("gbk"), (dest_ip,dest_port))


def main():
    # 1、创建套接字
    udp_socket = socket.socket (socket.AF_INET,socket.SOCK_DGRAM )

    # 2、绑定信息
    udp_socket.bind(("",7890))

    # 3、获取对方IP
    dest_ip = input("请输入对方IP")
    dest_port = int( input("请输入端口"))

    # 创建两个线程去执行接收和发送
    t_recv = threading.Thread(target=recv_msg, args = ( udp_socket, ))
    t_send = threading.Thread(target=send_msg,args = ( udp_socket,dest_ip,dest_port ))

    t_recv.start()
    t_send.start()



if __name__ == "__main__":
    main()
