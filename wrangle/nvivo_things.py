# -*- coding: utf-8 -*-
"""
处理nvivo我把空格连起来标的问题
"""
import xlrd
import xlwt

wb_input = xlrd.open_workbook("../input/bs1.xls")
sheet_input = wb_input.sheet_by_index(0)

word_type_dict = {}
i = 1
while True:
    try:
        line = sheet_input.row_values(i)
        word_type = line[1]
        word = line[3].replace(" ", "")
        if word not in word_type_dict.keys():
            word_type_dict[word] = {}
            word_type_dict[word][word_type] = 1
        elif word_type not in word_type_dict[word].keys():
            word_type_dict[word][word_type] = 1
        else:
            word_type_dict[word][word_type] = word_type_dict[word][word_type] + 1

        i = i + 1
    except IndexError:
        break
    else:
        continue

print(word_type_dict)

wb_modify = xlrd.open_workbook("../input/bsmod.xls")
sheet_modify_raw = wb_input.sheet_by_index(0)
