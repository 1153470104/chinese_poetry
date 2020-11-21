"""
统计数量的一个脚本
内有方法：统计时间 / 统计地点+时间 / 地点+时间+类型 的一些方法
"""

# -*- coding: utf-8 -*-
import xlrd
import xlwt
from co_occur import print_list


workbook = xlrd.open_workbook("../input/qujiang_重tag_合并版1.0.xls")
r_sheet = workbook.sheet_by_index(1)
w_book = xlwt.Workbook(encoding='utf-8')
group_type = ['自然风物', '宫苑游宴', '文人集会', '个人仕途', '怀友送别', '时局变迁', '叙事游记', '科举干谒']
group_time = ['初唐', '盛唐', '中唐', '晚唐']
group_location = ['曲', '杏', '慈恩', '乐游', '芙蓉']
group_real = ['实写', '虚写']
group_wenren = ['宫苑游宴', '文人集会']
group_unreal = ['个人仕途', '怀友送别', '时局变迁', '叙事游记']
group_festival = ['宫苑游宴', '叙事游记']


def add_time_type():
    # 各个类型在初盛中晚唐各有多少
    sheet = w_book.add_sheet('type-time')
    col = group_type
    row = group_time

    r = len(row)
    c = len(col)

    matrix = []
    for i in range(r):
        matrix.append([0]*c)
    for rr in range(r):
        for cc in range(c):
            ccc = cc
            if cc == 7:
                ccc = cc+3
            i = 0
            while True:
                try:
                    i = i + 1
                    if r_sheet.cell_value(i, 7 + ccc) == 1 and r_sheet.cell_value(i, 18) == row[rr]:
                        matrix[rr][cc] = matrix[rr][cc] + 1
                except IndexError:
                    # print("get to the end")
                    break
                else:
                    continue
    print_list(matrix)
    # return matrix
    add_sheet(sheet, col, row, matrix)


def add_sheet(sheet, c_list, r_list, d_matrix):
    c = len(c_list)
    r = len(r_list)
    for cc in range(c):
        sheet.write(0, cc+1, c_list[cc])
    for rr in range(r):
        sheet.write(rr+1, 0, r_list[rr])
    for ccc in range(c):
        for rrr in range(r):
            sheet.write(rrr+1, ccc+1, d_matrix[rrr][ccc])


def add_location_time(real):
    # 各个类型在初盛中晚唐各有多少
    if real == 1:
        sheet = w_book.add_sheet('real-location-time')
    else:
        sheet = w_book.add_sheet('unreal-location-time')

    col = group_location
    row = group_time

    r = len(row)
    c = len(col)

    matrix = []
    for i in range(r):
        matrix.append([0]*c)
    for rr in range(r):
        for cc in range(c):
            # ccc = cc
            # if cc == 7:
            #     ccc = cc+3
            i = 0
            while True:
                try:
                    i = i + 1
                    if col[cc] in r_sheet.cell_value(i, 15-real) and r_sheet.cell_value(i, 18) == row[rr]:
                        matrix[rr][cc] = matrix[rr][cc] + 1
                except IndexError:
                    # print("get to the end")
                    break
                else:
                    continue
    print_list(matrix)
    # return matrix
    add_sheet(sheet, col, row, matrix)


def add_time_type_location(location):
    # 各个类型在初盛中晚唐各有多少
    sheet = w_book.add_sheet(location + 'type-time')
    col = group_type
    row = group_time

    r = len(row)
    c = len(col)

    matrix = []
    for i in range(r):
        matrix.append([0]*c)
    for rr in range(r):
        for cc in range(c):
            ccc = cc
            if cc == 7:
                ccc = cc+3
            i = 0
            while True:
                try:
                    i = i + 1
                    if location in r_sheet.cell_value(i, 15) and r_sheet.cell_value(i, 7 + ccc) == 1 and r_sheet.cell_value(i, 18) == row[rr]:
                        matrix[rr][cc] = matrix[rr][cc] + 1
                except IndexError:
                    # print("get to the end")
                    break
                else:
                    continue
    print_list(matrix)
    # return matrix
    add_sheet(sheet, col, row, matrix)


# add_time_type()
# add_location_time(1)
# add_location_time(0)
add_time_type_location('曲江')
add_time_type_location('杏园')
add_time_type_location('慈恩寺')
add_time_type_location('乐游')
add_time_type_location('芙蓉')
w_book.save('../input/result1.xls')
