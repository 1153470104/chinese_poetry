from frequency import get_list_txt
from frequency import frequency
from frequency import dict_to_file
from frequency import get_all
from frequency import get_frequency

# dict_to_file(frequency(get_list_txt(0, "", False, 14, True)), "../output/qj_frequency/实写.txt")
# dict_to_file(frequency(get_all()), "../output/qj_frequency/全部.txt")
# get_frequency(0, "", False, 15, True, "../output/qj_frequency/虚写.txt")

get_frequency(4, "春", False, 15, False, "../output/qj_frequency/春.txt")
get_frequency(4, "夏", False, 15, False, "../output/qj_frequency/夏.txt")
get_frequency(4, "秋", False, 15, False, "../output/qj_frequency/秋.txt")
get_frequency(4, "冬", False, 15, False, "../output/qj_frequency/冬.txt")

get_frequency(18, "初唐", False, 15, False, "../output/qj_frequency/初唐.txt")
get_frequency(18, "盛唐", False, 15, False, "../output/qj_frequency/盛唐.txt")
get_frequency(18, "中唐", False, 15, False, "../output/qj_frequency/中唐.txt")
get_frequency(18, "晚唐", False, 15, False, "../output/qj_frequency/晚唐.txt")

# 实写
get_frequency(4, "春", True, 14, False, "../output/qj_frequency/实写春.txt")
get_frequency(4, "夏", True, 14, False, "../output/qj_frequency/实写夏.txt")
get_frequency(4, "秋", True, 14, False, "../output/qj_frequency/实写秋.txt")
get_frequency(4, "冬", True, 14, False, "../output/qj_frequency/实写冬.txt")

get_frequency(18, "初唐", True, 14, False, "../output/qj_frequency/实写初唐.txt")
get_frequency(18, "盛唐", True, 14, False, "../output/qj_frequency/实写盛唐.txt")
get_frequency(18, "中唐", True, 14, False, "../output/qj_frequency/实写中唐.txt")
get_frequency(18, "晚唐", True, 14, False, "../output/qj_frequency/实写晚唐.txt")

# 虚写
get_frequency(4, "春", True, 15, False, "../output/qj_frequency/虚写春.txt")
get_frequency(4, "夏", True, 15, False, "../output/qj_frequency/虚写夏.txt")
get_frequency(4, "秋", True, 15, False, "../output/qj_frequency/虚写秋.txt")
get_frequency(4, "冬", True, 15, False, "../output/qj_frequency/虚写冬.txt")

get_frequency(18, "初唐", True, 15, False, "../output/qj_frequency/虚写初唐.txt")
get_frequency(18, "盛唐", True, 15, False, "../output/qj_frequency/虚写盛唐.txt")
get_frequency(18, "中唐", True, 15, False, "../output/qj_frequency/虚写中唐.txt")
get_frequency(18, "晚唐", True, 15, False, "../output/qj_frequency/虚写晚唐.txt")
