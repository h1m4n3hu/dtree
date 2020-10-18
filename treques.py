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

    def preorder_iter(self):
        l.append(self.root)
        while len(l)>0:
            node=l.pop()
            print(node.value)
            if node.right:
                l.append(node.right)
            if node.left:
                l.append(node.left)

    def postorder_iter(self):
        s1=[]
        s2=[]
        s1.append(self.root)
        while s1:
            node=s1.pop()
            s2.append(node)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        while s2:
            node=s2.pop()
            print(node.value)

    def sum(self):
        sum=0
        l.append(self.root)
        while l:
            k=l.pop()
            sum+=k.value
            if k.right:
                l.append(k.right)
            if k.left:
                l.append(k.left)
        print(sum)

    def sum_left(self):
        sum=0
        k=self.root
        while True:
            if k:
                l.append(k)
                k=k.left
                if k:
                    sum+=k.value
            elif l:
                k=l.pop()
                k=k.right
            else:
                break
        print(sum)

t=Tree(Node(1))
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.right.left=Node(6)
t.root.right.right=Node(7)
#t.preorder_iter()   #1 2 4 5 3 6 7
#t.inorder_iter()    #4 2 5 1 6 3 7
#t.postorder_iter()  #4 5 2 6 7 3 1
t.sum_left()