# encoding: utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self):
        self.val = None
        self.next = None


class Solution:
    def __init__(self):
        self.cur_node = None

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    def add(self, data):
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    def print_ListNode(self, node):
        while node:
            print('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)


r = Solution()
l1 = ListNode()
l1 = r.add(1)
l1 = r.add(2)
r.print_ListNode(l1)
