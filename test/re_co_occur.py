from co_occur import get_txt_top
from co_occur import excel_export_co_matrix
from txt_wrangle import file_to_dict
from txt_wrangle import dict_sort_list
from txt_wrangle import list_to_file


stuff_list50 = get_txt_top("../output/tfidf_word/物象词500.txt", 50)
stuff_list100 = get_txt_top("../output/tfidf_word/物象词500.txt", 100)
people_list50 = get_txt_top("../output/tfidf_word/人词500.txt", 50)
people_list100 = get_txt_top("../output/tfidf_word/人词500.txt", 100)
location_list50 = get_txt_top("../output/tfidf_word/地点词500.txt", 50)
location_list100 = get_txt_top("../output/tfidf_word/地点词500.txt", 100)
time_list50 = get_txt_top("../output/tfidf_word/时词500.txt", 50)
time_list100 = get_txt_top("../output/tfidf_word/时词500.txt", 100)
status_list50 = get_txt_top("../output/tfidf_word/状态词500.txt", 50)
status_list100 = get_txt_top("../output/tfidf_word/状态词500.txt", 100)


excel_export_co_matrix(stuff_list50, stuff_list50, "../output/tfidf_word/newtf物象物象50.xls")
excel_export_co_matrix(location_list50, location_list50, "../output/tfidf_word/newtf地点地点50.xls")
excel_export_co_matrix(stuff_list50, location_list50, "../output/tfidf_word/newtf地点物象50.xls")
excel_export_co_matrix(people_list50, location_list50, "../output/tfidf_word/newtf地点人50.xls")
excel_export_co_matrix(status_list50, location_list50, "../output/tfidf_word/newtf地点状态50.xls")
excel_export_co_matrix(time_list50, location_list50, "../output/tfidf_word/newtf地点时间50.xls")

excel_export_co_matrix(stuff_list100, stuff_list100, "../output/tfidf_word/newtf物象物象100.xls")
excel_export_co_matrix(location_list100, location_list100, "../output/tfidf_word/newtf地点地点100.xls")
excel_export_co_matrix(stuff_list100, location_list100, "../output/tfidf_word/newtf地点物象100.xls")
excel_export_co_matrix(people_list100, location_list100, "../output/tfidf_word/newtf地点人100.xls")
excel_export_co_matrix(status_list50, location_list50, "../output/tfidf_word/newtf地点状态100.xls")
excel_export_co_matrix(time_list50, location_list50, "../output/tfidf_word/newtf地点时间100.xls")
