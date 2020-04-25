#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/4/24 --
import time
from collections.abc import Iterable, Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        # 可以迭代的对象
        return self

    def __next__(self):
        # 迭代需要的内容
        if self.current_num < len(self.names):
            result = self.names[self.current_num]
            self.current_num += 1
            return result
        else:
            # 停止迭代
            raise StopIteration


def main():
    c = Classmate()
    c.add("jack")
    c.add("tom")
    c.add("john")

    for name in c:
        print(name)


if __name__ == '__main__':
    main()
