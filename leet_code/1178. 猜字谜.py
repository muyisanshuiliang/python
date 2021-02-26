#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1178. 猜字谜.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/26 9:40   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。
字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：
单词 word 中包含谜面 puzzle 的第一个字母。
单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；
而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。
返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。

示例：
输入：
words = ["aaaa","asas","able","ability","actt","actor","access"],
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
输出：[1,1,3,2,4,0]
解释：
1 个单词可以作为 "aboveyz" 的谜底 : "aaaa"
1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"
3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"
2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"
4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"
没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。
 
提示：
1 <= words.length <= 10^5
4 <= words[i].length <= 50
1 <= puzzles.length <= 10^4
puzzles[i].length == 7
words[i][j], puzzles[i][j] 都是小写英文字母。
每个 puzzles[i] 所包含的字符都不重复。
'''

# import lib
import collections
from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        freq = collections.Counter()
        # 获取相同答案的解集和，只要字符相等，不管数量是否相等都是同一个解集
        for word in words:
            mask = 0
            for c in word:
                # 任何数与本身、0异或都是本身，所以一个字符无论出现都少次都不会影响mask的值
                mask |= 1 << (ord(c) - ord('a'))
            # 将解集数量放到字典中
            freq[mask] += 1
        res = []
        for puzzle in puzzles:
            total = 0
            # 获取谜面的所有子集
            subsets = self.subsets(puzzle[1:])
            for perm in subsets:
                # 必须包含首字母，所以所有的子集+首字母才是谜底
                mask = 1 << (ord(puzzle[0]) - ord('a'))
                for c in perm:
                    mask |= 1 << (ord(c) - ord('a'))
                # 最后查看mask在字典中是否存在，如果有，则返回对应的数量，否则返回0
                total += freq[mask]
            res.append(total)
        return res

    def subsets(self, words: List[int]) -> List[List[int]]:
        res = [""]
        for i in words:
            res = res + [i + word for word in res]
        return res


solution = Solution()
# print(solution.findNumOfValidWords(words=["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
#                                    puzzles=["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]))

print(solution.findNumOfValidWords(["apple", "pleas", "please"],
                                   ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"]))

print(1 << ord('p') - ord('a'))

mask = 0 | ord('c') - ord('a')
print(mask)
mask |= ord('d') - ord('a')
print(mask)
mask |= ord('c') - ord('a')
print(mask)
