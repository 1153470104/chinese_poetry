# -*- coding: utf-8 -*-
import xlrd
import xlwt
from xlutils.copy import copy
from co_occur import co_occur_some, co_occur_type_some, co_occur_type_xushi
from co_occur import co_occur_whole
from co_occur import dict_file


workbook = xlrd.open_workbook("../input/标注检查1106.xls")
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
# dict_file("物象", "../output/qujiang_co2/物象词frequency.txt")
# dict_file("地点", "../output/qujiang_co2/merge地点词frequency.txt")
#
# co_occur_some("物象", "地点", 50, 50, "../output/qujiang_co2/merge物地50.xls")
# co_occur_some("物象", "物象", 50, 50, "../output/qujiang_co2/merge物物50.xls")
# co_occur_some("地点", "地点", 50, 50, "../output/qujiang_co2/merge地地50.xls")
#
# co_occur_some("物象", "地点", 100, 100, "../output/qujiang_co2/merge物地100.xls")
# co_occur_some("物象", "物象", 100, 100, "../output/qujiang_co2/merge物物100.xls")
# co_occur_some("地点", "地点", 100, 100, "../output/qujiang_co2/merge地地100.xls")
#
# co_occur_type_some("物象", "地点", 50, 50, "../output/qujiang_co2/初唐merge物地50.xls", 18, "初唐")
# co_occur_type_some("物象", "地点", 50, 50, "../output/qujiang_co2/盛唐merge物地50.xls", 18, "盛唐")
# co_occur_type_some("物象", "地点", 50, 50, "../output/qujiang_co2/中唐merge物地50.xls", 18, "中唐")
# co_occur_type_some("物象", "地点", 50, 50, "../output/qujiang_co2/晚唐merge物地50.xls", 18, "晚唐")
#
# co_occur_type_some("地点", "地点", 50, 50, "../output/qujiang_co2/初唐merge地地50.xls", 18, "初唐")
# co_occur_type_some("地点", "地点", 50, 50, "../output/qujiang_co2/盛唐merge地地50.xls", 18, "盛唐")
# co_occur_type_some("地点", "地点", 50, 50, "../output/qujiang_co2/中唐merge地地50.xls", 18, "中唐")
# co_occur_type_some("地点", "地点", 50, 50, "../output/qujiang_co2/晚唐merge地地50.xls", 18, "晚唐")
#
# co_occur_type_some("物象", "物象", 50, 50, "../output/qujiang_co2/初唐merge物物50.xls", 18, "初唐")
# co_occur_type_some("物象", "物象", 50, 50, "../output/qujiang_co2/盛唐merge物物50.xls", 18, "盛唐")
# co_occur_type_some("物象", "物象", 50, 50, "../output/qujiang_co2/中唐merge物物50.xls", 18, "中唐")
# co_occur_type_some("物象", "物象", 50, 50, "../output/qujiang_co2/晚唐merge物物50.xls", 18, "晚唐")
#
# co_occur_type_some("物象", "地点", 100, 100, "../output/qujiang_co2/初唐merge物地100.xls", 18, "初唐")
# co_occur_type_some("物象", "地点", 100, 100, "../output/qujiang_co2/盛唐merge物地100.xls", 18, "盛唐")
# co_occur_type_some("物象", "地点", 100, 100, "../output/qujiang_co2/中唐merge物地100.xls", 18, "中唐")
# co_occur_type_some("物象", "地点", 100, 100, "../output/qujiang_co2/晚唐merge物地100.xls", 18, "晚唐")
#
# co_occur_type_some("地点", "地点", 100, 100, "../output/qujiang_co2/初唐merge地地100.xls", 18, "初唐")
# co_occur_type_some("地点", "地点", 100, 100, "../output/qujiang_co2/盛唐merge地地100.xls", 18, "盛唐")
# co_occur_type_some("地点", "地点", 100, 100, "../output/qujiang_co2/中唐merge地地100.xls", 18, "中唐")
# co_occur_type_some("地点", "地点", 100, 100, "../output/qujiang_co2/晚唐merge地地100.xls", 18, "晚唐")
#
# co_occur_type_some("物象", "物象", 100, 100, "../output/qujiang_co2/初唐merge物物100.xls", 18, "初唐")
# co_occur_type_some("物象", "物象", 100, 100, "../output/qujiang_co2/盛唐merge物物100.xls", 18, "盛唐")
# co_occur_type_some("物象", "物象", 100, 100, "../output/qujiang_co2/中唐merge物物100.xls", 18, "中唐")
# co_occur_type_some("物象", "物象", 100, 100, "../output/qujiang_co2/晚唐merge物物100.xls", 18, "晚唐")
#
# co_occur_type_some("物象", "地点", 50, 50, "../output/qujiang_co2/春merge物地50.xls", 4, "春")
# co_occur_type_some("物象", "地点", 50, 50, "../output/qujiang_co2/夏merge物地50.xls", 4, "夏")
# co_occur_type_some("物象", "地点", 50, 50, "../output/qujiang_co2/秋merge物地50.xls", 4, "秋")
# co_occur_type_some("物象", "地点", 50, 50, "../output/qujiang_co2/冬merge物地50.xls", 4, "冬")
#
# co_occur_type_some("地点", "地点", 50, 50, "../output/qujiang_co2/春merge地地50.xls", 4, "春")
# co_occur_type_some("地点", "地点", 50, 50, "../output/qujiang_co2/夏merge地地50.xls", 4, "夏")
# co_occur_type_some("地点", "地点", 50, 50, "../output/qujiang_co2/秋merge地地50.xls", 4, "秋")
# co_occur_type_some("地点", "地点", 50, 50, "../output/qujiang_co2/冬merge地地50.xls", 4, "冬")
#
# co_occur_type_some("物象", "物象", 50, 50, "../output/qujiang_co2/春merge物物50.xls", 4, "春")
# co_occur_type_some("物象", "物象", 50, 50, "../output/qujiang_co2/夏merge物物50.xls", 4, "夏")
# co_occur_type_some("物象", "物象", 50, 50, "../output/qujiang_co2/秋merge物物50.xls", 4, "秋")
# co_occur_type_some("物象", "物象", 50, 50, "../output/qujiang_co2/冬merge物物50.xls", 4, "冬")

