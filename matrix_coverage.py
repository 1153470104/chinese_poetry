import matrix_excel_wraggle
import co_occur


# get the list of top words
def coverage(w_list1, w_list2, rank_list, symmetry):
    total_times = 0  # summary of all top list times
    times_sum = 0  # summary of co-times in top list
    occur_time = 0

    if symmetry:
        w_length = len(w_list1)
        top_list = rank_list[0: w_length * w_length / 2 - w_length / 2]
        r_dict = {}
        for r in top_list:
            r.replace("(", "")
            r.replace(")", "")
            r.replace(" ", "")
            r_dict[r.split(",")[0]] = int(r.split(",")[1])

        for i in range(w_length):
            for j in range(w_length):
                if i != j:
                    co_word = w_list1[i] + "-" + w_list1[j]
                    if co_word in r_dict:
                        total_times = total_times + r_dict[co_word]
                        # TODO
    else:
        w1_length = len(w_list1)
        w2_length = len(w_list2)
        top_list = rank_list[0: w1_length * w2_length]
        r_dict = {}
        for r in top_list:
            r = str(r)
            r = r.replace("(", "")
            r = r.replace(")", "")
            r = r.replace(" ", "")
            r = r.replace("'", "")
            r = r.replace(".0", "")
            total_times = total_times + int(r.split(",")[1])
            # print(int(r.split(",")[1]))
            r_dict[r.split(",")[0]] = int(r.split(",")[1])
        # co_occur.print_dict(r_dict)

        for i in range(w1_length):
            for j in range(w2_length):
                co_word = w_list1[i] + "-" + w_list2[j]
                # print(co_word)
                if co_word in r_dict.keys():
                    occur_time = occur_time + 1
                    times_sum = times_sum + r_dict[co_word]
        print("top " + str(len(top_list)) + " co-occur")
        print("matrix would cover " + str(occur_time) + " times")
        print("coverage: " + str(times_sum / total_times))


rk_list = matrix_excel_wraggle.sort_excel_matrix("时词在哪写.xls")
c_list = co_occur.get_list_top("时词", 200)
r_list = co_occur.get_list_top("在哪写", 100)
coverage(c_list, r_list, rk_list, False)
