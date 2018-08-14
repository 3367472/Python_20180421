# encoding: utf-8
class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def creatlist(n):
    if n <= 0:
        return False
    elif n == 1:
        return Node(1)
    else:
        root = Node(1)
        tmp = root
        for i in range(2, n + 1):
            tmp.next = Node(i)
            tmp = tmp.next
    return root


def printlist(head):
    p = head
    while p != None:
        print(p.value)
        p = p.next


def listlen(head):
    c = 0
    p = head
    while p != None:
        c = c + 1
        p = p.next
    return c


def insertlist(head, n):
    if n < 1 or n > listlen(head):
        return 0
    p = head
    for i in range(1, n - 1):
        p = p.next
    a = input('Enter a value:')
    t = Node(value=a)
    t.next = p.next
    p.next = t
    return head


def dellist(head, n):
    if n < 1 or n > listlen(head):
        return head
    elif n == 1:
        head = head.next
    else:
        p = head
        for i in range(1, n - 1):
            p = p.next
        q = p.next
        p.next = q.next
    return head


def main():
    print('Create a linklist:')
    head = creatlist(7)
    printlist(head)
    print('----------------------')

    n1 = int(input('Enter the index to insert'))
    insertlist(head, n1)
    printlist(head)
    print('---------------')

    n2 = int(input('Enter the index to delete'))
    dellist(head, n2)
    printlist(head)


if __name__ == "__main__":
    main()
二叉树：

class BTNode(object):
    """docstring for BTNode"""

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# insert element
def InsertElementBinaryTree(root, node):
    if root:
        if node.data < root.data:
            if root.leftChild:
                InsertElementBinaryTree(root.leftChild, node)
            else:
                root.leftChild = node
        else:
            if root.rightChild:
                InsertElementBinaryTree(root.rightChild, node)
            else:
                root.rightChild = node
    else:
        return 0


# init a tree
def InitBinaryTree(dataSource, length):
    root = BTNode(dataSource[0])

    for x in range(1, length):
        node = BTNode(dataSource[x])
        InsertElementBinaryTree(root, node)
    return root
    print('Done...')


# pre-order
def PreorderTraversalBinaryTree(root):
    if root:
        print('%d | ' % root.data, )
        PreorderTraversalBinaryTree(root.leftChild)
        PreorderTraversalBinaryTree(root.rightChild)


# in-order
def InorderTraversalBinaryTree(root):
    if root:
        InorderTraversalBinaryTree(root.leftChild)
        print('%d | ' % root.data, )
        InorderTraversalBinaryTree(root.rightChild)


# post-order
def PostorderTraversalBinaryTree(root):
    if root:
        PostorderTraversalBinaryTree(root.leftChild)
        PostorderTraversalBinaryTree(root.rightChild)
        print('%d | ' % root.data, )


# layer-order
def TraversalByLayer(root, length):
    stack = []
    stack.append(root)
    for x in range(length):
        node = stack[x]
        print('%d | ' % node.data, )
        if node.leftChild:
            stack.append(node.leftChild)
        if node.rightChild:
            stack.append(node.rightChild)


if __name__ == '__main__':
    dataSource = [3, 4, 2, 6, 7, 1, 8, 5]
    length = len(dataSource)
    BTree = InitBinaryTree(dataSource, length)
    print('****NLR:')
    PreorderTraversalBinaryTree(BTree)
    print('\n****LNR')
    InorderTraversalBinaryTree(BTree)
    print('\n****LRN')
    PostorderTraversalBinaryTree(BTree)
    print('\n****LayerTraversal')
    TraversalByLayer(BTree, length)
