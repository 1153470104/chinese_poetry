# -*- coding: utf-8 -*-
import xlrd
import xlwt
from xlutils.copy import copy
from co_occur import co_occur_some
from co_occur import co_occur_whole
from co_occur import dict_file


workbook = xlrd.open_workbook("../input/标注1104.xls")
r_sheet = workbook.sheet_by_index(0)


def wash():
    # write file
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    w_sheet = book.add_sheet("0")

    row0 = r_sheet.row_values(0)
    for j in range(5):
        w_sheet.write(0, j, row0[j])
    i = 0
    while True:
        try:
            i = i + 1
            row = r_sheet.row_values(i)
            for j in range(5):
                r = row[j]
                r = r.replace(" ", "")
                r = r.replace("，", "")
                r = r.replace("。", "")
                if j == 0 or j == 1:
                    w_sheet.write(i, j, r.split("\\\\")[1])
                else:
                    w_sheet.write(i, j, r)

            # 下面的循环是循环一条记录里的8中词类，写入不同sheet
        except IndexError:  # 用错误处理机制进行退出
            print("get to the end")
            break
        else:
            continue

    # 把book对应的内容存到 一个新文件里
    book.save("../input/qujiang_label.xls")


# wash()
# dict_file("物象", "../output/qujiang_cooccur/物象词frequency.txt")
dict_file("地点", "../output/qujiang_cooccur/merge地点词frequency.txt")

# co_occur_some("物象", "地点", 50, 50, "../output/qujiang_cooccur/merge物地50.xls")
# co_occur_some("物象", "物象", 50, 50, "../output/qujiang_cooccur/merge物物50.xls")
# co_occur_some("地点", "地点", 50, 50, "../output/qujiang_cooccur/merge地地50.xls")

# co_occur_some("物象", "地点", 100, 100, "../output/qujiang_cooccur/merge物地100.xls")
# co_occur_some("物象", "物象", 100, 100, "../output/qujiang_cooccur/merge物物100.xls")
# co_occur_some("地点", "地点", 100, 100, "../output/qujiang_cooccur/merge地地100.xls")
