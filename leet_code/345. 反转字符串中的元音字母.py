"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1：
输入："hello"
输出："holle"

示例 2：
输入："leetcode"
输出："leotcede"
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        # def get_vowel(item: str) -> bool:
        #     vowel_dict = {
        #         'a': True,
        #         'e': True,
        #         'i': True,
        #         'o': True,
        #         'u': True,
        #         'A': True,
        #         'E': True,
        #         'I': True,
        #         'O': True,
        #         'U': True,
        #     }
        #     return vowel_dict.get(item, False)
        # s = list(s)
        # print(s)
        #
        # l_inx, r_inx = 0, len(s) - 1
        # while l_inx < r_inx:
        #     if not get_vowel(s[l_inx]):
        #         l_inx += 1
        #     if not get_vowel(s[r_inx]):
        #         r_inx -= 1
        #     if get_vowel(s[l_inx]) and get_vowel(s[r_inx]):
        #         s[l_inx], s[r_inx] = s[r_inx], s[l_inx]
        #         l_inx += 1
        #         r_inx -= 1
        # return ''.join(s)

        dic = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l = 0
        r = len(s) - 1
        ss = list(s)
        while l < r:
            if ss[l] in dic and ss[r] in dic:
                ss[l], ss[r] = ss[r], ss[l]
                l += 1
                r -= 1
            elif ss[l] not in dic:
                l += 1
            else:
                r -= 1
        return ''.join(ss)


print(Solution().reverseVowels('leetcode'))
