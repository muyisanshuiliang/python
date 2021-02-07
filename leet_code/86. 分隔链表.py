#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   86. 分隔链表.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/7 14:07   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。

示例：
输入：head = 1->4->3->2->5->2, x = 3
输出：1->2->2->4->3->5

'''

# import lib
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p = less = ListNode(0)
        q = more = ListNode(0)

        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                more.next = head
                more = more.next
            head = head.next

        more.next = None
        less.next = q.next
        return p.next


