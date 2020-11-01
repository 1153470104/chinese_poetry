import xlrd
import re
from co_occur import print_list
from co_occur import print_dict
from deduplication_excel import table_to_list


def get_data():
    workbook = xlrd.open_workbook("../input/qujiang_重tag_合并版1021.xls")
    r_sheet = workbook.sheet_by_index(1)
    title_list = r_sheet.col_values(2)[1:]
    qj_judge_list = r_sheet.col_values(6)[1:]
    location_list = r_sheet.col_values(14)[1:]
    unreal_location_list = r_sheet.col_values(15)[1:]
    content_list = r_sheet.col_values(19)[1:]
    length = len(title_list)
    poem_list = []
    for i in range(length):
        location = location_list[i] + unreal_location_list[i]
        if qj_judge_list[i] == 1:
            line = title_list[i] + ' ' + content_list[i]
            d = re.sub(u"（.*?）", "", line)
            d = re.sub(u"\\(.*?\\)", "", d)
            d = d.replace("。", ' ')
            d = d.replace(".", ' ')
            d = d.replace("·", ' ')
            d = d.replace("，", ' ')
            d = d.replace(",", ' ')
            l = d.split(" ")
            l.insert(0, location)
            poem_list.append(l)
    return poem_list


def get_location(target):
    if target == 'qj':
        return table_to_list("../input/location_mapping.xls", 0)
    elif target == "map":
        return table_to_list("../input/location_mapping.xls", 1)
    elif target == "big":
        return table_to_list("../input/location_mapping.xls", 2)


def list_flat(input_list):
    result = []
    for l in input_list:
        for ll in l:
            result.append(ll)
    return result


poetry_list = get_data()
# print_list(poem_list)
qj_list = get_location("qj")
map_list = get_location("map")
big_list = get_location("big")

qj_flat = list_flat(qj_list)
map_flat = list_flat(map_list)
big_flat = list_flat(big_list)

rest_list = []
for i in big_flat:
    if i not in qj_flat and i not in map_flat:
        rest_list.append(i)


def word_match(ss, loc, pos):
    loc_len = len(loc)
    str_len = len(ss)
    if pos + loc_len > str_len:
        return False
    j = 0
    for l in loc:
        if ss[pos + j] != l:
            return False
        j = j+1
    return True


def simple_get_surfix(ss, loc):
    loc_len = len(loc)
    str_len = len(ss)
    if loc in ss:
        for j in range(str_len):
            if word_match(ss, loc, j) and j + loc_len < str_len:
                return ss[j+loc_len]
    return ""


def list_get_surfix(ss, loc_list):
    if ss == "":
        return ""
    for l in loc_list:
        surfix = simple_get_surfix(ss, l)
        if surfix != "":
            return surfix
    return ""


# def dict_list_to_matrix:

dict_list = []
for location in qj_list:
    surfix_dict = {}
    for line in poetry_list:
        if location[0] not in line[0]:
            continue
        # print(location[0] + " " + line[0])
        ii = 0
        for sentence in line:
            ii = ii+1
            if ii == 1:
                continue
            # print(sentence)
            surfix = list_get_surfix(sentence, location[1:])
            # print(surfix)
            if surfix != "":
                if surfix not in surfix_dict.keys():
                    surfix_dict[surfix] = 1
                else:
                    surfix_dict[surfix] = surfix_dict[surfix] + 1
    print(location[1], end="")
    print(surfix_dict)
    dict_list.append(surfix_dict)

dict_list = []
for location in rest_list:
    surfix_dict = {}
    for line in poetry_list:
        for sentence in line:
            surfix = list_get_surfix(sentence, location)
            # print(surfix)
            if surfix != "":
                if surfix not in surfix_dict.keys():
                    surfix_dict[surfix] = 1
                else:
                    surfix_dict[surfix] = surfix_dict[surfix] + 1
    print(location[0], end="")
    print(surfix_dict)
    dict_list.append(surfix_dict)

dict_list = []
for location in rest_list:
    surfix_dict = {}
    for line in poetry_list:
        for sentence in line:
            surfix = simple_get_surfix(sentence, location)
            # print(surfix)
            if surfix != "":
                if surfix not in surfix_dict.keys():
                    surfix_dict[surfix] = 1
                else:
                    surfix_dict[surfix] = surfix_dict[surfix] + 1
    print(location, end="")
    print(surfix_dict)
    dict_list.append(surfix_dict)

# print(simple_get_surfix("曲江春上有", "曲江"))
# print(simple_get_surfix("春上有曲江", "曲江"))
# print(simple_get_surfix("春上曲江有", "曲江"))
# print(simple_get_surfix("曲水曲江有", "曲江"))
# print(simple_get_surfix("曲水曲江有", "曲水曲"))
# print(list_get_surfix("曲江春上有", ["曲子", "曲江", "春"]))
