#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/4/24 --

import multiprocessing


def download_from_web(q):
    data = [11, 22, 33, 44]

    for temp in data:
        q.put(temp)

    print("-----下载器已经下载完了数据并且存入队列中-----")


def analysis_data(q):
    """ 数据处理 """
    handle_data = list()
    # 从队列中获取数据
    while True:
        data = q.get()
        handle_data.append(data)
        if q.empty():
            break
    # 模拟数据处理
    print(handle_data)


def main():
    # 创建一个队列
    q = multiprocessing.Queue()
    # c创建多个进程，将队列的引用当做实参进行传递到里面

    q1 = multiprocessing.Process(target=download_from_web, args=(q,))
    q2 = multiprocessing.Process(target=analysis_data, args=(q,))
    q1.start()
    q2.start()


if __name__ == '__main__':
    main()
