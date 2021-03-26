#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1190. 反转每对括号间的子串.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/23 16:46   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给出一个字符串 s（仅含有小写英文字母和括号）。
请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
注意，您的结果中 不应 包含任何括号。

示例 1：
输入：s = "(abcd)"
输出："dcba"

示例 2：
输入：s = "(u(love)i)"
输出："iloveu"

示例 3：
输入：s = "(ed(et(oc))el)"
#         (ed(etco)el)
#         (edocteel)
#         (leetcode)
输出："leetcode"

示例 4：
输入：s = "a(bcdefghijkl(mno)p)q"
输出："apmnolkjihgfedcbq"

提示：
0 <= s.length <= 2000
s 中只有小写英文字母和括号
我们确保所有括号都是成对出现的
'''


# import lib
class Solution:
    def reverseParentheses(self, s: str) -> str:
        # N = len(s)
        # if N <= 1:
        #     return s
        # stack = []
        # for index in range(N - 1, -1, -1):
        #     if s[index] != '(':
        #         stack.append(s[index])
        #         continue
        #     data = []
        #     while stack and stack[-1] != ')':
        #         data.append(stack.pop())
        #     if stack[-1] == ')':
        #         stack.pop()
        #     while data:
        #         stack.append(data.pop(0))
        # stack.reverse()
        # return ''.join(stack)

        stack = ['']
        for c in s:
            if c == '(':
                stack.append('')
            elif c == ')':
                x = stack.pop()
                stack[-1] += x[::-1]
            else:
                stack[-1] += c
        return stack[0]


solution = Solution()
print(solution.reverseParentheses("(ed(et(oc))el)"))
print(solution.reverseParentheses("a(bcdefghijkl(mno)p)q"))
