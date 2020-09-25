from co_occur import csv_export_co_matrix
from co_occur import get_list


location_list = get_list("地点词")
stuff_full_list = get_list("物象词")
stuff_list = [x for x in stuff_full_list not in location_list]
status_list = get_list("状态词")
people_list = get_list("人词")
time_list = get_list("时词")

# csv_export_co_matrix(stuff_list, location_list, "../output/coverage/物象地点.csv")
# csv_export_co_matrix(stuff_list, stuff_list, "../output/coverage/物象物象.csv")
# csv_export_co_matrix(location_list, location_list, "../output/coverage/地点地点.csv")
# csv_export_co_matrix(people_list, location_list, "../output/coverage/地点人词.csv")
# csv_export_co_matrix(status_list, location_list, "../output/coverage/地点状态.csv")
# csv_export_co_matrix(time_list, location_list, "../output/coverage/地点时词.csv")
