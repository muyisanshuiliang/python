#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   331. 验证二叉树的前序序列化.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/12 11:21   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。
     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #

例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。
给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。
每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。
你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。

示例 1:
输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
输出: true

示例 2:
输入: "1,#"
输出: false

示例 3:
输入: "9,#,#,1"
输出: false
'''


# import lib
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not preorder:
            return False
        # """
        # 解法一：栈的思想
        # 根据原理巧妙的利用栈的特性：前序遍历的有效的叶子节点顺序为：[!#,#,#]，这种视为有效的叶子节点，直接用 # 将其替换即可
        # 模拟一遍过程：
        # 9,3,4,#,# => 9,3,#，继续
        # 9,3,#,1,#,# => 9,3,#,# => 9,# ，继续
        # 9,#2,#,6,#,# => 9,#,2,#,# => 9,#,# => #，结束
        # """
        # stack = []
        # for node in preorder.split(','):
        #     stack.append(node)
        #     while len(stack) >= 3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
        #         stack.pop(), stack.pop(), stack.pop()
        #         stack.append('#')
        # return len(stack) == 1 and stack.pop() == '#'

        """
        解法二：出度和入度
        在一棵二叉树中： 
        每个空节点（ "#" ）会提供 0 个出度和 1 个入度。
        每个非空节点会提供 2 个出度和 1 个入度。
        进入第一个节点的遍历，默认入度值为1，而出度为0，
        """
        nodes = preorder.split(',')
        diff = 1
        for node in nodes:
            # 进入节点后：入度 -1
            diff -= 1
            # 因为此时还未进行子节点的遍历，如果此时出度值大于入度值，说明不是前序遍历，返回False
            if diff < 0:
                return False
            # 如果当前不是根节点，说明该节点有两个出度，否则只有入度，没有出度
            elif node != "#":
                diff += 2
        # 二叉树出入度相等
        return diff == 0


solution = Solution()
print(solution.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
