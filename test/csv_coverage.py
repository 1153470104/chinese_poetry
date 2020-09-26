from wrangle.co_occur import get_list
from wrangle.co_occur import print_matrix
from wrangle.matrix_excel_wrangle import sort_csv_matrix
from wrangle.matrix_excel_wrangle import get_csv_matrix
from wrangle.matrix_coverage import file_coverage


stuff_full_list = get_list("物象词")
location_list = get_list("地点词")
stuff_list = [x for x in stuff_full_list if x not in location_list]
status_list = get_list("状态词")
people_list = get_list("人词")
time_list = get_list("时词")

# print_matrix(get_csv_matrix("../output/coverage/地点状态.csv"))
# sort_csv_matrix("../output/coverage/地点状态.csv")
