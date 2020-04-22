import socket
import time



def rec_data(new_client_socket):
    """为这个客户端返回信息"""
   # 1、接收浏览器发过来的请求
   # get /HTTP/1.1
    request = new_client_socket.recv(1024)
    print(request)

    # 3、返回http格式的数据给浏览器
    # 4、准备发送给浏览器的数据 header
    response = "http /1.1 200 ok\r\n"
    response += "\r\n"
    # 5、body


    # 打开指定文件
    with open("./index.html",'rb') as f:
            html_body = f.read()


    new_client_socket.send(response.encode("utf-8"))
    new_client_socket.send(html_body)



def main():
    # 1、创建套接字
    tcp_server_socket = socket.socket (socket.AF_INET , socket.SOCK_STREAM)

    # 2、绑定本地信息
    tcp_server_socket.bind(("", 8080))

    # 3、使套接字处于监听
    tcp_server_socket.listen(128)

    while True:
        # 4、等待客户端接入 ，生成new 客户端按套接字
        new_client_socket , new_client_addr = tcp_server_socket.accept()

        # 5、发送信息
        # new_client_socket.send("haha".encode("utf-8"))




        # 6、 接收客户请求,并响应
        rec_data(new_client_socket)

        # 7、关闭套接字
        new_client_socket.close()

    # 、关闭套接字
    tcp_server_socket.close()



if __name__ == "__main__":
    main()