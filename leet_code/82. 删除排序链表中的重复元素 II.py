#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   82. 删除排序链表中的重复元素 II.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/25 9:32   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
返回同样按升序排列的结果链表。

示例 1：
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

示例 2：
输入：head = [1,1,1,2,3]
输出：[2,3]

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
        # 解法一：递归
        # # 如果head为空或者只有一个节点，说明不存在重复节点，返回当前head
        # if not head or not head.next:
        #     return head
        # # 如果当前节点和下一个节点不相等，当前节点保留，计算next的头节点
        # if head.val != head.next.val:
        #     head.next = self.deleteDuplicates(head.next)
        # else:
        #     # 如果相等，一直向下找，找到链表尾部或者与当前节点值不相等的节点为止
        #     move = head.next
        #     # 1 —> 2① -> 2② -> 3① -> 3② -> 3③ -> 4 -> 5
        #     # 循环结束，move = 4
        #     while move and head.val == move.val:
        #         move = move.next
        #     return self.deleteDuplicates(move)
        # return head

        # 解法二：迭代一次遍历
        # dummy 节点，也叫做 哑节点。它在链表的迭代写法中非常常见，因为对于本题而言，我们可能会删除头结点 head，
        # 为了维护一个不变的头节点，所以我们添加了 dummy，让dummy.next = head，这样即使 head 被删了，
        # 那么会操作 dummy.next 指向新的链表头部，所以最终返回的也是 dummy.next。
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            # 跳过当前的重复节点，使得cur指向当前重复元素的最后一个位置
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            # 1 —> 2① -> 2② -> 3① -> 3② -> 3③ -> 4 -> 5
            # pre = 1 —> 2① -> 2② -> 3① -> 3② -> 3③ -> 4 -> 5
            # cur = 2② -> 3① -> 3② -> 3③ -> 4 -> 5
            # 注意：这里判断的是节点是否相等，不是节点值是否相等
            # 如果相等，说明pre与cur之间没有与cur值相等的节点
            if pre.next == cur:
                # pre和cur之间没有重复节点，pre后移
                pre = pre.next
            else:
                # pre->next指向cur的下一个位置（相当于跳过了当前的重复元素）
                # 但是pre不移动，仍然指向已经遍历的链表结尾
                # pre = 1 -> 3① -> 3② -> 3③ -> 4 -> 5
                pre.next = cur.next
            # cur = 3① -> 3② -> 3③ -> 4 -> 5
            cur = cur.next
        return dummy.next

        # 方法三：利用计数，两次遍历
        # 这个做法忽略了链表有序这个性质，使用了两次遍历，第一次遍历统计每个节点的值出现的次数，
        # 第二次遍历的时候，如果发现 head.next 的 val 出现次数不是 1 次，则需要删除 head.next。
        # dummy = ListNode(0)
        # dummy.next = head
        # val_list = []
        # while head:
        #     val_list.append(head.val)
        #     head = head.next
        # counter = collections.Counter(val_list)
        # head = dummy
        # while head and head.next:
        #     if counter[head.next.val] != 1:
        #         head.next = head.next.next
        #     else:
        #         head = head.next
        # return dummy.next
