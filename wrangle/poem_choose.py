# -*- coding: utf-8 -*-
import xlrd
import xlwt
import xlutils

# first part is to format the data of Tang poetry
workbook = xlrd.open_workbook("../input/全唐诗数据库reformat.xls")
r_sheet = workbook.sheet_by_index(0)

workbook_tang = xlrd.open_workbook("../input/qujiang_all.xls")
r_sheet2 = workbook_tang.sheet_by_index(0)
col = r_sheet2.col_values(1)

w_book = xlwt.Workbook(encoding='utf-8')
w_sheet = w_book.add_sheet('唐诗')


def group_contains(poem_txt, w_list):
    for w in w_list:
        if w in poem_txt:
            return True
    return False


# qj_list = ['曲江', '曲池', '芙蓉池', '芙蓉园', '芙蓉苑', '杏园', '紫云楼', '慈恩寺', '宜春苑', '宜春园']
# qj_list = ['乐游原', '乐游园']
qj_list = ['雁塔']
i = 0
j = 0
while True:
    try:
        i = i + 1
        num = r_sheet.cell_value(i, 1)
        txt = r_sheet.cell_value(i, 4)
        name = r_sheet.cell_value(i, 2)
        if group_contains(txt, qj_list) and num not in col or group_contains(name, qj_list):
            print(i)
            w_sheet.write(j, 0, r_sheet.cell_value(i, 0))
            w_sheet.write(j, 1, r_sheet.cell_value(i, 1))
            w_sheet.write(j, 2, r_sheet.cell_value(i, 2))
            w_sheet.write(j, 3, r_sheet.cell_value(i, 3))
            w_sheet.write(j, 4, txt)
            j = j+1
    except IndexError:
        print("get to the end")
        break
    else:
        continue

w_book.save("../input/yanta_01.xls")
