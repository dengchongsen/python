#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/4/16 23:32 
# @Author : Dcs
# @Site :  
# @File : 01_类来实现一个简单的线性函数.py 
# @Software: PyCharm

class Fun(object):
    def __init__(self,k, b):
        self.k=k
        self.b=b


    def main(self,x):
        y = self.k*x + self.b
        return y

    def update(self,k,b):
        self.k = k
        self.b = b


def main():
    p=Fun(2,3)
    print(p.k, p.b)
    print(p.main(5))
    print("-"*50)
    p.update(10,10)
    print(p.k, p.b)
    print(p.main(2))
    print("运算完毕")


if __name__ == "__main__":
    main()