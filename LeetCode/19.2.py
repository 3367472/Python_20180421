# encoding: utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return

        p1 = head
        p2 = head

        for i in range(n):
            p1 = p1.next
            if not p1.next:
                p2.val = p2.next.val
                p2.next = p2.next.next
                return head
        while p1.next:
            p2 = p2.next
            p1 = p1.next
        p2.next = p2.next.next
        return head


r = Solution()
r.removeNthFromEnd(5)
