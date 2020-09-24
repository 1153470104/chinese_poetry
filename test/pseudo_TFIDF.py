"""
divide the whole tang poetry set into 500-poetry (or other scale) sets
use those sets as different text material to calculate TF-IDF number
"""

import txt_wrangle
import participle_to_list

# co_occur.print_list([0, 1])
# g_list_1 = participle_to_list.get_scale_list(1)
# g_list_50 = participle_to_list.get_scale_list(50)
# g_list_100 = participle_to_list.get_scale_list(100)
# g_list_200 = participle_to_list.get_scale_list(200)
g_list_500 = participle_to_list.get_scale_list(500)

# txt_wraggle.list_to_file(
#     txt_wraggle.dict_sort_list(
#         txt_wraggle.real_tf_idf(
#             "../output/guanzhong_word/地点词count.txt", g_list_500))
#     , "../output/tfidf_word/地点词500.txt")
# txt_wraggle.list_to_file(txt_wraggle.dict_sort_list(txt_wraggle.real_tf_idf("../output/guanzhong_word/物象词count.txt", g_list_500)), "../output/tfidf_word/物象词500.txt")
# txt_wraggle.list_to_file(txt_wraggle.dict_sort_list(txt_wraggle.real_tf_idf("../output/guanzhong_word/人词count.txt", g_list_500)), "../output/tfidf_word/人词500.txt")
# txt_wraggle.list_to_file(txt_wraggle.dict_sort_list(txt_wraggle.real_tf_idf("../output/guanzhong_word/地点词count.txt", g_list_500)), "../output/tfidf_word/地点词500.txt")
# txt_wraggle.list_to_file(txt_wraggle.dict_sort_list(txt_wraggle.real_tf_idf("../output/guanzhong_word/状态词count.txt", g_list_500)), "../output/tfidf_word/状态词500.txt")
# txt_wraggle.list_to_file(txt_wraggle.dict_sort_list(txt_wraggle.real_tf_idf("../output/guanzhong_word/时词count.txt", g_list_500)), "../output/tfidf_word/时词500.txt")
# txt_wrangle.add_id("../output/tfidf_word/人词500.txt", "../output/tfidf_word/id人词500.txt")
# txt_wrangle.add_id("../output/tfidf_word/物象词500.txt", "../output/tfidf_word/id物象词500.txt")
# txt_wrangle.add_id("../output/tfidf_word/地点词500.txt", "../output/tfidf_word/id地点词500.txt")
# txt_wrangle.add_id("../output/tfidf_word/状态词500.txt", "../output/tfidf_word/id状态词500.txt")
# txt_wrangle.add_id("../output/tfidf_word/时词500.txt", "../output/tfidf_word/id时词500.txt")

# txt_wraggle.list_to_file(txt_wraggle.dict_sort_list(txt_wraggle.real_tf_idf("../output/guanzhong_word/物象词count.txt", g_list_100)), "../output/tfidf_word/物象词100.txt")
# txt_wraggle.list_to_file(txt_wraggle.dict_sort_list(txt_wraggle.real_tf_idf("../output/guanzhong_word/人词count.txt", g_list_100)), "../output/tfidf_word/人词100.txt")
# txt_wraggle.list_to_file(txt_wraggle.dict_sort_list(txt_wraggle.real_tf_idf("../output/guanzhong_word/地点词count.txt", g_list_100)), "../output/tfidf_word/地点词100.txt")

# txt_wrangle.txt_rm_location("../output/tfidf_word/地点词500.txt", "../output/tfidf_word/物象词500.txt", "../output/tfidf_word/物象词（去地点）500.txt")

