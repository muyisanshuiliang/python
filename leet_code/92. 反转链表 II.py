#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   92. 反转链表 II.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/19 9:48   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

示例 1：
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]

示例 2：
输入：head = [5], left = 1, right = 1
输出：[5]

提示：
链表中节点数目为 n
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

进阶： 你可以使用一趟扫描完成反转吗？
'''


# import lib

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        stack = []
        temp = self
        while temp:
            stack.append(temp.val)
            temp = temp.next
        return stack


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        count = 1
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        # 左边第二个节点的前节点是 [1->2->3->4->5] pre = 1 -> 2 -> 3 -> 4 -> 5
        while pre.next and count < left:
            pre = pre.next
            count += 1
        cur = pre.next  # 2
        # 头插法的尾指针
        tail = cur  # 2
        while cur and count <= right:
            # 保存下一个节点，作为下一次节点的当前节点（操作节点）
            nxt = cur.next
            # 将当前节点移动到pre节点之后，修改当前节点的下一个节点
            cur.next = pre.next
            # 修改pre节点的下一个节点为当前节点
            pre.next = cur
            # 尾指针指向当前节点的下一个节点
            tail.next = nxt
            # 修改当前节点的指向
            cur = nxt
            count += 1
        return dummy.next


node_1 = ListNode(1)
node_2 = ListNode(2)
node_1.next = node_2
node_3 = ListNode(3)
node_2.next = node_3
node_4 = ListNode(4)
node_3.next = node_4
node_5 = ListNode(5)
node_4.next = node_5
print(Solution().reverseBetween(node_1, left=2, right=4))
