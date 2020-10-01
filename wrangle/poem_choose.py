# -*- coding: utf-8 -*-
import xlrd
import xlwt
import xlutils

# first part is to format the data of Tang poetry
workbook = xlrd.open_workbook("../input/全唐诗数据库0805.xlsx")
r_sheet = workbook.sheet_by_index(0)

w_book = xlwt.Workbook(encoding='utf-8')
w_sheet = w_book.add_sheet('唐诗')

i = 0
j = 0
pre_txt = ""
while True:
    print(str(i) + ", ", end='')
    print(j)
    try:
        i = i+1
        pre_txt = r_sheet.cell_value(i, 4)
        pre_txt = pre_txt.replace("<em>", "")
        pre_txt = pre_txt.replace(" ", "")
        w_sheet.write(j, 0, r_sheet.cell_value(i, 0))
        w_sheet.write(j, 1, r_sheet.cell_value(i, 1))
        w_sheet.write(j, 2, r_sheet.cell_value(i, 2))
        w_sheet.write(j, 3, r_sheet.cell_value(i, 3))
        k = i
        while r_sheet.cell_value(k+1, 0) == 0 and r_sheet.cell_value(i, 2) != "句":
            pre_txt = pre_txt + r_sheet.cell_value(i+1, 4)
            pre_txt = pre_txt.replace("<em>", "")
            pre_txt = pre_txt.replace(" ", "")
            k = k+1

        w_sheet.write(j, 4, pre_txt)
        i = k
        j = j+1

        while r_sheet.cell_value(k+1, 0) == 0 and r_sheet.cell_value(i, 2) == "句":
            k = k+1
            w_sheet.write(j, 0, r_sheet.cell_value(i, 0))
            w_sheet.write(j, 1, r_sheet.cell_value(i, 1))
            w_sheet.write(j, 2, r_sheet.cell_value(i, 2))
            w_sheet.write(j, 3, r_sheet.cell_value(i, 3))
            pre_txt = r_sheet.cell_value(k, 4)
            pre_txt = pre_txt.replace("<em>", "")
            pre_txt = pre_txt.replace(" ", "")
            k = k+1
            w_sheet.write(j, 4, pre_txt)
            j = j+1
        i = k

    except IndexError:
        w_sheet.write(j, 4, pre_txt)
        print("get to the end")
        break
    else:
        continue
w_book.save("../input/全唐诗数据库reformat.xls")

# w_book = xlwt.Workbook(encoding='utf-8')
# w_sheet = w_book.add_sheet('唐诗')
#
#
# def group_contains(poem_txt, w_list):
#     for w in w_list:
#         if poem_txt.contains(w):
#             return True
#     return False
#
#
# qj_list = ['曲江', '曲池', '芙蓉池', '芙蓉园', '芙蓉苑', '杏园', '紫云楼', '慈恩寺', '宜春苑', '宜春园']
# i = 0
# while True:
#     try:
#         i = i + 1
#         r_sheet.cell_value(i, 2)
#     except IndexError:
#         # print("get to the end")
#         break
#     else:
#         continue
