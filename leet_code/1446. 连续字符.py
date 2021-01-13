import re


class Solution:
    def maxPower(self, s: str) -> int:
        return max(len(i.group()) for i in re.finditer(r'([a-z])\1*',s))


