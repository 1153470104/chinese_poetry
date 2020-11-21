"""
计算不同的分词方式正确率的脚本
"""

from participle import jiayan_tokenize
from test_material_format import correctness
from test_material_format import get_test_list
from participle import jieba_tokenize
from participle import pkuseg_tokenize
from co_occur import print_list


correctness(jiayan_tokenize(get_test_list()))
correctness(jieba_tokenize(get_test_list()))
# correctness(pkuseg_tokenize(get_test_list()))
