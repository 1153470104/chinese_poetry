# -*- coding: utf-8 -*-
import xlrd
from xlutils.copy import copy


"""
利用地词合并表单，对指代相同的地词进行合并的程序
"""


# 打印数列
def print_list(list_data):
    for d in list_data:
        print(d)


# 打印字典
def print_dict(dict_data):
    for d in dict_data:
        print(d + ": " + str(dict_data[d]))


# 打印字典
def print_matrix(matrix):
    for r in matrix:
        for c in r:
            print(str(c) + "\t", end='')
        print()


def table_to_dict(table_name, number):
    # 打开excel表格
    workbook = xlrd.open_workbook(table_name)
    r_sheet = workbook.sheet_by_index(number)
    du_dict = {}

    i = 0
    while True:
        try:
            line = r_sheet.row_values(i)
            for k in range(len(line)-1):
                du_dict[line[k+1]] = line[0]
            i = i + 1
        except IndexError:
            break
        else:
            continue

    return du_dict


def table_to_list(table_name, number):
    # 打开excel表格
    workbook = xlrd.open_workbook(table_name)
    r_sheet = workbook.sheet_by_index(number)
    du_list = []

    i = 0
    while True:
        content = []
        try:
            line = r_sheet.row_values(i)
            for k in range(len(line)):
                if line[k] != '':
                    content.append(line[k])
            du_list.append(content)
            i = i + 1
        except IndexError:
            break
        else:
            continue

    return du_list


def deduplicate_excel(data_name, output_name):
    du_dict = table_to_dict("../input/地词合并表单.xlsx", 0)
    workbook = xlrd.open_workbook(data_name)
    r_sheet = workbook.sheet_by_index(0)

    book = copy(workbook)
    w_sheet = book.get_sheet(0)

    i = 0
    while True:
        try:
            i = i + 1
            word = r_sheet.cell_value(i, 4)
            if word in du_dict.keys():
                w_sheet.write(i, 4, du_dict[word])
        except IndexError:
            break
        else:
            continue

    book.save(output_name)


# deduplicate_excel("908deduplicate.xls", "908deduplicate.xls")
deduplicate_excel("../input/qujiang_label.xls", "../input/曲江deduplicate.xls")
