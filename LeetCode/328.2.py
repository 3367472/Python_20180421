# encoding: utf-8
# 别人的第一名的算法，还没看懂
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        odd = ListNode(0)
        even = ListNode(0)
        cur1 = odd
        cur2 = even
        while head != None:
            cur1.next = head
            cur1 = head
            if head.next != None:
                cur2.next = head.next
                cur2 = head.next
                head = head.next.next
            else:
                head = head.next
        cur2.next = None
        cur1.next = even.next
        return odd.next






