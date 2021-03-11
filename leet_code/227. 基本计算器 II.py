#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   227. 基本计算器 II.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/11 9:40   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。

示例 1：
输入：s = "3+2*2"
输出：7

示例 2：
输入：s = " 3/2 "
输出：1

示例 3：
输入：s = " 3+5 / 2 "
输出：5

提示：
1 <= s.length <= 3 * 105
s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
s 表示一个 有效表达式
表达式中的所有整数都是非负整数，且在范围 [0, 231 - 1] 内
题目数据保证答案是一个 32-bit 整数
'''


# import lib
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            # 处理数字
            if each.isdigit():
                num = 10 * num + int(each)
            # 如果当前是最后一个或者是运算符，表示当前位置所处的数据已经处理完毕
            if i == len(s) - 1 or each in '+-*/':
                # 如果前一个字符是+，存正数入栈
                if pre_op == '+':
                    stack.append(num)
                # 如果前一个字符是-，存负数入栈
                elif pre_op == '-':
                    stack.append(-num)
                # 如果前一个字符是*，将栈顶元素与当前值进行计算，并将计算结果入栈
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                # 如果前一个字符是/，将栈顶元素与当前值进行计算，并将结果入栈
                elif pre_op == '/':
                    top = stack.pop()
                    # 注意区分计算大于0和小于0
                    if top < 0:
                        # -5 / 2 == -2.5
                        # -5 //2 == -3
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                pre_op = each
                num = 0
        return sum(stack)


solution = Solution()
print(solution.calculate(' 3+5 / 2 '))