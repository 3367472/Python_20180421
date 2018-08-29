# encoding: utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is not None and head.next is not None:
            memory_list = []
            p = head
            p_address = id(p)
            while p_address not in memory_list:
                if p.next is None:
                    return
                else:
                    memory_list.append(p_address)
                    p = p.next
                    p_address = id(p)
            return p
        return
