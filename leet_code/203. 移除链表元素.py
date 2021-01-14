# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sentinel.next


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
# l7 = ListNode(7)
# l6.next = l7
Solution().removeElements(l1, 6)
