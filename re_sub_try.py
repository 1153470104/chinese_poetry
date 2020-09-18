import re

s = "春日 出 苑游瞩 （ 太子 时 作 ） 三阳 丽景 早 芳辰 "
print(re.sub(u"（.*?）", "", s))
