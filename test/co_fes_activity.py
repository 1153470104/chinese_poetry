import xlrd
import xlwt


r_book = xlrd.open_workbook("../input/1124fes_fes_loc_activity.xls")
sheet = r_book.sheet_by_index(0)
w_book = xlwt.Workbook()
r_sheet = w_book.add_sheet("0")

i = 0
j = 0
while True:
    try:
        w_list = sheet.row_values(i)
        for k in range(len(w_list)):
            r_sheet.write(j, k, w_list[k])
        j = j+1
        if w_list[3] != "":
            r_sheet.write(j, 0, w_list[0])
            r_sheet.write(j, 1, "活动")
            r_sheet.write(j, 4, w_list[3])
            j = j+1
        i = i + 1
    except IndexError:  # 用错误处理机制进行退出
        print("get to the end")
        break
    else:
        continue


w_book.save("../input/1124fes_act.xls")
