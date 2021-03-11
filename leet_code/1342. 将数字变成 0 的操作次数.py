#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1342. 将数字变成 0 的操作次数.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/11 9:52   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。

示例 1：
输入：num = 14
输出：6
解释：
步骤 1) 14 是偶数，除以 2 得到 7 。
步骤 2） 7 是奇数，减 1 得到 6 。
步骤 3） 6 是偶数，除以 2 得到 3 。
步骤 4） 3 是奇数，减 1 得到 2 。
步骤 5） 2 是偶数，除以 2 得到 1 。
步骤 6） 1 是奇数，减 1 得到 0 。

示例 2：
输入：num = 8
输出：4
解释：
步骤 1） 8 是偶数，除以 2 得到 4 。
步骤 2） 4 是偶数，除以 2 得到 2 。
步骤 3） 2 是偶数，除以 2 得到 1 。
步骤 4） 1 是奇数，减 1 得到 0 。

示例 3：
输入：num = 123
输出：12
'''


# import lib
class Solution:
    def numberOfSteps(self, num: int) -> int:
        # res = 0
        # while num > 0:
        #     num = (num // 2) if num % 2 == 0 else (num - 1)
        #     res += 1
        # return res

        # 解法二：任何奇数&1都是1，偶数&1都是0
        # res = 0
        # while num > 0:
        #     if num & 1:
        #         num -= 1
        #     else:
        #         # 偶数//2，相当于右移一位
        #         num >>= 1
        #     res += 1
        # return res

        # 解法三：位操作
        # 获取当前整数的二进制数据
        s = bin(num)[2:]
        print(bin(num))
        print(s)
        print([int(i) for i in s])
        # 减一就是1的数量
        print(sum([int(i) for i in s]))
        # //2 就是除最高位外二进制数据的位数，0占1位，所以要除最高位
        print(len(s) - 1)
        # 计算步骤就是 减1 与 //2 操作步骤之和
        return len(s) + sum([int(i) for i in s]) - 1


solution = Solution()
print(solution.numberOfSteps(123))
