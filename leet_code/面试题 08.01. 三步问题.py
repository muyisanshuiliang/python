class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        i = 2
        pre_stage = pre_pre_stage = 1
        pre_pre_pre_stage = 0
        while i <= n:
            cur_stage = (pre_pre_stage + pre_stage + pre_pre_pre_stage) % 1000000007
            pre_pre_pre_stage = pre_pre_stage
            pre_pre_stage = pre_stage
            pre_stage = cur_stage
            i += 1
        return pre_stage


solution = Solution()
print(solution.waysToStep(2))
print(solution.waysToStep(3))
print(solution.waysToStep(4))
print(solution.waysToStep(5))
print(solution.waysToStep(6))
print(solution.waysToStep(7))
