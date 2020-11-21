"""
计算曲江词频
去停用词
"""
from frequency import get_fre
from frequency import frequency
from frequency import dict_to_file
from frequency import get_all
from frequency import combine_fre

# dict_to_file(frequency(get_list_txt(0, "", False, 14, True)), "../output/qj_frequency/实写.txt")
# dict_to_file(frequency(get_all()), "../output/qj_frequency/全部.txt")
# get_frequency(0, "", False, 15, True, "../output/qj_frequency/虚写.txt")

# get_frequency(4, "春", False, 15, False, "../output/qj_frequency/春.txt")
# get_frequency(4, "夏", False, 15, False, "../output/qj_frequency/夏.txt")
# get_frequency(4, "秋", False, 15, False, "../output/qj_frequency/秋.txt")
# get_frequency(4, "冬", False, 15, False, "../output/qj_frequency/冬.txt")

# get_fre("../output/qj_frequency/全部2.txt")
# get_fre(18, "初唐", "../output/qj_frequency/初唐2.txt")
# get_frequency(18, "初唐", False, 15, False, "../output/qj_frequency/初唐.txt")
# get_frequency(18, "盛唐", False, 15, False, "../output/qj_frequency/盛唐.txt")
# get_frequency(18, "中唐", False, 15, False, "../output/qj_frequency/中唐.txt")
# get_frequency(18, "晚唐", False, 15, False, "../output/qj_frequency/晚唐.txt")

# 实写
# get_fre(4, "春", 14, "true", "../output/qj_frequency/实写春2.txt")
# get_frequency(4, "春", True, 14, False, "../output/qj_frequency/实写春.txt")
# get_frequency(4, "夏", True, 14, False, "../output/qj_frequency/实写夏.txt")
# get_frequency(4, "秋", True, 14, False, "../output/qj_frequency/实写秋.txt")
# get_frequency(4, "冬", True, 14, False, "../output/qj_frequency/实写冬.txt")
#
# get_frequency(18, "初唐", True, 14, False, "../output/qj_frequency/实写初唐.txt")
# get_frequency(18, "盛唐", True, 14, False, "../output/qj_frequency/实写盛唐.txt")
# get_frequency(18, "中唐", True, 14, False, "../output/qj_frequency/实写中唐.txt")
# get_frequency(18, "晚唐", True, 14, False, "../output/qj_frequency/实写晚唐.txt")
#
# # 虚写
# get_frequency(4, "春", True, 15, False, "../output/qj_frequency/虚写春.txt")
# get_frequency(4, "夏", True, 15, False, "../output/qj_frequency/虚写夏.txt")
# get_frequency(4, "秋", True, 15, False, "../output/qj_frequency/虚写秋.txt")
# get_frequency(4, "冬", True, 15, False, "../output/qj_frequency/虚写冬.txt")
#
# get_frequency(18, "初唐", True, 15, False, "../output/qj_frequency/虚写初唐.txt")
# get_frequency(18, "盛唐", True, 15, False, "../output/qj_frequency/虚写盛唐.txt")
# get_frequency(18, "中唐", True, 15, False, "../output/qj_frequency/虚写中唐.txt")
# get_frequency(18, "晚唐", True, 15, False, "../output/qj_frequency/虚写晚唐.txt")


# get_frequency(14, "慈恩", False, 15, False, "../output/qj_frequency/实写慈恩寺.txt")
# get_frequency(14, "曲", False, 15, False, "../output/qj_frequency/实写曲江.txt")
# get_frequency(14, "芙蓉", False, 15, False, "../output/qj_frequency/实写芙蓉苑.txt")
# get_frequency(14, "杏", False, 15, False, "../output/qj_frequency/实写杏园.txt")
# get_frequency(14, "乐游", False, 15, False, "../output/qj_frequency/实写乐游原.txt")
# get_frequency(14, "宜春", False, 15, False, "../output/qj_frequency/实写宜春苑.txt")
#
#
# get_fre(15, "慈恩", 15, "true", "../output/qj_frequency/虚写慈恩寺2.txt")
# get_frequency(15, "慈恩", False, 15, False, "../output/qj_frequency/虚写慈恩寺.txt")
# get_frequency(15, "曲", False, 15, False, "../output/qj_frequency/虚写曲江.txt")
# get_frequency(15, "芙蓉", False, 15, False, "../output/qj_frequency/虚写芙蓉苑.txt")
# get_frequency(15, "杏", False, 15, False, "../output/qj_frequency/虚写杏园.txt")
# get_frequency(15, "乐游", False, 15, False, "../output/qj_frequency/虚写乐游原.txt")
# get_frequency(15, "宜春", False, 15, False, "../output/qj_frequency/虚写宜春苑.txt")

location = ["慈恩", "曲江", "芙蓉", "杏园", "乐游", "宜春"]
era = ["初唐", "盛唐", "中唐", "晚唐"]
seasons = ["春", "夏", "秋", "冬"]
# for loc in location:
#     for period in era:
#         for season in seasons:
#             get_fre(4, season, 18, period, 14, loc, "../output/qj_frequency/1121/" + "实写" + loc + period + season + ".txt")
#             get_fre(4, season, 18, period, 15, loc, "../output/qj_frequency/1121/" + "虚写" + loc + period + season + ".txt")

path = "../output/qj_frequency/1121/"
for loc in location:
    for period in era:
        for season in seasons:
            combine_fre(path+"实写"+loc+period+season+".txt", path+"虚写"+loc+period+season+".txt", path+loc+period+season+".txt")

# combine_fre("../output/qj_frequency/实写慈恩寺.txt", "../output/qj_frequency/虚写慈恩寺.txt", "../output/qj_frequency/慈恩寺.txt")
# combine_fre("../output/qj_frequency/实写曲江.txt", "../output/qj_frequency/虚写曲江.txt", "../output/qj_frequency/曲江.txt")
# combine_fre("../output/qj_frequency/实写芙蓉苑.txt", "../output/qj_frequency/虚写芙蓉苑.txt", "../output/qj_frequency/芙蓉苑.txt")
# combine_fre("../output/qj_frequency/实写杏园.txt", "../output/qj_frequency/虚写杏园.txt", "../output/qj_frequency/杏园.txt")
# combine_fre("../output/qj_frequency/实写乐游原.txt", "../output/qj_frequency/虚写乐游原.txt", "../output/qj_frequency/乐游原.txt")
# combine_fre("../output/qj_frequency/实写宜春苑.txt", "../output/qj_frequency/虚写宜春苑.txt", "../output/qj_frequency/宜春苑.txt")
