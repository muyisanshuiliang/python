class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.upper() == word or word.lower() == word or word.title() == word


solution = Solution()
print(solution.detectCapitalUse("USA"))
print(solution.detectCapitalUse("Usa"))
