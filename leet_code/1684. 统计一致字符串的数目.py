#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1684. 统计一致字符串的数目.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/24 16:33   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，
就称这个字符串是 一致字符串 。请你返回 words 数组中 一致字符串 的数目。

示例 1：
输入：allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
输出：2
解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。

示例 2：
输入：allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
输出：7
解释：所有字符串都是一致的。

示例 3：
输入：allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
输出：4
解释：字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。

提示:
1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
allowed 中的字符 互不相同 。
words[i] 和 allowed 只包含小写英文字母。
'''

# import lib
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int result = 0;
        //使用一个数组记录allowed 包含的字符，数组定位，效率较高
        int[] allow = new int[26];
        char[] chars = allowed.toCharArray();
        for (char aChar : chars) {
            allow[aChar - 'a'] = 1;
        }
        for (String word : words) {
            char[] arr = word.toCharArray();
            int index = 0;
            int length = arr.length;
            for (; index < length; index++) {
                //如果这个字符没有在allowed 中，直接结束
                if (allow[arr[index] - 'a'] == 0) {
                    break;
                }
            }
            //如果相等说明这个字符有判断到最后，结果加1
            if (index == length) {
                result++;
            }
        }
        return result;
    }
}
        :param allowed:
        :param words:
        :return:
        """
        res = len(words)
        for item in words:
            for item_s in item:
                # 逆向思维
                if item_s not in allowed:
                    res -= 1
                    break
        return res


solution = Solution()
print(solution.countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]))
