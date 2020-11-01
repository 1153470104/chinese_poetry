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


poem_list = get_data()
# print_list(poem_list)
# print_list(get_location("qj"))
# print_list(get_location("map"))
print_list(get_location("big"))
