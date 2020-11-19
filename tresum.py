class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None
        self.num=0

    def traverse(self,head):
        if head:
            print(head.value)
            self.traverse(head.left)
            self.traverse(head.right)


t=Tree()
t.root=Node(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.right.left=Node(6)
t.root.right.right=Node(7)
t.height(t.root)