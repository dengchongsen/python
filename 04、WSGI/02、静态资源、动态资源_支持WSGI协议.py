#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/9 0:14
# @Author : Dcs
# @Site :
# @File : 02、静态资源、动态资源.py
# @Software: PyCharm

import socket
import re
import multiprocessing
import mini_frame


class WSGIServer(object):

    def __init__(self):
        # 1、创建套接字
        self.tcp_server_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 2、绑定本地信息
        self.tcp_server_socket.bind(("", 8080))

        # 3、使套接字处于监听
        self.tcp_server_socket.listen(128)

    def server_client(self, new_socket):
        """为这个客户端返回数据"""
        # 1、接收浏览器发送的请求，即http请求
        # GET / HTTP / 1/1
        # ...
        request = new_socket.recv(1024).decode("utf-8")

        request_lines = request.splitlines()

        print("*" * 20)
        print("请求头")
        print(request_lines)

        # GET /index.html HTTP /1.1
        # get post

        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)
            # print("*"*20)
            # print("文件名为："+ file_name)
            if file_name == "/":
                file_name = "/index.html"

        # 2 返回HTTP格式的数据给浏览器

        if not file_name.endswith(".py"):
            """如果请求的资源不是.py结尾的就认为是静态资源（html/css/png）"""
            try:
                # print("尝试打开文件 ")
                # print(file_name)
                f = open("../03、http/" + file_name, 'rb')

            except(Exception):
                response = "HTTP/1.1/ 404 NOT FOUND \r\n"
                response += "\r\n"
                print("打开失败")
                response += "--------file not found------"
                new_socket.send(response.encode("utf-8"))

            else:
                html_content = f.read()
                f.close()
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                new_socket.send(response.encode("utf-8"))

                # print("---" * 20)
                print(html_content)
                new_socket.send(html_content)
        else:
            """如果是.py请求的是动态资源"""

            # body = "hahahhaha %s" %time.ctime()
            env = dict()

            env["PATH_INFO"] =file_name

            body = mini_frame.application(env, self.set_response_header)

            header = "HTTP/1.1 %s\r\n" % self.status
            for temp in self.headers:
                print(temp[0], temp[1])
                header += "%s:%s \r\n" % (temp[0], temp[1])
            header += "\r\n"

            response = header + body
            print("发送的数据为--------")
            print(response)
            new_socket.send(response.encode("utf-8"))

        # 关闭套接字
        new_socket.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = headers

    def run_forever(self):
        while True:
            # 4、等待客户端接入 ，生成new 客户端按套接字
            new_client_socket, new_client_addr = self.tcp_server_socket.accept()

            # 5、为这个客户服务
            p = multiprocessing.Process(
                target=self.server_client, args=(new_client_socket,))
            p.start()

            new_client_socket.close()

            # 7、关闭套接字
            new_client_socket.close()

        # 、关闭套接字
        self.tcp_server_socket.close()


def main():
    """控制整体，创建一个Web服务器对象，然后调用这个对象的run()方法"""
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()
