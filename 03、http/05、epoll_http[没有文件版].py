import socket
import select



tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.bind(("", 8080))

tcp_server_socket.listen(128)

# 设置套接字为非堵塞

tcp_server_socket.setblocking(False)  




# 创建一个'epoll'对象
epl = select.epoll()

# 创建客户端套接字列表

client_socket_list = list()

fd_event_dict = dict()

while True:

    fd_event_list = epl.poll()   # 默认会堵塞，直到os检测到数据到来  通过事件通知方式 告诉这个程序，此时才会解堵塞
    


    # [(fd,event) ,(套接字对应的文件描述符，这个文件描述符到底是什么事件   例如可以调用 rcv 接收等)]
    for fd,event in fd_event_list:
        if fd == tcp_server_socket.fileno():

     # 等待新用户的接入

            new_socket, new_addr = tcp_server_socket.accept()

            epl.register(new_socket.fileno(),select.EPOLLTN )
            
            fd_event_dict[new_socket.fileno()] = new_socket

        elif event == select.EPOLLIN:

                # 判断已经链接的客户端是否有数据发送过来




            recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")


            if recv_data:

                server_client(fd_enevt_dict[fd], recv_data)        
                

            else:

                # 对方调用close()导致recv_data返回

                fd_event_dict[fd].close()
                epl.unregister(fd)
                del fd_event_dict[fd]


tcp_server_socket.close()
