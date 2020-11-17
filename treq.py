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

    def morris(self):
        k=self.root
        while k:
            if k.left is None:
                yield k.value
                k=k.right
            else:
                pre=k.left
                while pre.right and pre.right!=k:
                    pre=pre.right
                if pre.right is None:
                    pre.right=k
                    k=k.left
                else:
                    pre.right=None
                    yield k.value
                    k=k.right

    def morri(self):
        k=self.root
        while k:
            if k.left is None:
                print(k.value)
                k=k.right
            else:
                while




t=Tree()
t.root=Node(4)
t.root.left=Node(2)
t.root.right=Node(5)
t.root.left.left=Node(1)
t.root.left.right=Node(3)
for i in t.morri():
    print(i)