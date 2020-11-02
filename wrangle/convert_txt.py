# -*- coding: utf-8 -*-
import xlrd

"""
把某个excel文档处理成特定模式的程序
"""


def print_list(list_data):
    for d in list_data:
        print(d)


workbook = xlrd.open_workbook("../input/标注1102.xls", encoding_override='utf-8')
sheet = workbook.sheet_by_index(0)
# poet_data = sheet.col_values(1)
i = 0
while True:
    try:
        i = i + 1
        p_data = sheet.row_values(i)
        f = open("../output/qujiangConvert/" + str(i) + ".txt", 'a', encoding='gb18030')
        f.write(str(i) + " ")
        f.write(p_data[1] + " ")
        f.write(p_data[2] + " ")
        f.write(p_data[3] + " ")
        print(type(p_data[4]))
        f.write(p_data[4])
        f.close()
    except IndexError:
        print("get to the end")
        break
    else:
        continue

#
# workbook = xlrd.open_workbook("545raw.xlsx")
# sheet = workbook.sheet_by_index(0)
# # poet_data = sheet.col_values(1)
# i = 0
# while True:
#     try:
#         i = i + 1
#         p_data = sheet.row_values(i)
#         if p_data[5] == 1.0:
#             f = open("545convert/" + str(p_data[0]) + ".txt", 'a', encoding='utf-8')
#             f.write(str(p_data[0]) + " ")
#             f.write(p_data[1] + " ")
#             f.write(p_data[2] + " ")
#             f.write(p_data[3] + " ")
#             if p_data[4] == 1.0:
#                 f.write("1 ")
#             else:
#                 f.write("0 ")
#             f.write(str(int(p_data[5])) + " ")
#             if p_data[6] == 1.0:
#                 f.write("1 ")
#             else:
#                 f.write("0 ")
#             if p_data[7] == 1.0:
#                 f.write("1 ")
#             else:
#                 f.write("0 ")
#             f.write(p_data[8] + " ")
#             f.write(p_data[9])
#             f.close()
#     except IndexError:
#         print("get to the end")
#         break
#     else:
#         continue
#
