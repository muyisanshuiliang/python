#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   224. 基本计算器.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/10 10:44   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。

示例 1：
输入：s = "1 + 1"
输出：2

示例 2：
输入：s = " 2-1 + 2 "
输出：3

示例 3：
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23

提示：
1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式
'''


# import lib
class Solution:
    def calculate(self, s: str) -> int:
        # if not s:
        #     return None
        #
        # def is_num(i):
        #     return i != '+' and i != '-' and i != ')' and i != '('
        #
        # stack = []
        # inx = len(s) - 1
        # while inx >= 0:
        #     if s[inx] == ' ':
        #         inx -= 1
        #         continue
        #     if (temp := s[inx]) == ')':
        #         stack.append(temp)
        #         inx -= 1
        #         continue
        #     if s[inx] == '(':
        #         temp_result = 0
        #         operator = None
        #         while stack and stack[-1] != ')':
        #             if stack[-1] != '+' and stack[-1] != '-' and operator is None:
        #                 temp_result = stack.pop()
        #             elif stack[-1] == '+' or stack[-1] == '-':
        #                 operator = stack.pop()
        #             else:
        #                 if operator == '+':
        #                     temp_result += stack.pop()
        #                 elif operator == '-':
        #                     temp_result -= stack.pop()
        #         stack.pop()
        #         stack.append(temp_result)
        #     elif s[inx] == '+' or s[inx] == '-':
        #         stack.append(s[inx])
        #     else:
        #         temp_num_str = s[inx]
        #         while inx > 0 and is_num(s[inx - 1]):
        #             inx -= 1
        #             if s[inx] == ' ':
        #                 continue
        #             temp_num_str = s[inx] + temp_num_str
        #         stack.append(int(temp_num_str))
        #     inx -= 1
        #
        # result = 0
        # operator = None
        # while stack:
        #     if stack[-1] != '+' and stack[-1] != '-' and operator is None:
        #         result = stack.pop()
        #     elif stack[-1] == '+' or stack[-1] == '-':
        #         operator = stack.pop()
        #     else:
        #         if operator == '+':
        #             result += stack.pop()
        #         elif operator == '-':
        #             result -= stack.pop()
        # return result

        # res：表示左边表达式除去栈内保存元素的计算结果；
        # sign：表示运算符；
        # num：表示当前遇到的数字，会更新到res中；
        # 用栈保存遇到左括号时前面计算好了的结果和运算符。
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            # 如果是数字，则对数字进行处理
            if c.isdigit():
                num = 10 * num + int(c)
            # 如果碰到的是运算符,说明右边的表达式处理完了
            elif c == "+" or c == "-":
                # 结果 = 左边的表达式res 运算符sign 右边的表达是num
                res += sign * num
                # 修改 num 为0
                num = 0
                # 为运算符赋新值，如果是加法 sign = 1，如果是减法 sign = -1
                sign = 1 if c == "+" else -1
            # 如果碰到的是左括号
            elif c == "(":
                # 把当前计算的结果和运算符存入栈
                stack.append(res)
                stack.append(sign)
                # 对计算结果和运算符赋新值
                res = 0
                sign = 1
            # 如果碰到的是右括号
            elif c == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res


solution = Solution()
print(solution.calculate(s="(1+(4+5+2)-3)+(6+8)"))
