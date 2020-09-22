from sklearn.cluster import KMeans
import numpy as np
from matrix_excel_wraggle import get_matrix
from matrix_excel_wraggle import get_column_list
from co_occur import print_list


def poetry_k_means(m_path, length, cluster_num):
    matrix = np.array(get_matrix(m_path))
    column_list = get_column_list(m_path)

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


path = "../output/output_908/地点物象100.xls"
poetry_k_means(path, 100, 7)
# print(kmeans.predict([[0, 0], [12, 3], [100, 9], [4, 4]]))
# print(kmeans.cluster_centers_)

# from sklearn.cluster import KMeans
#
# num_clusters = 7
# km_cluster = KMeans(n_clusters=num_clusters, max_iter=300, n_init=40
#                     , init='k-means++', n_jobs=-1)
#
# # 返回各自文本的所被分配到的类索引
# result = km_cluster.fit_predict(tfidf_matrix)
#
# print("Predicting result: ", result)
