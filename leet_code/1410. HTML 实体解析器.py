#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1410. HTML 实体解析器.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/26 14:57   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
「HTML 实体解析器」 是一种特殊的解析器，它将 HTML 代码作为输入，并用字符本身替换掉所有这些特殊的字符实体。
HTML 里这些特殊字符和它们对应的字符实体包括：

双引号：字符实体为 &quot; ，对应的字符是 " 。
单引号：字符实体为 &apos; ，对应的字符是 ' 。
与符号：字符实体为 &amp; ，对应对的字符是 & 。
大于号：字符实体为 &gt; ，对应的字符是 > 。
小于号：字符实体为 &lt; ，对应的字符是 < 。
斜线号：字符实体为 &frasl; ，对应的字符是 / 。
给你输入字符串 text ，请你实现一个 HTML 实体解析器，返回解析器解析后的结果。

示例 1：
输入：text = "&amp; is an HTML entity but &ambassador; is not."
输出："& is an HTML entity but &ambassador; is not."
解释：解析器把字符实体 &amp; 用 & 替换

示例 2：
输入：text = "and I quote: &quot;...&quot;"
输出："and I quote: \"...\""

示例 3：
输入：text = "Stay home! Practice on Leetcode :)"
输出："Stay home! Practice on Leetcode :)"

示例 4：
输入：text = "x &gt; y &amp;&amp; x &lt; y is always false"
输出："x > y && x < y is always false"

示例 5：
输入：text = "leetcode.com&frasl;problemset&frasl;all"
输出："leetcode.com/problemset/all"

提示：
1 <= text.length <= 10^5
字符串可能包含 256 个ASCII 字符中的任意字符。
'''


# import lib

class Solution:
    def entityParser(self, text: str) -> str:
        # 解法一：replace

        # 解法二：遍历处理
        d = {"&quot;": '"', "&apos;": "'", "&amp;": "&", "&gt;": ">", "&lt;": "<", "&frasl;": "/"}
        if not text or len(text) < 4:
            return text
        stack = []
        inx, N = 0, len(text)
        while inx < len(text):
            # 只要当前元素不等于&,就将当前元素直接追加到栈中，继续遍历
            while inx < N and text[inx] != '&':
                stack.append(text[inx])
                inx += 1
            # 如果当前元素为&,记录该位置的元素，继续遍历，直到末尾或者找到;为止
            begin = inx
            while inx < N and text[inx] != ";":
                inx += 1
            # 如果开始位置等于末尾，说明已经遍历到字符串末尾，直接结束循环
            if begin == N:
                break
            # 如果当前位置等于末尾，说明没有找到;，直接将当前位置到末尾的字符串追加到栈中
            elif inx == N:
                stack.append(text[begin:])
            # 如果找到;，在字典中获取元素，看元素是否存在，如果存在追加元素，不存在追加这部分值即可
            else:
                # 注意：如果进入该分支，说明inx为;所在位置的索引
                element = d.get(text[begin:inx + 1], None)
                if element:
                    stack.append(element)
                else:
                    stack.append(text[begin:inx + 1])
            # 索引后移
            inx += 1
        return ''.join(stack)


solution = Solution()
print(solution.entityParser(text="&amp;amp;amp;gt;"))
