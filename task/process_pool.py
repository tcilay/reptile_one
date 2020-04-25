#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/4/24 --
from multiprocessing import Pool
import os
import time
import random


def worker(msg):
    t_start = time.time()
    print("%s 开始执行，进程号是%d", (msg, os.getpid()))
    # random.random() 随机生成0-1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))


def main():
    p = Pool(3)
    for i in range(0, 10):
        # Pool().apply_async(要调用的目标，(传递给目标的参数元组))
        # 每次循环将会空闲出来的子进程去调用目标
        p.apply_async(worker, (i,))

    print("----------------start-----------------")
    p.close()  # 关闭进程池，关闭后不在接收新的请求
    p.join()  # 等待进程池中所有子任务执行完成，必须放在close语句之后
    print("----------------end-----------------")


if __name__ == "__main__":
    main()
