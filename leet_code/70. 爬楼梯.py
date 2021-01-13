class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        i = 2
        pre_stage = pre_pre_stage = 1
        while i <= n:
            cur_stage = pre_pre_stage + pre_stage
            pre_pre_stage = pre_stage
            pre_stage = cur_stage
            i += 1
        return pre_stage


solution = Solution()
print(solution.climbStairs(2))
print(solution.climbStairs(3))
print(solution.climbStairs(4))
print(solution.climbStairs(5))
print(solution.climbStairs(6))