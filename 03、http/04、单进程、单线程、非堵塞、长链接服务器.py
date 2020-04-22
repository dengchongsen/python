import socket
import time 




tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.bind(("",8080))

tcp_server_socket.listen(128)

# 设置套接字为非堵塞

tcp_server_socket.setblocking(False)  

# 创建客户端套接字列表

client_socket_list = list()



while True:


    time.sleep(1)
    try:
        new_socket, new_addr = tcp_server_socket.accept()

    except Exception as ret:
        print("--------没有新的客户端到来------")

    else:
        print("只要没有产生异常，那么就意味着来了一个新的客户端")

        # 设置套接字为非堵塞
        new_socket.setblocking(False)

        client_socket_list.append(new_socket)




        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024)

            except Exception as ret:
                print("这个客户端没有发送过来数据")

            else:
                print("没有产生异常")
                print(recv_data)

                if recv_data:

                    # 对方发送过来数据
                    print("对方发送过来数据")

                else:

                    # 对方调用close()导致recv_data返回

                    client_socket.close()

                    client_socket_list.remove(client_socket)

                    print("当前客户已服务完毕")

tcp_server_socket.close()
