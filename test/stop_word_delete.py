"""
去掉一个文件夹中的所有文件中的停用词，并存到另一个文件夹中
"""
import os

stop_file = "../input/"
s_f = open(stop_file, 'r', encoding="utf-8")
ll = s_f.readline()
stop_set = set()
while ll:
    stop_set.add(ll.replace("\n", ""))
s_f.close()

path = "../output/qj_frequency/"  # 文件夹目录
o_path = "../output/qj_fre_2/"

files = os.listdir(path)  # 得到文件夹下的所有文件名称
for file in files:  # 遍历文件夹
    if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
        f = open(path+file)  # 打开文件
        iter_f = iter(f)  # 创建迭代器
        w_f = open(o_path + file, 'w', encoding='utf-8')
        for line in iter_f:
            if line.split(" ")[0] not in stop_set:
                w_f.write(line)
        f.close()
        w_f.close()

