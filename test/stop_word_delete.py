"""
去掉一个文件夹中的所有文件中的停用词，并存到另一个文件夹中
"""
# -*- coding: utf-8 -*-
import os

stop_file = "../input/stop_word.txt"
s_f = open(stop_file, 'r', encoding="utf-8")
ll = s_f.readline()
stop_set = set()
while ll:
    stop_set.add(ll.replace("\n", ""))
    ll = s_f.readline()
s_f.close()

path1 = "../output/qj_frequency/"  # 文件夹目录
path2 = "../output/qj_frequency/1121/"  # 文件夹目录
output_path = "../output/qj_fre_2/"


def del_stop_word(path, o_path):
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    for file in files:  # 遍历文件夹
        print(file)
        if "txt" in file:  # 判断是否是txt文件
            f = open(path+file, 'r', encoding='utf-8')  # 打开文件
            line = f.readline()
            w_f = open(o_path + file, 'w', encoding='utf-8')
            while line:
                if line.split(" ")[0] not in stop_set:
                    w_f.write(line)
                line = f.readline()
            f.close()
            w_f.close()


del_stop_word(path1, output_path)
del_stop_word(path2, output_path)
