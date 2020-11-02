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

"""
利用jiayan包进行唐诗分词
"""


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


# txt = "实录卷二十五咸丰元年。辛亥。春。正月。戊子朔。上诣奉先殿行礼。○诣堂子行礼。遣官祭太庙后殿.御太和殿受朝。中和乐设而不作。不读贺表。诣寿康宫前殿拈香。后殿皇贵太妃前行礼。诣大高殿寿皇殿行礼。诣弘仁寺拈香。谕内阁、朕寅承丕绪。抚驭万方。敬念列圣御极之初。蠲免积逋。覃敷闿泽。使人安乐利。户免追呼。共享昇平之福。诚以民为邦本。厚民生、正所以培元气也。当兹建元肇始之时。宜行体仁长人之政。自道光十五年、二十五年。两次钦奉皇考宣宗成皇帝恩旨。将二十年以前、各省民欠钱粮。尽予豁免后。自二十一年迄今又届十稔。民间续有积欠。允宜大沛恩纶。期与薄海群黎。同跻仁寿。所有各省节年民欠正耗钱粮、及因灾缓徵带徵银谷、并借给耔种口粮牛具、及漕项芦课学租杂税等项。即著各该督抚将军府尹等、将道光三十年以前、实欠在民者。详悉查明。按照该省所属之某州某县银谷若干。速行开单具奏。候朕以次降旨、全行豁免。并著先将此旨、刊刻誊黄。遍行晓谕。务使城市乡村。遐陬僻壤。咸喻朝廷德意。毋任官吏胥役等、延阁侵渔。致滋弊窦。庶吾民休养生息。庆洽绥丰。用示朕元春布德。以仰副皇考三十年子惠元元。申锡无疆至意。又谕、僧格林沁等奏、本日升殿鸣鞭之际。有人自西向东趋走。纠仪科道未经拦阻等语。著都察院查明参奏。"
# print(text_tokenize(txt))

