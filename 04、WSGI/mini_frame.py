#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/9 19:48
# @Author : Dcs
# @File : mini_frame.py
# @Software: PyCharm


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    
    file_name = env['PATH_INFO']

    if file_name == "/index.py":
        return index()

    elif file_name == "/login.py":
        return login()

    else:    
        return 'hello world!'

def login():
    return "这是一个登陆页面"

def index():
    return "这是主页"

