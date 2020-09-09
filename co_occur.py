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


# 打开excel表格
workbook = xlrd.open_workbook("908deduplicate.xls")
r_sheet = workbook.sheet_by_index(0)


def get_list_top(type_txt, number):
    word_dict = {}
    i = 0
    while True:
        try:
            i = i + 1
            if r_sheet.cell_value(i, 1) == type_txt:
                if r_sheet.cell_value(i, 4) in word_dict:
                    word_dict[r_sheet.cell_value(i, 4)] = word_dict[r_sheet.cell_value(i, 4)] + 1
                else:
                    word_dict[r_sheet.cell_value(i, 4)] = 1
        except IndexError:
            print("get to the end")
            break
        else:
            continue
    sort_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    r_list = []
    for k in range(number):
        result = str(sort_list[k]).replace("(", "")
        result = result.replace(")", "")
        result = result.replace("'", "")
        result = result.split(",")[0]
        r_list.append(result)
    return r_list


def get_list(type_txt):
    """
    根据词性把词汇总为数组
    根据输入的属性，必须严格符合，从excel表格数据中提取出对应的词汇
    返回一个不重复的由这些词汇组成的列表
    :param type_txt: 属性值，
        只能是：动词、物象词、状态词、人词、时词、地点词、在哪写、写的哪 这8个
    :return: 表格中这个属性值所对应的所有词语，所组成的不重复的list
    """
    word_set = set()
    i = 0
    while True:
        try:
            i = i + 1
            if r_sheet.cell_value(i, 1) == type_txt:
                word_set.add(r_sheet.cell_value(i, 4))
        except IndexError:
            print("get to the end")
            break
        else:
            continue

    return list(word_set)


def list_co_matrix(r_list, c_list, matrix):
    """
    根据共现矩阵，排列矩阵中的共现次数（可视性好一点。。）
    打印出矩阵中两两对应的属性值，以及他们所对应的共现次数。
    :param r_list: row list, as one of the input list
    :param c_list: column list as one of the input list
    :param matrix: the co-occur matrix
        which must be calculate by the previous two list
        这里的共现矩阵必须是基于前两个列表计算出来的！不然没有任何意义，还可能出错
    """
    matrix_dict = {}
    r_len = len(r_list)
    c_len = len(c_list)
    for r in range(r_len):
        for c in range(c_len):
            matrix_dict[r_list[r] + " - " + c_list[c]] = matrix[r][c]
    print_dict(matrix_dict)


def co_matrix(r_list, c_list):
    """
    根据两个数列中的关键词计算共现矩阵
    根据输入的列属性值和行属性值，以及excel表格中的数据
    计算两两在同一个表格中的出现次数，填入矩阵中并返回
    :param r_list: r_list: row list, as one of the input list
    :param c_list: column list as one of the input list
    :return: 返回由上两个列表所计算出的共现矩阵
    """
    r = len(r_list)
    c = len(c_list)
    print("The size of matrix: " + str(r) + ", " + str(c))

    matrix = []
    for i in range(r):
        matrix.append([0]*c)

    # 遍历每一个矩阵的单位，计算该单位对应两个word的共现次数
    for y in range(r):
        r_word = r_list[y]
        for x in range(c):
            c_word = c_list[x]
            co_occur_time = 0

            # 循环统计两个word的共现次数
            i = 0
            poet_number = 0
            count = [0, 0]
            while True:
                try:
                    i = i + 1
                    if poet_number != r_sheet.cell_value(i, 0):
                        poet_number = r_sheet.cell_value(i, 0)
                        if count[0] == count[1] and count[1] == 1:
                            co_occur_time = co_occur_time + 1
                        count = [0, 0]
                    if r_sheet.cell_value(i, 4) == c_word:
                        count[0] = 1
                    elif r_sheet.cell_value(i, 4) == r_word:
                        count[1] = 1
                except IndexError:  # 用错误处理机制进行退出
                    # 避免因为到末尾导致最后一首诗的共现次数没有算入
                    # 在except中也检查一遍count，避免遗漏
                    if count[0] == count[1] and count[1] == 1:
                        co_occur_time = co_occur_time + 1
                    # print(str(y) + "get to the end")
                    break
                else:
                    continue
            matrix[y][x] = co_occur_time
        print(str(y))

    return matrix


