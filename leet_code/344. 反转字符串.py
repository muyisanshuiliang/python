"""
easy
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

示例 1：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]

示例 2：
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]

"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # l_index, r_index = 0, len(s) - 1
        # while l_index < r_index:
        #     if s[l_index] == s[r_index]:
        #         pass
        #     else:
        #         s[l_index], s[r_index] = s[r_index], s[l_index]
        #     l_index += 1
        #     r_index -= 1

        l = len(s) - 1
        for i in range(len(s) // 2):
            if s[i] != s[l]:
                s[i], s[l] = s[l], s[i]
            l -= 1
        print(s)


print(Solution().reverseString(["H", "a", "n", "n", "a", "h"]))
print(Solution().reverseString([]))

