import re


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        rx = re.compile('\D')
        i_number = [int(i) for i in rx.split(s) if len(i) != 0]
        s_number = []
        end = len(s) - 1
        result = ''
        while end >= 0:
            if s[end] == ']':
                s_number.append(']')
            elif s[end] == '[':
                result = result * i_number.pop()



s = "3[a]2[bc]"
print(s)
rx = re.compile('\d\\[{1}|\\]{1}\d\[{1}|\]{1}')
s_number = [i for i in rx.split(s) if len(i) != 0]
print(s_number)
print(type(s_number))

s = "33[a]2[2[bc]]"
rx = re.compile('\D')
i_number = [int(i) for i in rx.split(s) if len(i) != 0]
print(i_number)
print(type(i_number))

print('saaa' * 3)
result = ''
for s, i in zip(s_number, i_number):
    result = result + s * i
print(result)
