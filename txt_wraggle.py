from math import log


def print_dict(dict_data):
    for d in dict_data:
        print(d + ": " + str(dict_data[d]))


def dict_sort_list(w_dict):
    sort_list = sorted(w_dict.items(), key=lambda x: float(x[1]), reverse=True)
    i = 0
    for ii in sort_list:
        sort_list[i] = [ii[0], ii[1]]
        i = i+1
    # print_list(sort_list)
    return sort_list


def print_list(list_data):
    for d in list_data:
        print(d)


def file_to_dict(path):
    f = open(path, 'r', encoding='utf-8')
    f_dict = {}
    line = f.readline()
    while line:
        line = line.replace("\n", "")
        # print(line)
        f_dict[line.split(",")[0]] = line.split(",")[1]
        line = f.readline()
    f.close()
    return f_dict


def dict_to_file(t_dict, path):
    f = open(path, 'w', encoding='utf-8')
    for i in t_dict:
        f.write(i + "," + str(t_dict[i]) + "\n")
    f.close()


def list_to_file(t_list, path):
    f = open(path, 'w', encoding='utf-8')
    for i in t_list:
        f.write(i[0] + "," + str(i[1]) + "\n")
    f.close()


def tf_idf(doc, base):
    d_dict = file_to_dict(doc)
    b_dict = file_to_dict(base)
    tf_dict = {}
    for d in d_dict:
        if d in b_dict.keys() and float(b_dict[d]) != 0.0:
            tf_dict[d] = float(d_dict[d]) / log(float(b_dict[d])+1)
    # print_dict(tf_dict)
    return tf_dict


dict_to_file(tf_idf("guanzhong_word/人词count.txt", "全唐诗dict.txt"), "guanzhong_word/人词tf-idf.txt")
dict_to_file(tf_idf("guanzhong_word/动词count.txt", "全唐诗dict.txt"), "guanzhong_word/动词tf-idf.txt")
dict_to_file(tf_idf("guanzhong_word/时词count.txt", "全唐诗dict.txt"), "guanzhong_word/时词tf-idf.txt")
dict_to_file(tf_idf("guanzhong_word/物象词count.txt", "全唐诗dict.txt"), "guanzhong_word/物象词tf-idf.txt")
dict_to_file(tf_idf("guanzhong_word/地点词count.txt", "全唐诗dict.txt"), "guanzhong_word/地点词tf-idf.txt")
dict_to_file(tf_idf("guanzhong_word/状态词count.txt", "全唐诗dict.txt"), "guanzhong_word/状态词tf-idf.txt")
dict_to_file(tf_idf("guanzhong_word/写的哪count.txt", "全唐诗dict.txt"), "guanzhong_word/写的哪tf-idf.txt")
dict_to_file(tf_idf("guanzhong_word/在哪写count.txt", "全唐诗dict.txt"), "guanzhong_word/在哪写tf-idf.txt")


list_to_file(dict_sort_list(file_to_dict("guanzhong_word/人词tf-idf.txt")), "guanzhong_word/人词tfidf-sort.txt")
list_to_file(dict_sort_list(file_to_dict("guanzhong_word/动词tf-idf.txt")), "guanzhong_word/动词tfidf-sort.txt")
list_to_file(dict_sort_list(file_to_dict("guanzhong_word/时词tf-idf.txt")), "guanzhong_word/时词tfidf-sort.txt")
list_to_file(dict_sort_list(file_to_dict("guanzhong_word/物象词tf-idf.txt")), "guanzhong_word/物象词tfidf-sort.txt")
list_to_file(dict_sort_list(file_to_dict("guanzhong_word/地点词tf-idf.txt")), "guanzhong_word/地点词tfidf-sort.txt")
list_to_file(dict_sort_list(file_to_dict("guanzhong_word/状态词tf-idf.txt")), "guanzhong_word/状态词tfidf-sort.txt")
list_to_file(dict_sort_list(file_to_dict("guanzhong_word/写的哪tf-idf.txt")), "guanzhong_word/写的哪tfidf-sort.txt")
list_to_file(dict_sort_list(file_to_dict("guanzhong_word/在哪写tf-idf.txt")), "guanzhong_word/在哪写tfidf-sort.txt")
