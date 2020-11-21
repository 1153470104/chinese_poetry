"""
本程序主要用于计算共现矩阵

辅助函数：print_list() print_dict() print_matrix()
取得输入文本的函数：get_txt_top() get_list_top() get_list() get_dict() file_to_dict()
共现计算函数：co_matrix()
结果处理函数：dict_to_file() list_co_matrix() excel_export_co_matrix()
"""

# -*- coding: utf-8 -*-
import xlrd
import xlwt
import csv
import codecs


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
# workbook = xlrd.open_workbook("../input/908deduplicate.xls")
# workbook = xlrd.open_workbook("../input/qujiang_label.xls")
workbook = xlrd.open_workbook("../input/曲江deduplicate.xls")
r_sheet = workbook.sheet_by_index(0)
workbook2 = xlrd.open_workbook("../input/qujiang_all.xls")
p_sheet = workbook2.sheet_by_index(1)


"""function below is used to get list & get dict & get top"""


def get_txt_top(path, count):
    f = open(path, 'r', encoding='utf-8')
    t_list = []
    line = f.readline()
    for i in range(count):
        t_list.append(line.split(",")[0])
        line = f.readline()
    f.close()
    # print(t_list)
    return t_list


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
            # print("get to the end")
            break
        else:
            continue
    sort_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    r_list = []
    for k in range(number):
        # print(k)
        # print(sort_list[k])
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


def get_dict(type_txt):
    word_dict = {}
    i = 0
    while True:
        try:
            i = i + 1
            if r_sheet.cell_value(i, 1) == type_txt:
                w = r_sheet.cell_value(i, 4)
                if w in word_dict.keys():
                    word_dict[w] = word_dict[w] + 1
                else:
                    word_dict[w] = 1
        except IndexError:
            print("get to the end")
            break
        else:
            continue
    return word_dict


def dict_to_file(t_dict, path):
    f = open(path, 'w', encoding='utf-8')
    for i in t_dict:
        f.write(i + "," + str(t_dict[i]) + "\n")
    f.close()


def file_to_dict(path):
    f = open(path, 'r', encoding='utf-8')
    f_dict = {}
    line = f.readline()
    while line:
        line = line.replace("\n", "")
        f_dict[line.split(",")[0]] = line.split(",")[1]
        line = f.readline()
    f.close()
    print_dict(f_dict)
    return f_dict


"""next functions is the encapsulation of function above"""


def dict_file(type_txt, path):
    dict_to_file(get_dict(type_txt), path)


""" function below is use to manufacture & manipulate  matrix"""


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


def csv_export_co_matrix(r_list, c_list, csv_name):
    """
    根据两个数列中的关键词计算共现矩阵
    根据输入的列属性值和行属性值，以及csv表格中的数据
    export an csv table of the matrix
    :param csv_name: 要保存的矩阵名字
    :param r_list: r_list: row list, as one of the input list
    :param c_list: column list as one of the input list
    :return: 返回由上两个列表所计算出的共现矩阵
    """
    r = len(r_list)
    c = len(c_list)
    print("The size of matrix: " + str(r) + ", " + str(c))

    # 血的教训，要加newline=""
    data_csv = open(csv_name, 'w', newline="", encoding='gb18030')
    # data_csv.write(codecs.BOM_UTF8)
    csv_writer = csv.writer(data_csv, dialect='excel', delimiter=' ', quotechar=',')
    c_list.insert(0, "00")
    csv_writer.writerow(c_list)

    # 遍历每一个矩阵的单位，计算该单位对应两个word的共现次数
    for y in range(r):
        r_word = r_list[y]
        count_list = [r_word]
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
            count_list.append(co_occur_time)
        csv_writer.writerow(count_list)
        print(str(y))
    data_csv.close()


def excel_export_type_co_matrix(r_list, c_list, excel_name, col_num, type_txt):
    """
    根据两个数列中的关键词计算共现矩阵
    根据输入的列属性值和行属性值，以及excel表格中的数据
    export an excel table of the matrix
    :param type_txt: 要选择的特定类别
    :param col_num: 要选择的判定标准的列所在
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
                    # print(p_sheet.cell_value(int(poet_number), col_num))
                    if p_sheet.cell_value(int(poet_number), col_num) != type_txt:
                        continue
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


def excel_export_xushi(r_list, c_list, excel_name, xushi, type_or_not, col_num, type_txt):
    """
    根据两个数列中的关键词计算共现矩阵
    根据输入的列属性值和行属性值，以及excel表格中的数据
    export an excel table of the matrix
    :param type_txt: 要选择的特定类别
    :param col_num: 要选择的判定标准的列所在
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
                    # print(p_sheet.cell_value(int(poet_number), col_num))
                    # print(type_or_not)
                    if type_or_not:
                        if p_sheet.cell_value(int(poet_number), xushi) == "" or \
                                p_sheet.cell_value(int(poet_number), col_num) != type_txt:
                            continue
                    else:
                        if p_sheet.cell_value(int(poet_number), xushi) == "":
                            continue
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


"""next function is used to encapsulate the co-occur progress"""


def co_occur_whole(type1, type2, excel_name):
    r_list = get_list(type1)
    c_list = get_list(type2)
    excel_export_co_matrix(r_list, c_list, excel_name)


