# encoding: utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p and p.next:
            q = p.next
            p.next = p.next.next
            q.next = head
            head = q
        return head






