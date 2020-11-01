class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.head=None

    def traverse(self,head):
        if head:
            print(head.value)
            self.traverse(head.left)
            self.traverse(head.right)

t=Tree()
t.head=Node(1)
t.head.left=Node(2)
t.head.right=Node(3)
t.head.left.left=Node(4)
t.head.left.right=Node(5)
t.head.right.left=Node(6)
t.head.right.right=Node(7)
t.traverse(t.head)

    #        1
    #      /   \
    #     /     \
    #    2       3
    #   / \     / \
    #  /   \   /   \
    # 4     5 6     7