def co_occur_type_some(type1, type2, num1, num2, excel_name, col_num, type_txt):
    r_list = get_list_top(type1, num1)
    c_list = get_list_top(type2, num2)
    excel_export_type_co_matrix(r_list, c_list, excel_name, col_num, type_txt)


def co_occur_type_xushi(type1, type2, num1, num2, excel_name, xushi, type_or_not, col_num, type_txt):
    r_list = get_list_top(type1, num1)
    c_list = get_list_top(type2, num2)
    excel_export_xushi(r_list, c_list, excel_name, xushi, type_or_not, col_num, type_txt)


def co_occur_some(type1, type2, num1, num2, excel_name):
    r_list = get_list_top(type1, num1)
    c_list = get_list_top(type2, num2)
    excel_export_co_matrix(r_list, c_list, excel_name)


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
# stuff_list50 = get_list_top("物象词", 50)
# stuff_list100 = get_list_top("物象词", 100)
# location_list50 = get_list_top("地点词", 50)
# location_list100 = get_list_top("地点词", 100)
# status_list50 = get_list_top("状态词", 50)
# status_list100 = get_list_top("状态词", 100)
# time_list50 = get_list_top("时词", 50)
# time_list100 = get_list_top("时词", 100)
# people_list50 = get_list_top("人词", 50)
# people_list100 = get_list_top("人词", 100)
#
# excel_export_co_matrix(stuff_list50, stuff_list50, "output/物象物象50.xls")
# excel_export_co_matrix(location_list50, location_list50, "output/地点地点50.xls")
# excel_export_co_matrix(stuff_list50, location_list50, "output/地点物象50.xls")
# excel_export_co_matrix(time_list50, location_list50, "output/地点时间50.xls")
# excel_export_co_matrix(people_list50, location_list50, "output/地点人50.xls")
# excel_export_co_matrix(status_list50, location_list50, "output/地点状态50.xls")
#
# excel_export_co_matrix(stuff_list100, stuff_list100, "output/物象物象100.xls")
# excel_export_co_matrix(location_list100, location_list100, "output/地点地点100.xls")
# excel_export_co_matrix(stuff_list100, location_list100, "output/地点物象100.xls")
# excel_export_co_matrix(time_list100, location_list100, "output/地点时间100.xls")
# excel_export_co_matrix(people_list100, location_list100, "output/地点人100.xls")
# excel_export_co_matrix(status_list100, location_list100, "output/地点状态100.xls")


# stuff_list50 = get_list_top("物象词", 5)
# excel_export_co_matrix(stuff_list50, stuff_list50, "output/物象物象5.csv")


# stuff_list = get_list("物象词")
# location_list = get_list_top("地点词", 255)
# excel_export_co_matrix(stuff_list, location_list, "output_coverage/物象地点-总.xls")

# dict_to_file(get_dict("人词"), "guanzhong_word/人词count.txt")
# dict_to_file(get_dict("地点词"), "guanzhong_word/地点词count.txt")
# dict_to_file(get_dict("物象词"), "guanzhong_word/物象词count.txt")
# dict_to_file(get_dict("时词"), "guanzhong_word/时词count.txt")
# dict_to_file(get_dict("状态词"), "guanzhong_word/状态词count.txt")
# dict_to_file(get_dict("动词"), "guanzhong_word/动词count.txt")
# dict_to_file(get_dict("在哪写"), "guanzhong_word/在哪写count.txt")
# dict_to_file(get_dict("写的哪"), "guanzhong_word/写的哪count.txt")
# # file_to_dict("guanzhong_word/人词count.txt")

# work, output some files
# stuff_list50 = get_txt_top("guanzhong_word/物象词tfidf-sort.txt", 50)
# stuff_list100 = get_txt_top("guanzhong_word/物象词tfidf-sort.txt", 100)
# location_list50 = get_txt_top("guanzhong_word/地点词tfidf-sort.txt", 50)
# location_list100 = get_txt_top("guanzhong_word/地点词tfidf-sort.txt", 100)
# # status_list50 = get_list_top("状态词", 50)
# # status_list100 = get_list_top("状态词", 100)
# # time_list50 = get_list_top("时词", 50)
# # time_list100 = get_list_top("时词", 100)
# people_list50 = get_txt_top("guanzhong_word/人词tfidf-sort.txt", 50)
# people_list100 = get_txt_top("guanzhong_word/人词tfidf-sort.txt", 100)
# #
# excel_export_co_matrix(stuff_list50, stuff_list50, "output/tf物象物象50.xls")
# excel_export_co_matrix(location_list50, location_list50, "output/tf地点地点50.xls")
# excel_export_co_matrix(stuff_list50, location_list50, "output/tf地点物象50.xls")
# excel_export_co_matrix(people_list50, location_list50, "output/tf地点人50.xls")
#
# excel_export_co_matrix(stuff_list100, stuff_list100, "output/tf物象物象100.xls")
# excel_export_co_matrix(location_list100, location_list100, "output/tf地点地点100.xls")
# excel_export_co_matrix(stuff_list100, location_list100, "output/tf地点物象100.xls")
# excel_export_co_matrix(people_list100, location_list100, "output/tf地点人100.xls")
