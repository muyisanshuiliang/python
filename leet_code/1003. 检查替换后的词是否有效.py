#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1003. 检查替换后的词是否有效.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/23 16:30   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给你一个字符串 s ，请你判断它是否 有效 。
字符串 s 有效 需要满足：假设开始有一个空字符串 t = "" ，你可以执行 任意次 下述操作将 t 转换为 s ：
将字符串 "abc" 插入到 t 中的任意位置。形式上，t 变为 tleft + "abc" + tright，其中 t == tleft + tright 。
注意，tleft 和 tright 可能为 空 。
如果字符串 s 有效，则返回 true；否则，返回 false。

示例 1：
输入：s = "aabcbc"
输出：true
解释：
"" -> "abc" -> "aabcbc"
因此，"aabcbc" 有效。

示例 2：
输入：s = "abcabcababcc"
输出：true
解释：
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
因此，"abcabcababcc" 有效。

示例 3：
输入：s = "abccba"
输出：false
解释：执行操作无法得到 "abccba" 。

示例 4：
输入：s = "cababc"
输出：false
解释：执行操作无法得到 "cababc" 。
 
提示：
1 <= s.length <= 2 * 104
s 由字母 'a'、'b' 和 'c' 组成
'''


# import lib

class Solution:
    def isValid(self, s: str) -> bool:

        # 解法一：库函数
        # while 'abc' in s:
        #     s = s.replace('abc', '')
        # return not s

        N = len(s)
        if N <= 2:
            return False
        stack = [s[-1], s[-2]]
        print(stack)
        for i in range(N - 3, -1, -1):
            if len(stack) >= 2:
                middle = stack[-1]
                tail = stack[-2]
                if 'abc' == s[i] + middle + tail:
                    stack.pop()
                    stack.pop()
                    continue
            stack.append(s[i])
        return not stack


solution = Solution()
print(solution.isValid("abcabcababcc"))
print(solution.isValid("cababc"))
