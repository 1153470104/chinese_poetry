from wrangle.co_occur import get_list
from wrangle.co_occur import print_matrix
from wrangle.matrix_excel_wrangle import sort_csv_matrix
from wrangle.matrix_excel_wrangle import get_csv_matrix
from wrangle.matrix_coverage import file_coverage
from wrangle.matrix_coverage import coverage_iter_graph
from wrangle.co_occur import file_to_dict
from wrangle.txt_wrangle import dict_sort_list
from wrangle.txt_wrangle import list_to_file


# # sort raw word txt
# list_to_file(dict_sort_list(file_to_dict("../output/guanzhong_word/人词count.txt")), "../output/guanzhong_word/人词count-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("../output/guanzhong_word/物象词count.txt")), "../output/guanzhong_word/物象词count-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("../output/guanzhong_word/状态词count.txt")), "../output/guanzhong_word/状态词count-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("../output/guanzhong_word/时词count.txt")), "../output/guanzhong_word/时词count-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("../output/guanzhong_word/地点词count.txt")), "../output/guanzhong_word/地点词count-sort.txt")


# stuff_full_list = get_list("物象词")
# location_list = get_list("地点词")
# stuff_list = [x for x in stuff_full_list if x not in location_list]
# status_list = get_list("状态词")
# people_list = get_list("人词")
# time_list = get_list("时词")

stuff_path = "../output/guanzhong_word/物象词count-sort.txt"
location_path = "../output/guanzhong_word/地点词count-sort.txt"
people_path = "../output/guanzhong_word/人词count-sort.txt"
status_path = "../output/guanzhong_word/状态词count-sort.txt"
time_path = "../output/guanzhong_word/时词count-sort.txt"

idf_stuff_path = "../output/tfidf_word/物象词（去地点）500.txt"
idf_location_path = "../output/tfidf_word/地点词500.txt"
idf_people_path = "../output/tfidf_word/人词500.txt"
idf_status_path = "../output/tfidf_word/状态词500.txt"
idf_time_path = "../output/tfidf_word/时词500.txt"
# print_matrix(get_csv_matrix("../output/coverage/地点状态.csv"))
# sort_csv_matrix("../output/coverage/地点状态.csv")

# coverage_iter_graph(people_path, location_path, "../output/coverage/地点人词.csv", False)
# coverage_iter_graph(stuff_path, location_path, "../output/coverage/物象地点.csv", False)
# coverage_iter_graph(time_path, location_path, "../output/coverage/地点时词.csv", False)
# coverage_iter_graph(location_path, status_path, "../output/coverage/地点状态.csv", False)
coverage_iter_graph(location_path, location_path, "../output/coverage/地点地点.csv", True)

# coverage_iter_graph(idf_people_path, idf_location_path, "../output/coverage/地点人词.csv", False)
# coverage_iter_graph(idf_stuff_path, idf_location_path, "../output/coverage/物象地点.csv", False)
# coverage_iter_graph(idf_time_path, idf_location_path, "../output/coverage/地点时词.csv", False)
# coverage_iter_graph(idf_location_path, idf_status_path, "../output/coverage/地点状态.csv", False)
# coverage_iter_graph(idf_location_path, idf_location_path, "../output/coverage/地点地点.csv", True)
