from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        if not l or not r or len(l) == 0 or len(r) == 0:
            return [False] * len(l) if len(l) >= len(r) else len(r)
        result = []
        for (item_l, item_r) in zip(l, r):
            temp = nums[item_l: item_r]
            temp.append(nums[item_r])
            temp.sort()
            result.append(len(set(temp[i + 1] - temp[i] for i in range(len(temp) - 1))) == 1)
        return result

        ans = []
        for i in range(len(l)):
            li = (nums[l[i]:r[i] + 1:])
            li.sort()
            ans.append(True if all((li[i] - li[i - 1]) == li[1] - li[0] for i in range(1, len(li))) else False)
        return ans


print(Solution().checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]))

print(Solution().checkArithmeticSubarrays(nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10], l=[0, 1, 6, 4, 8, 7],
                                          r=[4, 4, 9, 7, 9, 10]))


def f(x):
    return x * x


nums = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10]
print(list(map(f,nums)))
