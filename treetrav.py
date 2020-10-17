class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

l=[]

class Tree:
    def __init__(self,root):
        self.root=root

    def pre_traversal(self,start,res):
        if start:
            res+=str(start.value)+" "
            res=self.pre_traversal(start.left,res)
            res=self.pre_traversal(start.right,res)
        return res

    def show(self):
        return self.pre_traversal(self.root,"")

    def inorder_iter(self):
        k=self.root
        l=[]
        while True:
            if k:
                l.append(k)
                k=k.left
            elif l:
                k=l.pop()
                print(k.value,end=" ")
                k=k.right
            else:
                break


t=Tree(Node(10))
t.root.left=Node(3)
t.root.right=Node(6)
t.root.left.left=Node(2)
t.root.left.right=Node(4)
t.root.right.left=Node(5)
t.root.right.right=Node(7)
#print(t.show())     #10 3 2 4 6 5 7
t.inorder_iter()