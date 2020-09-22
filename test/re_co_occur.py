from co_occur import get_txt_top
from co_occur import excel_export_co_matrix
from txt_wraggle import file_to_dict
from txt_wraggle import dict_sort_list
from txt_wraggle import list_to_file


stuff_list50 = get_txt_top("../output/tfidf_word/物象词500.txt", 50)
stuff_list100 = get_txt_top("../output/tfidf_word/物象词500.txt", 100)
people_list50 = get_txt_top("../output/tfidf_word/人词500.txt", 50)
people_list100 = get_txt_top("../output/tfidf_word/人词500.txt", 100)
location_list50 = get_txt_top("../output/tfidf_word/地点词500.txt", 50)
location_list100 = get_txt_top("../output/tfidf_word/地点词500.txt", 100)


excel_export_co_matrix(stuff_list50, stuff_list50, "../output/tfidf_word/newtf物象物象50.xls")
excel_export_co_matrix(location_list50, location_list50, "../output/tfidf_word/newtf地点地点50.xls")
excel_export_co_matrix(stuff_list50, location_list50, "../output/tfidf_word/newtf地点物象50.xls")
excel_export_co_matrix(people_list50, location_list50, "../output/tfidf_word/newtf地点人50.xls")

excel_export_co_matrix(stuff_list100, stuff_list100, "../output/tfidf_word/newtf物象物象100.xls")
excel_export_co_matrix(location_list100, location_list100, "../output/tfidf_word/newtf地点地点100.xls")
excel_export_co_matrix(stuff_list100, location_list100, "../output/tfidf_word/newtf地点物象100.xls")
excel_export_co_matrix(people_list100, location_list100, "../output/tfidf_word/newtf地点人100.xls")
