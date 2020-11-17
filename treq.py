class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

    def traverse(self,head):
        if head:
            print(head.value)
            self.traverse(head.left)
            self.traverse(head.right)

    def inord(self):
        l=[]
        k=self.root
        while True:
            if k:
                l.append(k)
                k=k.left
            elif l:
                last=l.pop()
                print(last.value)
                k=last.right
            else:
                break

    def morris_inord(self):
        k=self.root
        while k:
            if k.left:
                pre=k.left
                while pre.right and pre.right!=k:
                    pre=pre.right
                if pre.right is None:
                    pre.right=k
                    k=k.left
                else:
                    print(k.value,'i')
                    pre.right=None
                    k=k.right
            else:
                print(k.value)
                k=k.right

    def morris_preord(self):
        k=self.root
        while k:
            if k.left:
                pre=k.left
                while pre.right and pre.right!=k:
                    pre=pre.right
                if pre.right is None:
                    print(k.value,'i')
                    pre.right=k
                    k=k.left
                else:
                    pre.right=None
                    k=k.right
            else:
                print(k.value)
                k=k.right

t=Tree()
t.root=Node(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.right.left=Node(6)
t.root.right.right=Node(7)
t.morris_preord()