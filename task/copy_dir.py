#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/4/24 --
import os
import multiprocessing
from multiprocessing import Manager, Queue
import time


def copy_file(q,file_name, old_dir_name, new_dir_name):
    """ 复制文件 """
    # print(file_name)
    # print(old_dir_name)
    # print(new_dir_name)
    time.sleep(1)
    # 读取文件
    old_file = open(old_dir_name + "/" + file_name, "rb")
    content = old_file.read()
    old_file.close()

    # 写入文件
    new_file = open(new_dir_name + "/" + file_name, "wb")
    new_file.write(content)
    new_file.close()

    q.put(file_name)


def main():
    # 获取文件夹名字
    old_dir_name = input("请输入要copy的文件夹：")
    # 创建一个新的文件
    new_dir_name = old_dir_name + "_bak"
    try:
        os.mkdir(new_dir_name)
    except:
        pass
    # 获取文件夹所有的待copy的文件名字
    file_names = os.listdir(old_dir_name)
    print(file_names)
    # 创建进程池
    p = multiprocessing.Pool(3)

    # 添加copy 进度
    # 创建队列
    q = multiprocessing.Manager().Queue()

    # 复制原文件夹中的文件，到新文件夹中去
    for file_name in file_names:
        p.apply_async(copy_file, args=(q,file_name, old_dir_name, new_dir_name))
    p.close()
    # p.join()
    file_num = len(file_names)
    copy_ok_num = 0
    while True:
        file_name = q.get()
        copy_ok_num += 1
        print("\r拷贝进度为：%.2f %%" % (copy_ok_num*100/file_num),end="")
        if copy_ok_num >= file_num:
            break



if __name__ == '__main__':
    main()
