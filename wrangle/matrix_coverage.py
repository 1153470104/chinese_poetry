import matplotlib.pyplot as plt
from wrangle import co_occur, matrix_excel_wrangle

"""
计算共现矩阵覆盖率的程序
未写完，目前只能计算非对称共现矩阵的覆盖度
"""


# get the list of top words
def coverage(w_list1, w_list2, rank_list, symmetry):
    """
    通过传入的两个矩阵的坐标 list 和排好序的 ranklist， 计算自定义的 coverage
    同时利用 symmetry 区分是否是对称矩阵，
    :param w_list1: 列向量的词汇集合
    :param w_list2: 行向量的词汇集合
    :param rank_list: 共现矩阵词对 的排序集合
    :param symmetry: 是否是对称矩阵的 布尔符号
    :return: 返回由上两个列表所计算出的共现矩阵
    """
    total_times = 0  # summary of all top list times
    times_sum = 0  # summary of co-times in top list
    occur_time = 0

    if symmetry:
        w_length = len(w_list1)
        top_list = rank_list[0: w_length * w_length]
        r_dict = {}
        for r in top_list:
            r = str(r)
            r = r.replace("(", "")
            r = r.replace(")", "")
            r = r.replace(" ", "")
            r = r.replace("'", "")
            r = r.replace(".0", "")
            total_times = total_times + int(r.split(",")[1])
            r_dict[r.split(",")[0]] = int(r.split(",")[1])
        total_times = total_times / 2
        for i in range(w_length):
            for j in range(w_length):
                co_word = w_list1[i] + "-" + w_list2[j]
                # print(co_word)
                if co_word in r_dict.keys():
                    occur_time = occur_time + 1
                    times_sum = times_sum + r_dict[co_word]
        print("top " + str(len(top_list)) + ", ", end='')
        print("matrix cover " + str(occur_time) + ", ", end='')
        a = occur_time / len(top_list)
        b = times_sum / total_times / 2
        print("weight coverage: " + str(b))
        return [a, b, times_sum]

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
        print("top " + str(len(top_list)) + ", ", end='')
        print("matrix cover " + str(occur_time) + ", ", end='')
        a = occur_time / len(top_list)
        b = (times_sum / total_times)
        print("weight coverage: " + str(b))
        return [a, b, times_sum]


# rk_list = matrix_excel_wraggle.sort_excel_matrix("时词在哪写.xls")
# c_list = co_occur.get_list_top("时词", 200)
# r_list = co_occur.get_list_top("在哪写", 100)
# coverage(c_list, r_list, rk_list, False)

# def file_coverage(type1, top_num1, type2, top_num2, matrix_path, symmetry):
#     rk_list = matrix_excel_wrangle.sort_excel_matrix(matrix_path)
#     c_list = co_occur.get_list_top(type1, top_num1)
#     r_list = co_occur.get_list_top(type2, top_num2)
#     return coverage(c_list, r_list, rk_list, symmetry)


def file_coverage(type1_txt, top_num1, type2_txt, top_num2, matrix_path, symmetry):
    rk_list = matrix_excel_wrangle.sort_csv_matrix(matrix_path)
    c_list = co_occur.get_txt_top(type1_txt, top_num1)
    r_list = co_occur.get_txt_top(type2_txt, top_num2)
    return coverage(c_list, r_list, rk_list, symmetry)


def coverage_iter_graph(type1_txt, type2_txt, matrix_path, symmetry, name):
    x = []
    y = []
    z = []
    d = []
    g = []
    for i in range(1, 60):
        r2 = file_coverage(type1_txt, i * 5, type2_txt, i * 5
                           , matrix_path, symmetry)
        x.append(i * 5)
        y.append(r2[0])
        z.append(r2[1])
        d.append(r2[2])
        # g.append()

    plt.figure()
    plt.plot(x, y)
    plt.title(name + ": cover percentage")
    plt.figure()
    plt.plot(x, z)
    plt.title(name + ": weight coverage")
    # plt.figure()
    # plt.plot(x, d)
    # plt.title("total number")
    plt.show()
