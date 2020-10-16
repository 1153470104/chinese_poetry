from participle import jiayan_tokenize
from test_material_format import correctness
from test_material_format import get_test_list

correctness(jiayan_tokenize(get_test_list()))
