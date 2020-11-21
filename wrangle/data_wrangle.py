"""
提取 excel 文件的不同列，分别统计存储到新文件的不同表的函数
"""

# -*- coding: utf-8 -*-
import xlrd
import xlwt
from xlutils.copy import copy


# 打印数列
def print_list(list_data):
    for d in list_data:
        print(d)


# 打印字典
def print_dict(dict_data):
    for d in dict_data:
        print(d + ": " + str(dict_data[d]))


# 转换字符串到
def list_txt(txt):
    space_list = ['.', ',', ';', '。', '，', '；', '!', '_']
    for s in space_list:
        txt = txt.replace(s, ' ')
    # print_list(txt.split())
    return txt.split()


# 转换列表到字典
def dict_list(s_list):
    s_dict = {}
    for s in s_list:
        if s in s_dict:
            s_dict[s] = s_dict[s] + 1
        else:
            s_dict[s] = 1
    print_dict(s_dict)
    return s_dict


# read file
workbook = xlrd.open_workbook("test.xlsx")
r_sheet = workbook.sheet_by_index(0)
name_list = r_sheet.row_values(0)

# write file
# book = xlwt.Workbook(encoding="utf-8", style_compression=0)
book = copy(workbook) # 调用xlutils 里的copy函数转换原有只读workbook为可读文件
sheet_1 = book.add_sheet("ID-" + name_list[3], cell_overwrite_ok=True)
sheet_2 = book.add_sheet("ID-" + name_list[4], cell_overwrite_ok=True)
sheet_3 = book.add_sheet("ID-" + name_list[5], cell_overwrite_ok=True)
sheet_4 = book.add_sheet("ID-" + name_list[6], cell_overwrite_ok=True)
sheet_5 = book.add_sheet("ID-" + name_list[7], cell_overwrite_ok=True)
sheet_6 = book.add_sheet("ID-" + name_list[8], cell_overwrite_ok=True)
sheet_7 = book.add_sheet("ID-" + name_list[9], cell_overwrite_ok=True)
sheet_8 = book.add_sheet("ID-" + name_list[10], cell_overwrite_ok=True)

# 用count数组来记录现有行号（找不到别的方法了。。。）
count = [1, 1, 1, 1, 1, 1, 1, 1]

# 把需要调整的sheet放到一个list中
sheet_list = [sheet_1, sheet_2, sheet_3, sheet_4,
              sheet_5, sheet_6, sheet_7, sheet_8]

# 循环写入每个文件的
k = 0
for s in sheet_list:
    s.write(0, 0, "诗歌ID")
    s.write(0, 1, name_list[3 + k])
    s.write(0, 2, "频次")
    k = k + 1

# 循环读取一行行文本处理
i = 0
while True:
    try:
        i = i + 1
        p_data = r_sheet.row_values(i)
        # 下面的循环是循环一条记录里的8中词类，写入不同sheet
        for j in range(8):
            # 调用两个方法，得到单个记录对应的字典。
            p_dict = dict_list(list_txt(p_data[3 + j]))
            for p in p_dict:
                sheet_list[j].write(count[j], 0, p_data[0])
                sheet_list[j].write(count[j], 1, p)
                sheet_list[j].write(count[j], 2, p_dict[p])
                count[j] = count[j] + 1
    except IndexError:  # 用错误处理机制进行退出
        print("get to the end")
        break
    else:
        continue

# 把book对应的内容存到 一个新文件里
book.save("result.xls")