def excel_export_co_matrix(r_list, c_list, excel_name):
    """
    根据两个数列中的关键词计算共现矩阵
    根据输入的列属性值和行属性值，以及excel表格中的数据
    export an excel table of the matrix
    :param excel_name: 要保存的矩阵名字
    :param r_list: r_list: row list, as one of the input list
    :param c_list: column list as one of the input list
    :return: 返回由上两个列表所计算出的共现矩阵
    """
    r = len(r_list)
    c = len(c_list)
    print("The size of matrix: " + str(r) + ", " + str(c))

    # new an excel file for the matrix content
    w_book = xlwt.Workbook(encoding='utf-8')
    w_sheet = w_book.add_sheet('matrix')
    ii = 0
    for c_word in c_list:
        ii = ii + 1
        w_sheet.write(0, ii, c_word)
    jj = 0
    for r_word in r_list:
        jj = jj + 1
        w_sheet.write(jj, 0, r_word)

    # 遍历每一个矩阵的单位，计算该单位对应两个word的共现次数
    for y in range(r):
        r_word = r_list[y]
        for x in range(c):
            c_word = c_list[x]
            co_occur_time = 0

            # 循环统计两个word的共现次数
            i = 0
            poet_number = 0
            count = [0, 0]
            while True:
                try:
                    i = i + 1
                    if poet_number != r_sheet.cell_value(i, 0):
                        poet_number = r_sheet.cell_value(i, 0)
                        if count[0] == count[1] and count[1] == 1:
                            co_occur_time = co_occur_time + 1
                        count = [0, 0]
                    if r_sheet.cell_value(i, 4) == c_word:
                        count[0] = 1
                    elif r_sheet.cell_value(i, 4) == r_word:
                        count[1] = 1
                except IndexError:  # 用错误处理机制进行退出
                    # 避免因为到末尾导致最后一首诗的共现次数没有算入
                    # 在except中也检查一遍count，避免遗漏
                    if count[0] == count[1] and count[1] == 1:
                        co_occur_time = co_occur_time + 1
                    # print(str(y) + "get to the end")
                    break
                else:
                    continue
            w_sheet.write(y+1, x+1, co_occur_time)
        print(str(y))
    w_book.save(excel_name)


# # test1: test print matrix & init matrix
# print_matrix(co_matrix([9, 0], [9, 8, 3]))

# # test2: test co_matrix
# print_matrix(co_matrix(["长安", "商山"], ["登", "过", "望"]))
# list_co_matrix(["长安", "商山"], ["登", "过", "望"], co_matrix(["长安", "商山"], ["登", "过", "望"]))

# # test3: test get_list()
# print(type(get_list("状态词")))
# print(get_list("状态词"))

# # test4: integrated test, 人词、物象词
# people_list = get_list("人词")
# stuff_list = get_list("物象词")
# sort_co_matrix(people_list, stuff_list, co_matrix(people_list, stuff_list))

# # test4: integrated test, 人词、物象词
# people_list = get_list("时词")
# stuff_list = get_list("地点词")
# sort_co_matrix(people_list, stuff_list, co_matrix(people_list, stuff_list))

# # test5: test matrix to excel
# excel_export_co_matrix(["长安", "商山"], ["登", "过", "望"], "商山长安.xls")

# # test4: integrated test, 人词、物象词
# people_list = get_list("时词")
# stuff_list = get_list("在哪写")
# excel_export_co_matrix(people_list, stuff_list, "时词在哪写.xls")

# test4: integrated test, 人词、物象词
# location_list = get_list_top("地点词", 50)
# excel_export_co_matrix(location_list, location_list, "地点词50.xls")

# test9
# print_list(get_list_top("物象词", 20))

# work, output some files
stuff_list50 = get_list_top("物象词", 50)
stuff_list100 = get_list_top("物象词", 100)
location_list50 = get_list_top("地点词", 50)
location_list100 = get_list_top("地点词", 100)
status_list50 = get_list_top("状态词", 50)
status_list100 = get_list_top("状态词", 100)
time_list50 = get_list_top("时词", 50)
time_list100 = get_list_top("时词", 100)
people_list50 = get_list_top("人词", 50)
people_list100 = get_list_top("人词", 100)

excel_export_co_matrix(stuff_list50, stuff_list50, "output/物象物象50.xls")
excel_export_co_matrix(location_list50, location_list50, "output/地点地点50.xls")
excel_export_co_matrix(stuff_list50, location_list50, "output/地点物象50.xls")
excel_export_co_matrix(time_list50, location_list50, "output/地点时间50.xls")
excel_export_co_matrix(people_list50, location_list50, "output/地点人50.xls")
excel_export_co_matrix(status_list50, location_list50, "output/地点状态50.xls")

excel_export_co_matrix(stuff_list100, stuff_list100, "output/物象物象100.xls")
excel_export_co_matrix(location_list100, location_list100, "output/地点地点100.xls")
excel_export_co_matrix(stuff_list100, location_list100, "output/地点物象100.xls")
excel_export_co_matrix(time_list100, location_list100, "output/地点时间100.xls")
excel_export_co_matrix(people_list100, location_list100, "output/地点人100.xls")
excel_export_co_matrix(status_list100, location_list100, "output/地点状态100.xls")
