"""
如果字符串 s 中 不存在 两个不同字符 频次 相同的情况，就称 s 是 优质字符串 。
给你一个字符串 s，返回使 s 成为 优质字符串 需要删除的 最小 字符数。
字符串中字符的 频次 是该字符在字符串中的出现次数。例如，在字符串 "aab" 中，'a' 的频次是 2，而 'b' 的频次是 1 。

示例 1：
输入：s = "aab"
输出：0
解释：s 已经是优质字符串。

示例 2：
输入：s = "aaabbbcc"
输出：2
解释：可以删除两个 'b' , 得到优质字符串 "aaabcc" 。
另一种方式是删除一个 'b' 和一个 'c' ，得到优质字符串 "aaabbc" 。

示例 3：
输入：s = "ceabaacb"
输出：2
解释：可以删除两个 'c' 得到优质字符串 "eabaab" 。
注意，只需要关注结果字符串中仍然存在的字符。（即，频次为 0 的字符会忽略不计。）
 
提示：
1 <= s.length <= 105
s 仅含小写英文字母
"""


class Solution:
    def minDeletions(self, s: str) -> int:
        nums = [s.count(chr(97 + i)) for i in range(26)]
        nums.sort(reverse=True)
        print(nums)
        # 记录当前数量的字符是否存在元素
        res = {}
        count = 0
        for item in nums:
            number_exist = res.get(item, False)
            # 如果不存在元素，直接记录当前元素的数量
            if not number_exist:
                res[item] = True
            else:
                # 如果存在元素则继续向下查找，直到找到不存在的数字为止
                while item > 0:
                    item -= 1
                    count += 1
                    number_exist = res.get(item, False)
                    if not number_exist:
                        res[item] = True
                        break
        return count


print(Solution().minDeletions(s="ceabaacb"))
print(Solution().minDeletions(s="aaabbbcc"))
print(Solution().minDeletions(s="aab"))
print(Solution().minDeletions(s="abcabc"))
