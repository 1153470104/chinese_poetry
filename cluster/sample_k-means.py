from sklearn.cluster import KMeans
import numpy as np
import xlrd


# 打印数列
def print_list(list_data):
    for d in list_data:
        print(d)


# 得到这个matrix excel表格的 列向量 所对应的词
def get_column_list(matrix_name):
    # 打开excel表格
    workbook = xlrd.open_workbook(matrix_name)
    r_sheet = workbook.sheet_by_index(0)
    return r_sheet.row_values(0)[1:]


# 读取excel文件变成 矩阵形式
def get_matrix(matrix_name):
    # 打开excel表格
    workbook = xlrd.open_workbook(matrix_name)
    r_sheet = workbook.sheet_by_index(0)
    c_lines = len(r_sheet.row_values(1))-1
    r_lines = len(r_sheet.col_values(1))-1

    matrix = []
    for i in range(r_lines):
        matrix.append([0]*c_lines)

    for j in range(r_lines):
        for k in range(c_lines):
            matrix[j][k] = r_sheet.cell_value(j+1, k+1)

    return matrix


# 用来进行k-means的函数
def poetry_k_means(m_path, cluster_num):
    """
    使用excel 共现表格, 作为输入，选定需要聚类出的组数，
    利用sklearn进行聚类分析，没有返回值，打印聚类得出来的聚类的组

    :param m_path: 要进行聚类分析的共现矩阵文件的路径，同一个文件夹下直接写名字
    :param cluster_num: 要聚类的组数，即k
    :return: 暂时没有

    只是初步的聚类，调参什么的 因为不是很会 所以没有搞
    所以效果非常不好，目前没有看出什么东西。。
    """
    matrix = np.array(get_matrix(m_path))
    column_list = get_column_list(m_path)
    length = len(column_list)

    k_means = KMeans(n_clusters=cluster_num, random_state=0).fit(matrix)
    label = k_means.labels_
    group_list = []
    for i in range(cluster_num):
        e_list = []
        for j in range(length):
            if label[j] == i:
                e_list.append(column_list[j])
        group_list.append(e_list)
    print_list(group_list)


# sample:
# 输入一个文件夹下的 xls文件："地点物象100.xls"
# 以及要聚类分成的组 7组
poetry_k_means("地点物象100.xls", 7)
