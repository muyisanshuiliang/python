#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   328. 奇偶链表.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/7 14:22   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL

示例 2:
输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL

说明:
应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
'''


# import lib

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        str_val = str(self.val)
        temp = self.next
        while temp:
            str_val += '---->' + str(temp.val)
            temp = temp.next
        return str_val


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # if not head or not head.next:
        #     return head
        # # odd_head 奇数节点的头节点
        # # odd_tail 奇数节点的尾节点
        # # even_head 偶数节点的头节点
        # # even_tail 偶数节点的尾节点
        # even_head = even_tail = head
        # odd_head = odd_tail = head.next
        # temp = odd_head.next
        # index = 0
        # while temp:
        #     if index % 2 == 0:
        #         even_tail.next = temp
        #         even_tail = even_tail.next
        #     else:
        #         odd_tail.next = temp
        #         odd_tail = odd_tail.next
        #     index += 1
        #     temp = temp.next
        # # 偶数节点尾指针的下一个置空
        # odd_tail.next = None
        # # 奇数指针的下一个指向偶数指针的头节点
        # even_tail.next = odd_head
        # return even_head

        # 可以将奇数节点和偶数节点分离成奇数链表和偶数链表，然后将偶数链表连接在奇数链表之后，合并后的链表即为结果链表。原始链表的头节点 head 也是奇数链表的头节点以及结果链表的头节点，head 的后一个节点是偶数链表的头节点。令 evenHead = head.next，则 evenHead 是偶数链表的头节点。维护两个指针 odd 和 even 分别指向奇数节点和偶数节点，初始时 odd = head，even = evenHead。通过迭代的方式将奇数节点和偶数节点分离成两个链表，每一步首先更新奇数节点，然后更新偶数节点。全部节点分离完毕的条件是 even 为空节点或者 even.next 为空节点，此时 odd 指向最后一个奇数节点. 最后令 odd.next = evenHead，将偶数链表连接在奇数链表之后，即完成了奇数链表和偶数链表的合并，结果链表的头节点仍然是 head.
        if not head:
            return head

        even_head = head.next  # 相当于哨兵节点
        odd, even = head, even_head
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


node_1 = ListNode(0)
node_2 = ListNode(1)
node_1.next = node_2

node_3 = ListNode(2)
node_2.next = node_3

node_4 = ListNode(3)
node_3.next = node_4

node_5 = ListNode(4)
node_4.next = node_5

node_6 = ListNode(5)
node_5.next = node_6

node_7 = ListNode(6)
node_6.next = node_7

node_8 = ListNode(7)
node_7.next = node_8

node_9 = ListNode(8)
node_8.next = node_9

node_10 = ListNode(9)
node_9.next = node_10

print(Solution().oddEvenList(node_1))
