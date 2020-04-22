#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/4/16 23:52 
# @Author : Dcs
# @Site :  
# @File : 02_闭包实现线性函数.py 
# @Software: PyCharm



def line(k,b):
    def create_y(x):
        print(k*x+b)

    return create_y

line_1=line(1,2)
line_1(1)
line_1(2)
line_1(3)
print("-"*20)
line_2=line(7,8)
line_2(1)
line_2(2)
line_2(3)