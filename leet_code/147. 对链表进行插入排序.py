"""
对链表进行插入排序。
插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

插入排序算法：
插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
 

示例 1：
输入: 4->2->1->3
输出: 1->2->3->4

示例 2：
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = str(self.val)
        temp = self.next
        while temp:
            result = result + '->' + str(temp.val)
            temp = temp.next
        return result


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        # if not head:
        #     return head
        #
        #     # 将节点放入数组
        # nodes = []
        # node = head
        # while node:
        #     nodes.append(node)
        #     node = node.next
        #
        # # 排序数组
        # nodes = sorted(nodes, key=lambda x: x.val)
        #
        # # 更新指针
        # for i in range(len(nodes) - 1):
        #     nodes[i].next = nodes[i + 1]
        # nodes[len(nodes) - 1].next = None
        #
        # return nodes[0]

        if not head:
            return head
        # 前指针
        pre = head
        # 当前指针
        cur = head.next
        # 判断当前指针是否为空
        while cur:
            # 如果前指针的值小于等于当前指针，当前指针直接后移
            if cur.val >= pre.val:
                pre = cur
                cur = cur.next
                continue
            # 如果当前指针的值小于头指针，则修改头指针
            if cur.val < head.val:
                pre.next = cur.next
                cur.next = head
                head = cur
                cur = pre.next
            # 判断入队
            else:
                temp = head
                while temp.next:
                    # 如果当前指针的值大于等于中间指针后面的值，中间指针后移继续查询
                    if cur.val >= temp.next.val:
                        temp = temp.next
                    else:
                        # 修改指针的指向
                        pre.next = cur.next
                        cur.next = temp.next
                        temp.next = cur
                        cur = pre.next
                        break
        return head


node_1 = ListNode(4)
node_2 = ListNode(2)
node_1.next = node_2
node_3 = ListNode(1)
node_2.next = node_3
node_4 = ListNode(3)
node_3.next = node_4
print(node_1)
print(Solution().insertionSortList(node_1))
