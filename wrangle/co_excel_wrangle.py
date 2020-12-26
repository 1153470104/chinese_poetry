"""
本程序用于excel表格内容的去空格
"""
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
# workbook = xlrd.open_workbook("907汇总及编码.xls")
# workbook = xlrd.open_workbook("../input/1122Festival_Poems.xls")
workbook = xlrd.open_workbook("../input/1120qujiang_festival.xls")
r_sheet = workbook.sheet_by_index(2)
tang_period = [[], [], [], []]
i = 0
while True:
    try:
        if r_sheet.cell_value(i, 5) == "初唐":
            tang_period[0].append(i+1)
        elif r_sheet.cell_value(i, 5) == "盛唐":
            tang_period[1].append(i+1)
        elif r_sheet.cell_value(i, 5) == "中唐":
            tang_period[2].append(i+1)
        elif r_sheet.cell_value(i, 5) == "晚唐":
            tang_period[3].append(i+1)
        i = i + 1
    except IndexError:  # 用错误处理机制进行退出
        print("get to the end")
        break
    else:
        continue

# print(tang_period)

r_book = xlrd.open_workbook("../input/1124fes_act.xls")
sheet = r_book.sheet_by_index(0)
w_book = xlwt.Workbook()
r1 = w_book.add_sheet("初唐")
r2 = w_book.add_sheet("盛唐")
r3 = w_book.add_sheet("中唐")
r4 = w_book.add_sheet("晚唐")

i = 0
q, w, e, r = 1, 1, 1, 1
while True:
    try:
        i = i + 1
        number = sheet.cell_value(i, 0)
        if number in tang_period[0]:
            w_list = sheet.row_values(i)
            for j in range(len(w_list)):
                r1.write(q, j, w_list[j])
            q += 1
        if number in tang_period[1]:
            w_list = sheet.row_values(i)
            for j in range(len(w_list)):
                r2.write(w, j, w_list[j])
            w += 1
        if number in tang_period[2]:
            w_list = sheet.row_values(i)
            for j in range(len(w_list)):
                r3.write(e, j, w_list[j])
            e += 1
        if number in tang_period[3]:
            w_list = sheet.row_values(i)
            for j in range(len(w_list)):
                r4.write(r, j, w_list[j])
            r += 1
    except IndexError:  # 用错误处理机制进行退出
        print("get to the end")
        break
    else:
        continue

w_book.save("../input/1124act_period.xls")

# book = copy(workbook)  # 调用xlutils 里的copy函数转换原有只读workbook为可读文件
# w_sheet = book.get_sheet(0)
#
# # 循环读取一行行文本处理
# i = 0
# while True:
#     try:
#         i = i + 1
#         w_sheet.write(i, 0, r_sheet.cell_value(i, 0).replace("文件\\\\", ""))
#         w_sheet.write(i, 1, r_sheet.cell_value(i, 1).replace("节点\\\\", ""))
#         # w_sheet.write(i, 4, r_sheet.cell_value(i, 4).replace(" ", ""))
#     except IndexError:  # 用错误处理机制进行退出
#         print("get to the end")
#         break
#     else:
#         continue
#
# # 把book对应的内容存到 一个新文件里
# book.save("../input/1122fes.xls")
