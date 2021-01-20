"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        stack = []
        temp_root = root
        while True:
            stack.append(temp_root)
            if not self.is_leaf(temp_root):
                temp_root = temp_root.left
            else:
                break

        print()

    def is_leaf(self, node: TreeNode) -> bool:
        return not node.left and node.left is None


root = TreeNode(5)

left = TreeNode(4)
right = TreeNode(8)
root.left = left
root.right = right

left_left = TreeNode(11)
right_left = TreeNode(13)
right_right = TreeNode(4)
left.left = left_left
right.left = right_left
right.right = right_right

left_left_left = TreeNode(7)
left_left_right = TreeNode(2)
left.left.left = left_left_left
left.left.right = left_left_right

right_right_left = TreeNode(5)
right_right_right = TreeNode(1)
right.right.left = right_right_left
right.right.right = right_right_right

# print(Solution().pathSum(root, 22))

print(10 ** 2)
