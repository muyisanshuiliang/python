#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   844. 比较含退格的字符串.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/16 13:36   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
注意：如果对空文本输入退格字符，文本继续为空。

示例 1：
输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。

示例 2：
输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。

示例 3：
输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。

示例 4：
输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。
 
提示：
1 <= S.length <= 200
1 <= T.length <= 200
S 和 T 只含有小写字母以及字符 '#'。
 
进阶：
你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
'''


# import lib
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # stack_s, stack_t = [], []
        # for item_s in S:
        #     if item_s == '#':
        #         if stack_s:
        #             stack_s.pop()
        #     else:
        #         stack_s.append(item_s)
        #
        # for item_t in T:
        #     if item_t == '#':
        #         if stack_t:
        #             stack_t.pop()
        #     else:
        #         stack_t.append(item_t)
        # return stack_s == stack_t

        # stack = []
        # for item_s in S:
        #     if item_s == '#':
        #         if stack:
        #             stack.pop()
        #     else:
        #         stack.append(item_s)
        # level = 0
        # for item_inx in range(len(T) - 1, -1, -1):
        #     temp = T[item_inx]
        #     if temp != '#':
        #         if level != 0:
        #             level -= 1
        #         else:
        #             if stack and stack[-1] == temp:
        #                 stack.pop()
        #             else:
        #                 return False
        #     else:
        #         level += 1
        # return stack.__len__() == 0

        skip1 = skip2 = 0
        i, j = len(S) - 1, len(T) - 1
        while i >= 0 or j >= 0:
            char_S = char_T = ''
            while i >= 0:
                if S[i] == '#':
                    skip1 += 1
                    i -= 1
                    continue
                elif skip1 != 0:
                    i -= 1
                    skip1 -= 1
                    continue
                else:
                    char_S = S[i]
                    break

            while j >= 0:
                if T[j] == '#':
                    skip2 += 1
                    j -= 1
                    continue
                elif skip2 != 0:
                    j -= 1
                    skip2 -= 1
                    continue
                else:
                    char_T = T[j]
                    break

            if char_S != char_T:
                return False
            i -= 1
            j -= 1

        return True


solution = Solution()
# print(solution.backspaceCompare(S="a#c", T="b"))
# print(solution.backspaceCompare(S="a##c", T="#a#c"))
# print(solution.backspaceCompare("xywrrmp", "xywrrmu#p"))
print(solution.backspaceCompare("aaa###a", "aaaa###a"))
