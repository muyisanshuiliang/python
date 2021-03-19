#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1598. 文件夹操作日志搜集器.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/17 10:23   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
每当用户执行变更文件夹操作时，LeetCode 文件系统都会保存一条日志记录。
下面给出对变更操作的说明：
"../" ：移动到当前文件夹的父文件夹。如果已经在主文件夹下，则 继续停留在当前文件夹 。
"./" ：继续停留在当前文件夹。
"x/" ：移动到名为 x 的子文件夹中。题目数据 保证总是存在文件夹 x 。
给你一个字符串列表 logs ，其中 logs[i] 是用户在 ith 步执行的操作。
文件系统启动时位于主文件夹，然后执行 logs 中的操作。
执行完所有变更文件夹操作后，请你找出 返回主文件夹所需的最小步数 。

示例 1：
输入：logs = ["d1/","d2/","../","d21/","./"]
输出：2
解释：执行 "../" 操作变更文件夹 2 次，即可回到主文件夹

示例 2：
输入：logs = ["d1/","d2/","./","d3/","../","d31/"]
输出：3

示例 3：
输入：logs = ["d1/","../","../","../"]
输出：0

提示：
1 <= logs.length <= 103
2 <= logs[i].length <= 10
logs[i] 包含小写英文字母，数字，'.' 和 '/'
logs[i] 符合语句中描述的格式
文件夹名称由小写英文字母和数字组成
'''

# import lib
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # if len(logs) == 0:
        #     return 0
        # stack = []
        # for item in logs:
        #     if stack and item == '../':
        #         stack.pop()
        #     elif item in ['./', '../']:
        #         pass
        #     else:
        #         stack.append(item)
        # return len(stack)

        if len(logs) == 0:
            return 0
        res = 0
        for item in logs:
            if res != 0 and item == '../':
                res -= 1
            elif item in ['./', '../']:
                pass
            else:
                res += 1
        return res


solution = Solution()
# print(solution.minOperations(logs=["d1/", "d2/", "./", "d3/", "../", "d31/"]))
print(solution.minOperations(logs=["./", "../", "./"]))
