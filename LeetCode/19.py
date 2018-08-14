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

        p = head
        count = 1
        while p.next:
            p = p.next
            count += 1

        pre = head
        cur = head
        if count == n:
            pre.val = pre.next.val
            pre.next = pre.next.next
        for _ in range(count - n):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        return head


r = Solution()
r.removeNthFromEnd(5)
