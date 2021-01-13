class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return True
        if t is None or len(t) == 0:
            return False
        # 反转待查找的字符
        l = list(s)
        l.reverse()
        pre_index = len(t)
        # 在被查找的字符中循待查找的字符（从右向左查找）
        for item in l:
            # 查找并非全部查找，而是从上一次查找的字符串之前进行查找
            rfind = t[:pre_index].rfind(item)
            # 如果未找到，直接返回False
            if rfind == -1:
                return False
            # 如果找到，则修改被查找字符串的右端截止点
            pre_index = rfind
        # 循环完毕，说明查找到
        return True


s = "abc"
# s = ""
t = "ahbgdc"
solution = Solution()
print(solution.isSubsequence(s, t))
