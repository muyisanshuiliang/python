class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # # 中间节点，记录
        pre = ListNode()
        pre.next = temp_head = head
        while temp_head and temp_head.next :
            pre.next = temp_head.next
            temp_head.next = pre.next.next
            pre.next.next = temp_head
            if head == temp_head:
                head = pre.next
            pre = temp_head
            temp_head = temp_head.next
        return head

        # dummyHead = ListNode(0)
        # dummyHead.next = head
        # temp = dummyHead
        # while temp.next and temp.next.next:
        #     node1 = temp.next
        #     node2 = temp.next.next
        #     temp.next = node2
        #     node1.next = node2.next
        #     node2.next = node1
        #     temp = node1
        # return dummyHead.next





# print(Solution().swapPairs([]))
l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
l3 = ListNode(3)
l2.next = l3
l4 = ListNode(4)
l3.next = l4
l5 = ListNode(5)
l4.next = l5
l6 = ListNode(6)
l5.next = l6
l7 = ListNode(7)
l6.next = l7
print(Solution().swapPairs(l1))
