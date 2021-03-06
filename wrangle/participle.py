"""
利用jiayan包进行唐诗分词
各类包调用分词
"""
# -*- coding: utf-8 -*-
import re
from jiayan import load_lm
from jiayan import CharHMMTokenizer
import xlrd
import xlwt
import pandas as pd
import os
from jiayan import WordNgramTokenizer
import kenlm
import jieba
import pkuseg


# test_text = "往时中补右，扈跸上元初。反气凌行在，妖星下直庐。六龙瞻汉阙，万骑略姚墟。" \
#             "玄朔回天步，神都忆帝车。一戎才汗马，百姓免为鱼。通籍蟠螭印，差肩列凤舆。" \
#             "事殊迎代邸，喜异赏朱虚。寇盗方归顺，乾坤欲晏如。不才同补衮，奉诏许牵裾。" \
#             "鸳鹭叨云阁，麒麟滞玉除。文园多病后，中散旧交疏。飘泊哀相见，平生意有馀。" \
#             "风烟巫峡远，台榭楚宫虚。触目非论故，新文尚起予。清秋凋碧柳，别浦落红蕖。" \
#             "消息多旗帜，经过叹里闾。战连唇齿国，军急羽毛书。幕府筹频问，山家药正锄。" \
#             "台星入朝谒，使节有吹嘘。西蜀灾长弭，南翁愤始摅。对扬抏士卒，干没费仓储。" \
#             "势藉兵须用，功无礼忽诸。御鞍金騕褭，宫砚玉蟾蜍。拜舞银钩落，恩波锦帕舒。" \
#             "此行非不济，良友昔相于。去旆依颜色，沿流想疾徐。沈绵疲井臼，倚薄似樵渔。" \
#             "乞米烦佳客，钞诗听小胥。杜陵斜晚照，潏水带寒淤。莫话清溪发，萧萧白映梳。 "
# text = '是故内圣外王之道，暗而不明，郁而不发，天下之人各为其所欲焉以自为方。'

# # 打开全唐诗的excel表格
# workbook = xlrd.open_workbook("../input/全唐诗数据库0805.xlsx")
# sheet = workbook.sheet_by_index(0)
# title_data = sheet.col_values(2)
# poet_data = sheet.col_values(4)
# # print_list(poet_data)
#
# # 把首行去掉
# poet_data = poet_data[1:]
# participle = []
# i = 1
# for d in poet_data:
#     d = title_data[i] + d                     # 和诗的标题加在一起
#     d = re.sub(u"（.*?）", "", d)             # 去掉括号内容
#     d = re.sub(u"<.*?>", "", d)               # 去掉< emm >
#     p = text_tokenize(d)                      # 调包分词
#     print(str(i) + " " + p)
#     participle.append(p)                      # 放到那个list里面
#     i = i+1
#
# # 下面就是把这列表写到excel里面
# book = xlwt.Workbook(encoding="utf-8", style_compression=0)
# sheet = book.add_sheet('jiayan', cell_overwrite_ok=True)
# count = 0
# for data in participle:
#     sheet.write(count, 0, count)
#     sheet.write(count, 1, data)
#     count = count+1
#
# book.save("全唐诗jiayan.xls")


def print_list(list_data):
    for dd in list_data:
        print(dd)


def text_tokenize(text_data):
    # lm = load_lm('../jiayan.klm')
    lm = load_lm('../tang.klm')
    tokenizer = CharHMMTokenizer(lm)
    result = ''
    t_list = list(tokenizer.tokenize(text_data))
    for t in t_list:
        result = result + t + " "
    result = result[:-1]
    return result


def jiayan_tokenize(input_list):
    participle = []
    for d in input_list:
        # print(d)
        p = text_tokenize(d)                      # 调包分词
        participle.append(p)                      # 放到那个list里面
    return participle


def jieba_tokenize(input_list):
    # jieba.enable_paddle()
    jieba.load_userdict("../input/Tang_poet_dict.txt")
    participle = []
    for d in input_list:
        # print(d)
        p = jieba.cut(d)
        participle.append(' '.join(list(p)))
    return participle


def pkuseg_tokenize(input_list):
    seg = pkuseg.pkuseg()
    participle = []
    for d in input_list:
        p = seg.cut(d)
        # print(p)
        participle.append(" ".join(p))
    return participle


# txt = ["寒驚薊門葉，秋發小山枝。松陰背日轉，竹影避風移。提壺菊花岸，高興芙蓉池。欲知涼氣早，巢空燕不窺。"]
# # print(text_tokenize(txt))
# print(jiayan_tokenize(txt))
# print(jieba_tokenize(txt))

