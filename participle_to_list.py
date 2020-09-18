import re
import xlrd


workbook = xlrd.open_workbook("全唐诗jiayan.xls")
sheet = workbook.sheet_by_index(0)
p_data = sheet.col_values(1)


def dict_to_file(t_dict, path):
    f = open(path, 'w', encoding='utf-8')
    for i in t_dict:
        f.write(i + "," + str(t_dict[i]) + "\n")
    f.close()


pw_dict = {}
for pp in p_data:
    pp = re.sub("\\(.*?\\)", "", pp)
    pp = pp.replace(",", "")
    pp = pp.replace("，", "")
    pp = pp.replace("。", "")
    p_split = pp.split(" ")
    for w in p_split:
        if w in pw_dict.keys():
            pw_dict[w] = pw_dict[w] + 1
        else:
            pw_dict[w] = 1

dict_to_file(pw_dict, "全唐诗dict.txt")

