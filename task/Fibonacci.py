#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/4/25 --

"""
    斐波那契数列（Fibonacci sequence），又称黄金分割数列、
    因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，
    故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34、…
"""


class Fibonacci(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return result
        else:
            raise StopIteration


if __name__ == '__main__':

    # a = 0
    # b = 1
    # num_list = list()
    # current_num = 0
    # while current_num < 10:
    #     num_list.append(a)
    #     a, b = b, a + b
    #     current_num += 1
    #
    # for num in num_list:
    #     print("%d  " % num, end="")

    fib = Fibonacci(10)
    for num in fib:
        print("%d  " % num, end="")
