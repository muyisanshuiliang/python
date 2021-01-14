"""
给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

示例 1:
输入：s = "egg", t = "add"
输出：true

示例 2：
输入：s = "foo", t = "bar"
输出：false

示例 3：
输入：s = "paper", t = "title"
输出：true
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 逐个循环字符串的每个元素首次出现的位置是相等的
        # return all(s.index(s[i]) == t.index(t[i]) for i in range(len(s)))

        # s2t, ts2 = {}, {}
        # # 依次对s,t中的元素进行遍历
        # for item in range(len(s)):
        #     s_item = s[item]
        #     t_item = t[item]
        #     """
        #     s2t.get(s_item, None) != t_item：从s的字典中获取值，如果该值与当前t的遍历值，不相等，说明不是重构
        #     """
        #     bs = s2t.__contains__(s_item) and s2t.get(s_item, None) != t_item
        #     bt = ts2.__contains__(t_item) and ts2.get(t_item, None) != s_item
        #     if bs or bt:
        #         return False
        #     """
        #     s字典中当前元素映射的值是t的当前元素
        #     t字典中当前元素映射的值是s的当前元素
        #     """
        #     s2t[s_item] = t_item
        #     ts2[t_item] = s_item
        # return True

        d_dict = {}
        n = len(s)
        for i in range(n):
            # 如果s的映射字典中没有当前元素
            if s[i] not in d_dict:
                # 如果t的当前元素已经在s字典中了，那么该映射关系不成立，返回false
                if t[i] in list(d_dict.values()):
                    return False
                else:
                    # 在字典中添加映射关系
                    d_dict[s[i]] = t[i]
            # 如果s的映射字典中有当前元素，判断当前元素是否与t的当前元素一致，不一致就返回False
            else:
                if d_dict[s[i]] != t[i]:
                    return False
        return True


print(Solution().isIsomorphic(s="egg", t="add"))
