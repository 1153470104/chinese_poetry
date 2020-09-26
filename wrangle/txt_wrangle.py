from math import log
from co_occur import print_list
from co_occur import print_dict

"""
处理纯文本文件的一些函数
"""


def dict_sort_list(w_dict):
    """
    将字典排序，输出一个二维数组，存储 词汇 和 对应数字
    :param w_dict: 输入的字典
    :return: 一个二维倒序数据，存储词汇和数字
    """
    sort_list = sorted(w_dict.items(), key=lambda x: float(x[1]), reverse=True)
    i = 0
    for ii in sort_list:
        sort_list[i] = [ii[0], ii[1]]
        i = i+1
    return sort_list


def add_id(path, id_path):
    """ 把path中的文档加个 id 输出到id_path中 """
    f = open(path, 'r', encoding='utf-8')
    id_f = open(id_path, 'w', encoding='utf-8')

    line = f.readline()
    i = 1
    while line:
        line = str(i)+","+line
        id_f.write(line)
        line = f.readline()
        i = i+1

    id_f.close()
    f.close()


def file_to_dict(path):
    """
    读取存储有词汇+对应数字的 path文件，把里面的内容转换成 一个 字典
    :param path: 要读取的文件
    :return: 转换好的dict字典
    """
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
    """
    读取参数t_dict的内容，写到path文件里面去
    :param t_dict: 一个字典数据结构，里面存储 词汇 + 对应数字
    :param path:  要保存的文件路径
    :return: 不返回
    """
    f = open(path, 'w', encoding='utf-8')
    for i in t_dict:
        f.write(i + "," + str(t_dict[i]) + "\n")
    f.close()


def list_to_file(t_list, path):
    """
    把list输出为文件
    :param t_list: 二维数组，词汇 + 对应数字
    :param path: 输出的文件路径
    :return:不返回
    """
    f = open(path, 'w', encoding='utf-8')
    for i in t_list:
        f.write(i[0] + "," + str(i[1]) + "\n")
    f.close()


def tf_idf(doc, base):
    """
    通过doc中的词汇和对应数字，基于base语料库的词汇和对应数字，计算每个其中词汇的tfidf
    不过这个tfidf并不是严格意义上的tfidf，只是一种变形，缺少依据
    :param doc: 要用来计算 类tfidf值的词汇+对应数字文件
    :param base: 用来作为语料库的词汇+对应数字文件
    :return: 返回一个词汇 和 类tfidf指标的dict
    """
    d_dict = file_to_dict(doc)
    b_dict = file_to_dict(base)
    tf_dict = {}
    for d in d_dict:
        if d in b_dict.keys() and float(b_dict[d]) != 0.0:
            # tf_dict[d] = float(d_dict[d]) / (log(float(b_dict[d])+1) * float(b_dict[d]))
            tf_dict[d] = float(d_dict[d]) / (log(float(b_dict[d]) + 1) * log(float(b_dict[d]) + 1))
    # print_dict(tf_dict)
    return tf_dict


def idf(word, group_list):
    """
    假的 idf。。不要用
    """
    count = 0
    for d in group_list:
        if word in d:
            count = count + 1
    g_length = len(group_list)
    return log((g_length+1) / (count + 1))


def real_tf_idf(doc, group_list):
    """
    目前看来还行的tf-idf
    :param doc: 需要进行tf-idf 计算的文档，由词汇和词频组成
    :param group_list: 一个列表，每个列表的元素为该组内包含的所有词汇的集合
    :return: 返回一个词汇：tf-idf 对应的字典
    """
    d_dict = file_to_dict(doc)
    tf_dict = {}
    # i = 0
    for d in d_dict:
        # print(i)
        # i = i + 1
        print(d + ": ", end="")
        print(idf(d, group_list))
        tf_dict[d] = float(d_dict[d]) * idf(d, group_list)
    # print_dict(tf_dict)
    return tf_dict


def txt_rm_location(dict_path, path, path_rm):
    location_dict = file_to_dict(dict_path)
    f = open(path, 'r', encoding='utf-8')
    w_f = open(path_rm, 'w', encoding='utf-8')
    line = f.readline()
    while line:
        if not line.split(",")[0] in location_dict.keys():
            w_f.write(line)
        line = f.readline()
    w_f.close()
    f.close()

# dict_to_file(tf_idf("guanzhong_word/人词count.txt", "全唐诗dict.txt"), "guanzhong_word/人词tf-idf.txt")
# dict_to_file(tf_idf("guanzhong_word/动词count.txt", "全唐诗dict.txt"), "guanzhong_word/动词tf-idf.txt")
# dict_to_file(tf_idf("guanzhong_word/时词count.txt", "全唐诗dict.txt"), "guanzhong_word/时词tf-idf.txt")
# dict_to_file(tf_idf("guanzhong_word/物象词count.txt", "全唐诗dict.txt"), "guanzhong_word/物象词tf-idf.txt")
# dict_to_file(tf_idf("guanzhong_word/地点词count.txt", "全唐诗dict.txt"), "guanzhong_word/地点词tf-idf.txt")
# dict_to_file(tf_idf("guanzhong_word/状态词count.txt", "全唐诗dict.txt"), "guanzhong_word/状态词tf-idf.txt")
# dict_to_file(tf_idf("guanzhong_word/写的哪count.txt", "全唐诗dict.txt"), "guanzhong_word/写的哪tf-idf.txt")
# dict_to_file(tf_idf("guanzhong_word/在哪写count.txt", "全唐诗dict.txt"), "guanzhong_word/在哪写tf-idf.txt")
#
#
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/人词tf-idf.txt")), "guanzhong_word/人词tfidf-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/动词tf-idf.txt")), "guanzhong_word/动词tfidf-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/时词tf-idf.txt")), "guanzhong_word/时词tfidf-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/物象词tf-idf.txt")), "guanzhong_word/物象词tfidf-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/地点词tf-idf.txt")), "guanzhong_word/地点词tfidf-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/状态词tf-idf.txt")), "guanzhong_word/状态词tfidf-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/写的哪tf-idf.txt")), "guanzhong_word/写的哪tfidf-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/在哪写tf-idf.txt")), "guanzhong_word/在哪写tfidf-sort.txt")

# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/人词count.txt")), "guanzhong_word/人词count-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/动词count.txt")), "guanzhong_word/动词count-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/时词count.txt")), "guanzhong_word/时词count-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/物象词count.txt")), "guanzhong_word/物象词count-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/地点词count.txt")), "guanzhong_word/地点词count-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/状态词count.txt")), "guanzhong_word/状态词count-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/写的哪count.txt")), "guanzhong_word/写的哪count-sort.txt")
# list_to_file(dict_sort_list(file_to_dict("guanzhong_word/在哪写count.txt")), "guanzhong_word/在哪写count-sort.txt")
