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

    def morris_post(self):
        k=self.root
        while k:
            if k.right:
                pre=k.right
                while pre.left and pre.left!=k:
                    pre=pre.left
                if pre.left is None:
                    yield k.value
                    pre.left=k
                    k=k.right
                else:
                    pre.left=None
                    k=k.left
            else:
                yield k.value
                k=k.left

    def morris_pre(self):
        k=self.root
        while k:
            if k.left:
                pre=k.left
                while pre.right and pre.right!=k:
                    pre=pre.right
                if pre.right is None:
                    yield k.value
                    pre.right=k
                    k=k.left
                else:
                    pre.right=None
                    k=k.right
            else:
                yield k.value
                k=k.right

    def printSpiral(self):
        s1=[]
        s2=[]
        s1.append(self.root)
        while s1 or s2:
            while s1:
                k=s1.pop(0)
                print(k.value,end=" ")
                s2.append(k.left)
                s2.append(k.right)
            print("\n")
            while s2:
                k=s2.pop(0)
                print(k.value,end=" ")
                s1.append(k.left)
                s1.append(k.right)
            print("\n")

    def rev_lev(self):
        l=[]
        ll=[]
        k=self.root
        l.append(k)
        while l:
            k=l.pop(0)
            ll.append(k.value)
            if k.right:l.append(k.right)
            if k.left:l.append(k.left)
        for i in reversed(ll):
            print(i)

    def specific_order(self):   #1234756....4 7 5 6....u see that?
        k=self.root
        l1=[]
        m=k.left
        l2=[]
        n=k.right
        print(k.value)
        l1.append(m)
        l2.append(n)
        while l1 or l2:
            mm=l1.pop(0)
            nn=l2.pop(0)
            print(mm.value)
            print(nn.value)
            if mm.left:l1.append(mm.left)
            if nn.left:l2.append(nn.right)
            if mm.right:l1.append(mm.right)
            if nn.right:l2.append(nn.left)

    def height(self,head):
        if not head:
            self.num+=1
            print(self.num)
            return 0
        return 1+max(self.height(head.left),self.height(head.right))

t=Tree()
t.root=Node(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.right.left=Node(6)
t.root.right.right=Node(7)
t.height(t.root)