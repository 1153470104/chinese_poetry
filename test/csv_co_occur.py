"""
全共现的脚本，带计算覆盖率
"""
# -*- coding: utf-8 -*-
from wrangle.co_occur import csv_export_co_matrix
from wrangle.co_occur import get_list


stuff_full_list = get_list("物象词")
location_list = get_list("地点词")
stuff_list = [x for x in stuff_full_list if x not in location_list]
status_list = get_list("状态词")
people_list = get_list("人词")
time_list = get_list("时词")

# 物象的问题，有字符无法读写。。。
# csv_export_co_matrix(stuff_list, location_list, "../output/coverage/物象地点.csv")
csv_export_co_matrix(stuff_list, stuff_list, "../output/coverage/物象物象.csv")
# csv_export_co_matrix(location_list, stuff_list, "../output/coverage/物象地点.csv")  # reverse

# csv_export_co_matrix(location_list, location_list, "../output/coverage/地点地点.csv")
# csv_export_co_matrix(people_list, location_list, "../output/coverage/地点人词.csv")
# csv_export_co_matrix(status_list, location_list, "../output/coverage/地点状态.csv")
# csv_export_co_matrix(time_list, location_list, "../output/coverage/地点时词.csv")
