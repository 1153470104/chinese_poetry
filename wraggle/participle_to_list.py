import re
import xlrd

# 打开excel表格
workbook = xlrd.open_workbook("全唐诗jiayan.xls")
sheet = workbook.sheet_by_index(0)
p_data = sheet.col_values(1)


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


pw_dict = {}
for pp in p_data:
    pp = re.sub("\\(.*?\\)", "", pp)            # 之前发现格式化不干净，漏了‘(’‘)’再格式一遍
    pp = pp.replace(",", "")                    # 标点符号都去掉
    pp = pp.replace("，", "")
    pp = pp.replace("。", "")
    # 在遍历p_data的时候 遍历p_split 存到dict里面
    p_split = pp.split(" ")
    for w in p_split:
        if w in pw_dict.keys():
            pw_dict[w] = pw_dict[w] + 1
        else:
            pw_dict[w] = 1

# 然后存到全唐诗dict.txt里面
dict_to_file(pw_dict, "全唐诗dict.txt")

