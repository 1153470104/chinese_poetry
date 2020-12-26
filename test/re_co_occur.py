"""
共现+补词共现
加节日的共现
"""
from co_occur import get_txt_top, get_list, get_list_top
from co_occur import excel_export_co_matrix
from txt_wrangle import file_to_dict
from txt_wrangle import dict_sort_list
from txt_wrangle import list_to_file


festival_list = get_list("节庆")
time_list = get_list("时词")
nomapping_loc_list = get_list("no mapping 地点")
mapping_loc_list = get_list("mapping 地点")
poeple_list = get_list("人词")
activity_list = get_list("活动")
motion_list = get_list("动词")
stuff_list = get_list("物词")

excel_export_co_matrix(festival_list, activity_list, "../output/co_fes_period/晚唐节庆活动.xls")
excel_export_co_matrix(festival_list, nomapping_loc_list, "../output/co_fes_period/晚唐节庆nomapping.xls")
excel_export_co_matrix(festival_list, mapping_loc_list, "../output/co_fes_period/晚唐节庆mapping.xls")
excel_export_co_matrix(festival_list, time_list, "../output/co_fes_period/晚唐节庆时间.xls")
excel_export_co_matrix(festival_list, stuff_list, "../output/co_fes_period/晚唐节庆物象.xls")
excel_export_co_matrix(festival_list, motion_list, "../output/co_fes_period/晚唐节庆动作.xls")

# location_add = ['长安', '五陵', '新丰', '春宫', '咸阳']
# people_add = ['佳人', '天子', '王孙', '明主', '神仙']
# time_add = ['春', '秋', '晚', '朝', '暮', '秦', '汉']
# status_add = ['远']
# stuff_add = ['云', '花', '路', '水', '山', '树', '风', '雨', '日', '雪', '地', '月', '草', '柳']
#
# stuff2_list50 = get_txt_top("../output/tfidf_word/物象词（去地点）500.txt", 50)
# people_list50 = get_txt_top("../output/tfidf_word/人词500.txt", 50)
# location_list50 = get_txt_top("../output/tfidf_word/地点词500.txt", 50)
# time_list50 = get_txt_top("../output/tfidf_word/时词500.txt", 50)
# status_list50 = get_txt_top("../output/tfidf_word/状态词500.txt", 50)
#
# add_stuff2_list50 = stuff2_list50 + stuff_add
# add_people_list50 = people_add + people_list50
# add_location_list50 = location_add + location_list50
# add_time_list50 = time_add + time_list50
# add_status_list50 = status_list50 + status_add

# stuff_list50 = get_txt_top("../output/tfidf_word/物象词500.txt", 50)

# stuff_list100 = get_txt_top("../output/tfidf_word/物象词500.txt", 100)
# stuff2_list100 = get_txt_top("../ou0tput/tfidf_word/物象词（去地点）500.txt", 100)
# people_list100 = get_txt_top("../output/tfidf_word/人词500.txt", 100)
# location_list100 = get_txt_top("../output/tfidf_word/地点词500.txt", 100)
# time_list100 = get_txt_top("../output/tfidf_word/时词500.txt", 100)
# status_list100 = get_txt_top("../output/tfidf_word/状态词500.txt", 100)
#




# excel_export_co_matrix(stuff2_list50, stuff2_list50, "../output/tfidf_word/newtf物象物象（去地点）50.xls")
# excel_export_co_matrix(stuff2_list50, location_list50, "../output/tfidf_word/newtf地点物象（去地点）50.xls")
# excel_export_co_matrix(stuff_list50, stuff_list50, "../output/tfidf_word/newtf物象物象50.xls")
# excel_export_co_matrix(location_list50, location_list50, "../output/tfidf_word/newtf地点地点50.xls")
# excel_export_co_matrix(stuff_list50, location_list50, "../output/tfidf_word/newtf地点物象50.xls")
# excel_export_co_matrix(people_list50, location_list50, "../output/tfidf_word/newtf地点人50.xls")
# excel_export_co_matrix(status_list50, location_list50, "../output/tfidf_word/newtf地点状态50.xls")
# excel_export_co_matrix(time_list50, location_list50, "../output/tfidf_word/newtf地点时间50.xls")
#
# excel_export_co_matrix(stuff2_list100, stuff2_list100, "../output/output1029/newtf物象物象（去地点）100.xls")
# excel_export_co_matrix(stuff2_list10, location_list100, "../output/output1029/newtf地点物象（去地点）100.xls")
# excel_export_co_matrix(stuff_list100, stuff_list100, "../output/output1029/newtf物象物象100.xls")
# excel_export_co_matrix(location_list100, location_list100, "../output/output1029/newtf地点地点100.xls")
# excel_export_co_matrix(stuff_list100, location_list100, "../output/output1029/newtf地点物象100.xls")
# excel_export_co_matrix(people_list100, location_list100, "../output/output1029/newtf地点人100.xls")
# excel_export_co_matrix(status_list50, location_list50, "../output/output1029/newtf地点状态100.xls")
# excel_export_co_matrix(time_list50, location_list50, "../output/output1029/newtf地点时间100.xls")

# excel_export_co_matrix(add_stuff2_list50, add_stuff2_list50, "../output/output1029/newtf物象物象（去地点）50.xls")
# excel_export_co_matrix(add_stuff2_list50, add_location_list50, "../output/output1029/newtf地点物象（去地点）50.xls")
# excel_export_co_matrix(add_location_list50, add_location_list50, "../output/output1029/newtf地点地点50.xls")
# excel_export_co_matrix(add_people_list50, add_location_list50, "../output/output1029/newtf地点人50.xls")
# excel_export_co_matrix(add_status_list50, add_location_list50, "../output/output1029/newtf地点状态50.xls")
# excel_export_co_matrix(add_time_list50, add_location_list50, "../output/output1029/newtf地点时间50.xls")
