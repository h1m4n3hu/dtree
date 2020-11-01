class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.head=None
        self.i=0

    def traverse(self,head):
        if head:
            print(head.value,end=" ")       #head
            self.traverse(head.left)        #left
            self.traverse(head.right)       #right

    def height(self,head):
        if head is None:
            return 0
        lheight=self.height(head.left)
        rheight=self.height(head.right)
        return 1+max(lheight,rheight)

    def diameter(self,head):
        if head is None:
            return 0
        lheight=self.height(head.left)
        rheight=self.height(head.right)
        return 1+lheight+rheight

    def size(self,head):
        if head:
            self.i+=1
            self.size(head.left)        #left
            self.size(head.right)       #right
        return self.i

t=Tree()
t.head=Node(1)
t.head.left=Node(2)
t.head.right=Node(3)
t.head.left.left=Node(4)
t.head.left.right=Node(5)
t.head.right.left=Node(6)
t.head.right.right=Node(7)
print(t.size(t.head))

    #        1
    #      /  \
    #     /    \
    #    2      3
    #   / \    / \
    #  4   5  6   7
