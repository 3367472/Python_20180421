# encoding: utf-8
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
        if head is not None and head.next is not None:
            odd_tail = head
            even_head = head.next
            even_tail = head.next
            while even_tail and even_tail.next:
                odd_tail.next = even_tail.next
                temp = even_tail.next.next
                odd_tail = odd_tail.next
                odd_tail.next = even_head
                even_tail.next = temp
                even_tail = even_tail.next
        return head






