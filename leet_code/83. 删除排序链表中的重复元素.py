#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   83. 删除排序链表中的重复元素.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/26 12:12   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
返回同样按升序排列的结果链表。

示例 1：
输入：head = [1,1,2]
输出：[1,2]

示例 2：
输入：head = [1,1,2,3,3]
输出：[1,2,3]

提示：
链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列
'''


# import lib

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        # 解法一：一次遍历，删除节点相同的节点
        # if not head:
        #     return head
        # pre, cur = head, head.next
        # while cur:
        #     if cur.val == pre.val:
        #         pre.next = cur.next
        #     else:
        #         pre = cur
        #     cur = cur.next
        # return head

        # 解法二：
        # #  1 —> 2① -> 2② -> 3① -> 3② -> 3③ -> 4 -> 5
        # # slow = fast = 1
        # slow = head
        # fast = head
        # while fast:
        #     if fast.val != slow.val:
        #         slow.next = fast
        #         slow = fast
        #     fast = fast.next
        #     slow.next = None
        # return head

        # 解法二：递归求解，终止条件，遍历到链表的末尾
        # if not head or not head.next:
        #     return head
        # head.next = self.deleteDuplicates(head.next)
        # return head if head.val != head.next.val else head.next

        # 解法三：递归求解，终止条件，遍历到链表的末尾
        if not head or not head.next:
            return head
        # 如果当前节点的和next节点的值不相等，保留当前节点，获取以next节点为头节点的新链表的头节点
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
        else:
            # 如果当前节点的和next节点的值相等，标记删除节点
            # 1 —> 2① -> 2② -> 3① -> 3② -> 3③ -> 4 -> 5
            # head = 3①,move = 3②
            move = head.next
            # 如果删除节点的next不为空并且删除节点next的值与当前节点的值相等，继续下移，直至不相等的节点出现
            while move.next and head.val == move.next.val:
                move = move.next
            # 如果删除节点的next不为空并且删除节点next的值与当前节点的值相等，继续下移，直至不相等的节点出现
            # 循环完成后 move = 3③,此时以move为头节点，来进行后续节点的判断，3①,3②两个节点已被抛弃
            return self.deleteDuplicates(move)
        return head

        # 解法四：利用set集合求解，删除多余的节点
        # if not head or not head.next:
        #     return head
        # val_set = set()
        # val_set.add(head.val)
        # root = ListNode(0)
        # root.next = head
        # # 如果当前节点或当前节点的.next为空，说明已经到链表尾部
        # while head and head.next:
        #     # 如果该值已出现在集合中了，head.next指向 head.next.next
        #     if head.next.val in val_set:
        #         head.next = head.next.next
        #     # 如果该值未出现在集合中，将当前节点的值添加到set中，将head指针下移
        #     else:
        #         head = head.next
        #         val_set.add(head.val)
        # return root.next
