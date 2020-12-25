class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

l=[]
s=""

class Tree:
    def __init__(self,root):
        self.root=root

    def indexer(self,root,hd,m):
        if root is None:
            return
        try:
            m[hd].append(root.value)
        except:
            m[hd]=[root.value]
        self.indexer(root.left,hd-1,m)
        self.indexer(root.right,hd+1,m)

    def vert(self,root):
        m=dict()
        hd=0
        self.indexer(root,hd,m)
        print(list(enumerate(sorted(m))))
        for index, value in enumerate(sorted(m)):
            for i in m[value]:
                print(i)

t=Tree(Node(1))
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.right.left=Node(6)
t.root.right.right=Node(7)
t.vert(t.root)