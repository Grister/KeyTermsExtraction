# #  write your code here
# from lxml import etree
#
# xml_path = 'data/dataset/input.txt'
#
# with open(xml_path, 'r') as file:
#     xml_string = file.read()
#
# root = etree.fromstring(xml_string)
#
# new_list = []
# # etree.dump(root)
# for data in root[0]:
#     new_list.append(data.get('name'))
#
# print(*new_list)

import re

patern_1 = r"b?ea?st"
patern_2 = r".?.?.?.?.?"
patern_3 = r"bea?s?t?"
patern_4 = r"....."
patern_5 = r'.....?'

word_1, word_2, word_3 = "beast", "best", "east"
print(re.match(patern_1, word_1))
print(re.match(patern_1, word_2))
print(re.match(patern_1, word_3))
print()
print(re.match(patern_2, word_1))
print(re.match(patern_2, word_2))
print(re.match(patern_2, word_3))
print()
print(re.match(patern_3, word_1))
print(re.match(patern_3, word_2))
print(re.match(patern_3, word_3))
print()
print(re.match(patern_4, word_1))
print(re.match(patern_4, word_2))
print(re.match(patern_4, word_3))
print()
print(re.match(patern_5, word_1))
print(re.match(patern_5, word_2))
print(re.match(patern_5, word_3))


