from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # merge sort 해보자.
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge_two_list(l1, l2):
            if l1 and l2:
                if l1.val > l2.val:
                    l1, l2 = l2, l1
                l1.next = merge_two_list(l1.next, l2)
            return l1 or l2

        if not (head and head.next):
            return head

        half, first, second = None, head, head

        while second and second.next:
            half, first, second = first, first.next, second.next.next
        half.next = None

        left = self.sortList(head)
        right = self.sortList(first)

        return merge_two_list(left, right)

    # python 내장 sort
    # def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head:
    #         node = head
    #         temp_list = []
    #         while node:
    #             temp_list.append(node.val)
    #             node = node.next
    #         temp_list.sort()
    #
    #         head = ListNode(temp_list[0])
    #         test_node = head
    #         for tt in temp_list[1:]:
    #             test_node.next = ListNode(tt)
    #             test_node = test_node.next
    #
    #     return head

sol = Solution()


sol.sortList([4,2,1,3])