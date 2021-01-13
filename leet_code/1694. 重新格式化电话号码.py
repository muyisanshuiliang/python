import re


class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """


number = "1-23-45 6,234,5,622"
r = '\D'
# 将不符合正则表达式的元素替换成 ''
number = re.sub(r, '', number)
length = len(number)
print(length)
print(number)
new_phone_number = ''
print(list(range(0, length, 3)))
for index in list(range(0, length, 3)):
    if length - index == 3 or length - index == 2:
        new_phone_number = new_phone_number + number[index:]
        break
    elif length - index == 4:
        new_phone_number = new_phone_number + number[index:index + 2] + '-' + number[index + 2:]
        break
    else:
        new_phone_number = new_phone_number + number[index:index + 3] + '-'
print(new_phone_number)
