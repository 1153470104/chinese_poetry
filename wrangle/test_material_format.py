"""
分词预处理 / 分词几个指标的计算
"""

import xlrd
import re
from co_occur import print_list


def make_material():
    workbook = xlrd.open_workbook("../input/qj分词汇总.xls")
    sheet = workbook.sheet_by_index(1)
    poet_data = sheet.col_values(19)[1:]
    # print_list(poet_data)

    wf = open("../input/qujiang_test.txt", 'w', encoding='utf-8')
    for l in poet_data:
        wf.write(l + '\n')
    wf.close()


make_material()
f = open("../input/qujiang_test.txt", 'r', encoding='utf-8')
poet_list = []
line = f.readline()
while line:
    d = re.sub(u"（.*?）", "", line)
    d = re.sub(u"\\(.*?\\)", "", d)
    poet_list.append(d.replace("\n", ''))
    line = f.readline()


def get_test_list():
    test_list = []
    for l in poet_list:
        dd = l.replace(' ', '')
        test_list.append(dd)
    return test_list


def list_participle(output_list):
    correct_list = []
    for i in output_list:
        ii = i.replace("。", ' ')
        ii = ii.replace("，", ' ')
        i_split = ii.split(' ')
        re_split = []
        for x in i_split:
            if x != '':
                re_split.append(x)
        correct_list.append(re_split)
    return correct_list


def correctness(output_list):
    """
    print accuracy & recall & F1
    :return: nothing
    """
    correct_list = list_participle(poet_list)
    result_list = list_participle(output_list)
    real_word = 0
    output_word = 0
    correct_word = 0
    length = len(correct_list)
    for i in range(length):
        r_list = correct_list[i]
        o_list = result_list[i]
        real_word = real_word + len(r_list)
        output_word = output_word + len(o_list)
        r_dict = {}
        o_dict = {}
        i = 0
        j = 0
        for w in r_list:
            r_dict[i] = w
            i = i + len(w)
        for v in o_list:
            o_dict[j] = v
            j = j + len(v)
        rm = r_dict.keys()
        om = o_dict.keys()
        for ii in rm:
            if ii in om and r_dict[ii] == o_dict[ii]:
                correct_word = correct_word + 1

    print(correct_word)
    print(real_word)
    print(output_word)
    print("The recall rate: " + str(correct_word / real_word))
    print("The accuracy rate: " + str(correct_word / output_word))
    print("The F1 value: " + str(2 / (output_word / correct_word + real_word / correct_word)))


# print_list(list_participle(poet_list))
# correctness(poet_list)
