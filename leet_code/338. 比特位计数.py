#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   338. 比特位计数.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/3 15:40   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:
输入: 2
输出: [0,1,1]

示例 2:
输入: 5
输出: [0,1,1,2,1,2]

进阶:
给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。

'''

# import lib
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []

        # 解法一：将数字转换成二进制，然后对‘1’进行统计
        # for item in range(num + 1):
        #     result.append(bin(item).count('1'))
        # return result

        # 解法二：递归获取
        # def count(num):
        #     # 0数字包含1的位数是0
        #     if num == 0:
        #         return 0
        #     # 奇数包含1的位数是前一个偶数包含的数字+1，如：4——0100，5——0101
        #     if num % 2 == 1:
        #         return count(num - 1) + 1
        #     # 偶数（=2 * N）包含1的位数与N 包含的数字相等，，右移一位扩大2倍，如：3——0011，6——0110
        #     return count(num // 2)
        #
        # for i in range(num + 1):
        #     result.append(count(i))
        # return result

        # 解法四：记忆搜索
        # 例如：获取8中‘1’的数量时，会依次计算4->2->1->0，但是实际在之前已经对这些数据中‘1’的数量进行了计算，这样就存在重复计算，
        #      如果存在，直接返回即可，减少了重复计算量
        # result = [0] * (num + 1)
        #
        # def count(num):
        #     if num == 0:
        #         return 0
        #     if result[num] != 0:
        #         return result[num]
        #     if num % 2 == 1:
        #         res = count(num - 1) + 1
        #     else:
        #         res = count(num // 2)
        #     result[num] = res
        #     return res
        #
        # for i in range(num + 1):
        #     count(i)
        # return result

        # 解法四：动态规划
        # 偶数&1 = 0，奇数&1 = 1，
        result = [0] * (num + 1)
        for i in range(1, num + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result


solution = Solution()
# 0——0000
# 1——0001
# 2——0010
# 3——0011
# 4——0100
# 5——0101
# 6——0110
# 7——0111
# 8——1000
# 9——1001
# 10——1010
print(solution.countBits(10))