# co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/实写merge物地50.xls", 14, False, 1, "初唐")
# co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/实写merge地地50.xls", 14, False, 1, "初唐")
# co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/实写merge物物50.xls", 14, False, 1, "初唐")
# co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/虚写merge物地50.xls", 15, False, 1, "初唐")
# co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/虚写merge地地50.xls", 15, False, 1, "初唐")
# co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/虚写merge物物50.xls", 15, False, 1, "初唐")

# co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/实写初唐merge物地50.xls", 14, True, 18, "初唐")
# co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/实写盛唐merge物地50.xls", 14, True, 18, "盛唐")
# co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/实写中唐merge物地50.xls", 14, True, 18, "中唐")
# co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/实写晚唐merge物地50.xls", 14, True, 18, "晚唐")
#
co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/实写初唐merge地地50.xls", 14, True, 18, "初唐")
co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/实写盛唐merge地地50.xls", 14, True, 18, "盛唐")
co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/实写中唐merge地地50.xls", 14, True, 18, "中唐")
co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/实写晚唐merge地地50.xls", 14, True, 18, "晚唐")

co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/实写初唐merge物物50.xls", 14, True, 18, "初唐")
co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/实写盛唐merge物物50.xls", 14, True, 18, "盛唐")
co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/实写中唐merge物物50.xls", 14, True, 18, "中唐")
co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/实写晚唐merge物物50.xls", 14, True, 18, "晚唐")

co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/实写春merge物地50.xls", 14, True, 4, "春")
co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/实写夏merge物地50.xls", 14, True, 4, "夏")
co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/实写秋merge物地50.xls", 14, True, 4, "秋")
co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/实写冬merge物地50.xls", 14, True, 4, "冬")

co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/实写春merge地地50.xls", 14, True, 4, "春")
co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/实写夏merge地地50.xls", 14, True, 4, "夏")
co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/实写秋merge地地50.xls", 14, True, 4, "秋")
co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/实写冬merge地地50.xls", 14, True, 4, "冬")

co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/实写春merge物物50.xls", 14, True, 4, "春")
co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/实写夏merge物物50.xls", 14, True, 4, "夏")
co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/实写秋merge物物50.xls", 14, True, 4, "秋")
co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/实写冬merge物物50.xls", 14, True, 4, "冬")


co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/虚写初唐merge物地50.xls", 15, True, 18, "初唐")
co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/虚写盛唐merge物地50.xls", 15, True, 18, "盛唐")
co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/虚写中唐merge物地50.xls", 15, True, 18, "中唐")
co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/虚写晚唐merge物地50.xls", 15, True, 18, "晚唐")

co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/虚写初唐merge地地50.xls", 15, True, 18, "初唐")
co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/虚写盛唐merge地地50.xls", 15, True, 18, "盛唐")
co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/虚写中唐merge地地50.xls", 15, True, 18, "中唐")
co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/虚写晚唐merge地地50.xls", 15, True, 18, "晚唐")

co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/虚写初唐merge物物50.xls", 15, True, 18, "初唐")
co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/虚写盛唐merge物物50.xls", 15, True, 18, "盛唐")
co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/虚写中唐merge物物50.xls", 15, True, 18, "中唐")
co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/虚写晚唐merge物物50.xls", 15, True, 18, "晚唐")

co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/虚写春merge物地50.xls", 15, True, 4, "春")
co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/虚写夏merge物地50.xls", 15, True, 4, "夏")
co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/虚写秋merge物地50.xls", 15, True, 4, "秋")
co_occur_type_xushi("物象", "地点", 50, 50, "../output/qujiang_co2/虚写冬merge物地50.xls", 15, True, 4, "冬")

co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/虚写春merge地地50.xls", 15, True, 4, "春")
co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/虚写夏merge地地50.xls", 15, True, 4, "夏")
co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/虚写秋merge地地50.xls", 15, True, 4, "秋")
co_occur_type_xushi("地点", "地点", 50, 50, "../output/qujiang_co2/虚写冬merge地地50.xls", 15, True, 4, "冬")

co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/虚写春merge物物50.xls", 15, True, 4, "春")
co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/虚写夏merge物物50.xls", 15, True, 4, "夏")
co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/虚写秋merge物物50.xls", 15, True, 4, "秋")
co_occur_type_xushi("物象", "物象", 50, 50, "../output/qujiang_co2/虚写冬merge物物50.xls", 15, True, 4, "冬")
