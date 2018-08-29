# encoding: utf-8
# 这个方法可行么？
# case 1
# [1,2,3,4,5,6->3]
# slow = 1 2 3 4 5
# fast = 1 3 5 3 5
# slow == fast break
# slow = 5 6 3
# head = 1 2 3
####################
# case 2
# [1,2,3,4,5,6,7->3]
# slow = 1 2 3 4 5 6
# fast = 1 3 5 7 4 6
# slow == fast break
# slow = 6 7 3
# head = 1 2 3
####################
# case 3
# [1,2,3,4,5,6,7->4]
# slow = 1 2 3 4 5 6 7 4 5
# fast = 1 3 5 7 5 7 5 7 5
# slow == fast break
# slow = 5 6 7 4
# head = 1 2 3 4
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
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head
