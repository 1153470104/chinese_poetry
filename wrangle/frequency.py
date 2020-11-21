"""
用于统计词频
函数：根据需要的类型选择文本 / 统计频率， 以及一些辅助函数
"""

import xlrd


workbook = xlrd.open_workbook("../input/qj分词汇总.xls")
r_sheet = workbook.sheet_by_index(1)


def get_all():
    txt = []
    i = 0
    while True:
        try:
            i = i + 1
            line = r_sheet.row_values(i)
            txt.append(line[2] + " " + line[19])
        except IndexError:
            print("get to the end")
            break
        else:
            continue
    return txt


def get_list_txt(col_num, type_txt, xushi_or_not, xushi_num, only_xushi):
    row_list = []
    if only_xushi:
        dtm_col = r_sheet.col_values(xushi_num)

        i = 0
        while True:
            try:
                i = i + 1
                if dtm_col[i] != "":
                    row_list.append(i)
            except IndexError:
                print("get to the end")
                break
            else:
                continue
        return get_type_txt(row_list)

    if not xushi_or_not:
        dtm_col = r_sheet.col_values(col_num)

        i = 0
        while True:
            try:
                i = i + 1
                if type_txt in dtm_col[i]:
                    row_list.append(i)
            except IndexError:
                print("get to the end")
                break
            else:
                continue
    else:
        dtm_col = r_sheet.col_values(col_num)
        xushi_col = r_sheet.col_values(xushi_num)
        i = 0
        while True:
            try:
                i = i + 1
                if xushi_col[i] != "" and type_txt in dtm_col[i]:
                    row_list.append(i)
            except IndexError:
                print("get to the end")
                break
            else:
                continue

    return get_type_txt(row_list)


def get_type_txt(row_list):
    txt_list = []
    i = 0
    while True:
        try:
            i = i + 1
            line = r_sheet.row_values(i)
            if i in row_list:
                txt_list.append(line[2] + " " + line[19])
        except IndexError:
            print("get to the end")
            break
        else:
            continue
    return txt_list


def frequency(txt_list):
    txt = ""
    for t in txt_list:
        txt = txt + str(t)
    txt = txt.replace("，", " ")
    txt = txt.replace(",", " ")
    txt = txt.replace("。", " ")
    w_list = txt.split(" ")
    w_dict = {}
    for w in w_list:
        if w == "":
            continue
        if w in w_dict.keys():
            w_dict[w] = w_dict[w] + 1
        else:
            w_dict[w] = 1
    return w_dict


def dict_to_file(w_dict, path):
    f = open(path, 'w', encoding="utf-8")
    items = sorted(w_dict.items(), key=lambda item: item[1], reverse=True)
    for i in items:
        f.write(i[0] + " " + str(i[1]) + "\n")
    f.close()


def get_frequency(col_num, type_txt, xushi_or_not, xushi_num, only_xushi, path):
    dict_to_file(
        frequency(
            get_list_txt(col_num, type_txt, xushi_or_not, xushi_num, only_xushi)), path)


def combine_fre(path1, path2, path3):
    f1 = open(path1, 'r', encoding='utf-8')
    f2 = open(path2, 'r', encoding='utf-8')
    w_dict = {}
    line1 = f1.readline()
    while line1:
        line1 = line1.replace("\n", "")
        fre = line1.split(" ")
        w_dict[fre[0]] = int(fre[1])
        line1 = f1.readline()
    line2 = f2.readline()
    while line2:
        line2 = line2.replace("\n", "")
        fre = line2.split(" ")
        if fre[0] not in w_dict.keys():
            w_dict[fre[0]] = int(fre[1])
        else:
            w_dict[fre[0]] = w_dict[fre[0]] + int(fre[1])
        line2 = f2.readline()

    f1.close()
    f2.close()
    dict_to_file(w_dict, path3)
