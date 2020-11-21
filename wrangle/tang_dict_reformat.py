"""
一个检测、打印的脚本
"""

from co_occur import print_list

# f = open("../input/Tang_word.txt", 'r', encoding='utf-8')
# wf = open("../input/Tang_vocabulary.txt", 'w', encoding='utf-8')
# line = f.readline()
# whole_list = []
# while line:
#     ll = line.replace("\n", '')
#     line_list = ll.split(" ")
#     for i in line_list:
#         if i != '':
#             whole_list.append(i)
#     line = f.readline()
# print_list(whole_list)
# for d in whole_list:
#     wf.write(d + "\n")
#
# f.close()
# wf.close()
f1 = open("../input/Tang_vocabulary.txt", 'r', encoding='utf-8')
f2 = open("../input/Tang_location.txt", 'r', encoding='utf-8')
wf = open("../input/Tang_poet_dict.txt", 'w', encoding='utf-8')
line = f1.readline()
while line:
    wf.write(line)
    line = f1.readline()
line2 = f2.readline()
while line2:
    wf.write(line2)
    line2 = f2.readline()
wf.close()
