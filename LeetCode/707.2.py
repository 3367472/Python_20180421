# encoding: utf-8
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.linkedlist = list()

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= len(self.linkedlist):
            return -1
        else:
            return self.linkedlist[index]

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.linkedlist.insert(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.linkedlist.append(val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if 0 <= index <= len(self.linkedlist):
            self.linkedlist.insert(index, val)

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if 0 <= index < len(self.linkedlist):
            self.linkedlist.pop(index)



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

r = MyLinkedList()
r.addAtHead(1)
r.addAtTail(3)
r.addAtIndex(1, 2)
print(r.get(1))
r.deleteAtIndex(1)
print(r.get(1))

r = MyLinkedList()
r.addAtHead(1)
r.addAtIndex(1, 2)
print(r.get(1))
print(r.get(0))
print(r.get(1))

r = MyLinkedList()
print(r.get(0))
print(r.addAtIndex(1, 2))
print(r.get(0))
print(r.get(1))
print(r.addAtIndex(0, 1))
print(r.get(0))
print(r.get(1))

r = MyLinkedList()
print(r.addAtHead(38))
print(r.addAtHead(45))
print(r.deleteAtIndex(2))
print(r.addAtIndex(1, 24))
print(r.addAtTail(36))
print(r.addAtIndex(3, 72))
print(r.addAtTail(76))
print(r.addAtHead(7))
print(r.addAtHead(36))
print(r.addAtHead(34))
print(r.addAtTail(91))
print(r.addAtTail(69))
print(r.addAtHead(37))
print(r.addAtTail(38))
print(r.addAtTail(4))
print(r.addAtHead(66))
print(r.addAtTail(38))
print(r.deleteAtIndex(14))
print(r.addAtTail(12))
print(r.addAtTail(32))
print(r.get(5))
print(r.addAtIndex(7, 5))
print(r.addAtHead(74))
print(r.get(7))
print(r.get(13))
print(r.addAtHead(11))
print(r.get(8))
print(r.addAtIndex(10, 9))
print(r.addAtTail(19))
print(r.addAtIndex(3, 76))
print(r.addAtHead(7))
print(r.addAtHead(37))
print(r.addAtHead(99))
print(r.get(10))
print(r.addAtHead(12))
print(r.addAtIndex(1, 20))
print(r.addAtTail(29))
print(r.addAtHead(42))
print(r.addAtIndex(21, 52))
print(r.get(11))
print(r.addAtTail(44))
print(r.addAtTail(47))
print(r.addAtIndex(6, 27))
print(r.addAtIndex(31, 85))
print(r.addAtHead(59))
print(r.addAtHead(57))
print(r.get(4))
print(r.addAtTail(99))
print(r.addAtIndex(13, 83))
print(r.addAtIndex(10, 34))
print(r.addAtHead(48))
print(r.deleteAtIndex(9))
print(r.addAtIndex(22, 64))
print(r.addAtHead(69))
print(r.deleteAtIndex(33))
print(r.addAtTail(5))
print(r.deleteAtIndex(18))
print(r.addAtTail(87))
print(r.addAtHead(42))
print(r.addAtTail(1))
print(r.addAtTail(35))
print(r.addAtHead(31))
print(r.addAtTail(67))
print(r.addAtIndex(36, 46))
print(r.deleteAtIndex(23))
print(r.addAtHead(64))
print(r.addAtHead(81))
print(r.addAtHead(29))
print(r.addAtTail(50))
print(r.get(23))
print(r.addAtIndex(36, 63))
print(r.addAtTail(8))
print(r.addAtTail(19))
print(r.addAtTail(98))
print(r.deleteAtIndex(22))
print(r.get(28))
print(r.addAtHead(42))
print(r.get(24))
print(r.get(34))
print(r.addAtTail(32))
print(r.deleteAtIndex(25))
print(r.addAtTail(53))
print(r.addAtIndex(55, 76))
print(r.addAtHead(38))
print(r.addAtIndex(23, 98))
print(r.addAtTail(27))
print(r.get(18))
print(r.addAtIndex(44, 27))
print(r.addAtIndex(16, 8))
print(r.addAtHead(70))
print(r.addAtHead(15))
print(r.get(9))
print(r.get(27))
print(r.get(59))
print(r.addAtIndex(40, 50))
print(r.addAtHead(15))
print(r.addAtIndex(11, 57))
print(r.addAtHead(80))
print(r.addAtTail(50))
print(r.addAtIndex(23, 37))
print(r.get(12))
