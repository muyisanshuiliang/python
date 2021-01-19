"""
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"

示例 3：
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"

示例 4：
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"

"""

import re


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 通过正则把中间的数字全部解析出来
        rx = re.compile('\\D')
        s_number = [int(i) for i in rx.split(s) if len(i) != 0]
        # 定义一个栈，用于数据处理
        stack = []
        inx = len(s) - 1
        # 对字符串从右至左依次处理
        while inx >= 0:
            # 判断当前是否为‘[’，如果是则意味着需要对字符串与数字进行相乘
            if s[inx] == '[':
                temp_str = ''
                while stack[-1] != ']':
                    temp_str += stack.pop()
                # 循环最后记得把左括号弹出来
                stack.pop()
                temp_str = temp_str * s_number.pop()
                stack.append(temp_str)
            elif s[inx].isdigit():
                pass
            else:
                stack.append(s[inx])
            inx -= 1
        stack.reverse()
        return ''.join(stack)


s = "3[a3[a]]2[bc]"
print(Solution().decodeString(s))
