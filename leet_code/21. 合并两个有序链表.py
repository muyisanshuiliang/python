class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        result = temp = ListNode()
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        temp.next = l1 if l1 is not None else l2
        # if l1 is not None:
        #     temp.next = l1
        # if l2 is not None:
        #     temp.next = l2
        return result.next


l1_node_4 = ListNode(4)
l1_node_2 = ListNode(2, next=l1_node_4)
l1_node_1 = ListNode(1, next=l1_node_2)

l2_node_4 = ListNode(4)
l2_node_2 = ListNode(3, next=l2_node_4)
l2_node_1 = ListNode(1, next=l2_node_2)

solution = Solution()
print(solution.mergeTwoLists(l1_node_1, l2_node_1).__str__())
