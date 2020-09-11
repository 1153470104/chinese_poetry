# -*- coding: utf-8 -*-
import xlrd
import xlwt


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


def get_matrix(matrix_name):
    # 打开excel表格
    workbook = xlrd.open_workbook(matrix_name)
    r_sheet = workbook.sheet_by_index(0)
    c_lines = len(r_sheet.row_values(1))-1
    r_lines = len(r_sheet.col_values(1))-1

    matrix = []
    for i in range(r_lines):
        matrix.append([0]*c_lines)

    for j in range(r_lines):
        for k in range(c_lines):
            matrix[j][k] = r_sheet.cell_value(j+1, k+1)

    return matrix


def sort_matrix(r_list, c_list, matrix):

    matrix_dict = {}
    r_len = len(r_list)
    c_len = len(c_list)
    for r in range(r_len):
        for c in range(c_len):
            matrix_dict[r_list[r] + " - " + c_list[c]] = matrix[r][c]
    sort_list = sorted(matrix_dict.items(), key=lambda x: x[1], reverse=True)
    print_list(sort_list)


def sort_excel_matrix(matrix_name):

    e_matrix = get_matrix(matrix_name)
    workbook = xlrd.open_workbook(matrix_name)
    r_sheet = workbook.sheet_by_index(0)
    c_list = r_sheet.row_values(0)[1:]
    r_list = r_sheet.col_values(0)[1:]
    sort_matrix(r_list, c_list, e_matrix)


def matrix_flat(matrix_name, output_name):
    e_matrix = get_matrix(matrix_name)
    workbook = xlrd.open_workbook(matrix_name)
    r_sheet = workbook.sheet_by_index(0)
    c_list = r_sheet.row_values(0)[1:]
    r_list = r_sheet.col_values(0)[1:]
    r_len = len(r_list)
    c_len = len(c_list)
    book = xlwt.Workbook()
    w_sheet = book.add_sheet('0')
    i = 0
    for r in range(r_len):
        for c in range(c_len):
            for k in range(int(e_matrix[r][c])):
                w_sheet.write(i, 0, r_list[r])
                w_sheet.write(i, 1, c_list[c])
                i = i + 1
    book.save(output_name)


# sort_excel_matrix("时词在哪写.xls")
# # sort_excel_matrix("商山长安.xls")

# matrix_flat("商山长安.xls", "商山长安flat.xls")

# get the flat file of matrices
# matrix_flat("output/物象物象50.xls", "output917/物象物象50flat.xls")
# matrix_flat("output/地点地点50.xls", "output917/地点地点50flat.xls")
# matrix_flat("output/地点物象50.xls", "output917/地点物象50flat.xls")
# matrix_flat("output/地点时间50.xls", "output917/地点时间50flat.xls")
# matrix_flat("output/地点人50.xls", "output917/地点人50flat.xls")
# matrix_flat("output/地点状态50.xls", "output917/地点状态50flat.xls")
#
# matrix_flat("output/物象物象100.xls", "output917/物象物象100flat.xls")
# matrix_flat("output/地点地点100.xls", "output917/地点地点100flat.xls")
# matrix_flat("output/地点物象100.xls", "output917/地点物象100flat.xls")
# matrix_flat("output/地点时间100.xls", "output917/地点时间100flat.xls")
# matrix_flat("output/地点人100.xls", "output917/地点人100flat.xls")
# matrix_flat("output/地点状态100.xls", "output917/地点状态100flat.xls")
