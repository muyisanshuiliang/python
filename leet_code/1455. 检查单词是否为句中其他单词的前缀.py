class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        split = sentence.split(' ')
        if not searchWord:
            return -1
        for item_inx, item_val in enumerate(split, 1):
            if item_val.startswith(searchWord):
                return item_inx
        return -1


sentence = "i love eating burger"
searchWord = "burg"
split = sentence.split(' ')
# 下标的起始位置从1开始计算
for item_inx, item_val in enumerate(split, 1):
    print('{} = {}'.format(item_inx, item_val))
solution = Solution()
print(solution.isPrefixOfWord(sentence, searchWord))
