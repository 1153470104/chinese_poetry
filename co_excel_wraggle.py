# -*- coding: utf-8 -*-
import xlrd
import xlwt
from xlutils.copy import copy


# 打印数列
def print_list(list_data):
    for d in list_data:
        print(d)


# 打印字典
def print_dict(dict_data):
    for d in dict_data:
        print(d + ": " + str(dict_data[d]))


# read file
workbook = xlrd.open_workbook("907汇总及编码.xls")
r_sheet = workbook.sheet_by_index(0)


book = copy(workbook) # 调用xlutils 里的copy函数转换原有只读workbook为可读文件
w_sheet = book.get_sheet(0)

# 循环读取一行行文本处理
i = 0
while True:
    try:
        i = i + 1
        # w_sheet.write(i, 0, r_sheet.cell_value(i, 0).replace("文件\\\\", ""))
        # w_sheet.write(i, 1, r_sheet.cell_value(i, 1).replace("节点\\\\", ""))
        w_sheet.write(i, 4, r_sheet.cell_value(i, 4).replace(" ", ""))
    except IndexError:  # 用错误处理机制进行退出
        print("get to the end")
        break
    else:
        continue

# 把book对应的内容存到 一个新文件里
book.save("908.xls")
