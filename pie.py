class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

l=[]
list_two=[]

class Tree:
    def __init__(self,root):
        self.root=root

    def lot(self):
        l.append(self.root)
        while l:
            k=l.pop(0)
            list_two.append(k.value)
            if k.right:
                l.append(k.right)
            if k.left:
                l.append(k.left)
        list_two.reverse()
        print(list_two)

t=Tree(Node(1))
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.right.left=Node(6)
t.root.right.right=Node(7)
#t.lot()     #1 2 3 4 5 6 7
t.lot()     #4 5 6 7 2 3 1





    #         1
    #        / \
    #       /   \
    #      2     3
    #     /\     /\
    #    4  5   6  7
