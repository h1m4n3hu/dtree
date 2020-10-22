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
            print("     ",node.value)
            for i in l:print(i.value,end=" ")
            if node.right:
                l.append(node.right)
                for i in l:print(i.value,end=" ")
            if node.left:
                l.append(node.left)
                for i in l:print(i.value,end=" ")
            print("----------------------")

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

    def max(self):
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
        m=0
        while s2:
            k=s2.pop()
            if k.value>m:
                m=k.value
            else:pass
        print(m)

    def post_find(self,n):
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
        m=0
        while s2:
            k=s2.pop()
            if k.value==n:
                break
            m+=1
        print(m)

    def in_find(self,n):
        var=0
        k=self.root
        while True:
            if k:
                l.append(k)
                k=k.left
            elif l:
                k=l.pop()
                if k.value==n:
                    break
                var+=1
                k=k.right
            else:
                break
        print(var)

    def pre_find(self,n):
        k=self.root
        l1=[]
        l2=[]
        var=0
        l1.append(k)
        while l1:
            k=l1.pop()
            l2.append(k)
            if k.left:
                l1.append(k.left)
            if k.right:
                l1.append(k.right)
        while l2:
            k=l2.pop()
            if k.value==n:
                break
            var+=1
        print(var)

    def in_pre_post(self,ino,pre,gap):
        gap=gap-3
        for i in range(len(ino)):
            if ino[i]==pre[0]:
                self.in_pre_post(ino[0:i],pre[1:],gap)
                print("  "*gap,ino[i])
                self.in_pre_post(ino[i+1:],pre[len(ino[0:i])+1:],gap)
                #print(ino[0:i],ino[i],ino[i+1:])

    #no of levels in a binary tree
    def height(self,head):
        if not head:
            return 0
        return 1+max(self.height(head.left),self.height(head.right))

    #no of nodes in a binary tree
    def size(self,head):
        if not head:
            return 0
        return 1+self.size(head.left)+self.size(head.right)

    def diameter(self,k):
        if k is None:
            return 0
        else:
            lt = self.height(k.left)
            rt = self.height(k.right)
            return 1+lt+rt

    #leaves of a tree
    def leaves(self,k):
        if not k.right or not k.left:
            print(k.value,end=" ")
        if k.left:
            self.leaves(k.left)
        if k.right:
            self.leaves(k.right)

    def boundary(self):
        k=j=i=self.root
        print(self.root.value,end=" ")
        while k.left.left:
            print(k.left.value,end=" ")
            k=k.left
        while j.right.right:
            print(j.right.value,end=" ")
            j=j.right
        self.leaves(i)

    #level order traversal reversal
    def rev_level(self):
        l2=[]
        k=self.root
        l.append(k)
        while len(l)>0:
            k=l.pop(0)
            l2.append(k)
            if k.right:
                l.append(k.right)
            if k.left:
                l.append(k.left)
        l2.reverse()
        for i in l2:print(i.value)

    #nodes at a level k
    def dist(self,head,k):
        if head is None:
            return
        if k==0:
            print(head.value)
        else:
            self.dist(head.left,k-1)
            self.dist(head.right,k-1)

    def possible_paths(self,head,st=""):
        if head:
            st+=str(head.value)
        if head is None:
            print(st)
        else:
            self.possible_paths(head.left,st)
            self.possible_paths(head.right,st)

    def path_of_a_leaf(self,head,leaf,st=""):
        if head:
            st += str(head.value)
        if head is None:
            if int(st[-1])==leaf:
                print(st)
        else:
            self.path_of_a_leaf(head.left,leaf,s)
            self.path_of_a_leaf(head.right,leaf,s)

    def a_leaf(self,head,value):
        if head:
            if head.left.value == value or head.right.value == value:
                print(head.value)
            self.a_leaf(head.left,value)
            self.a_leaf(head.right,value)

    def subtrees(self,head):
        if head:
            print(self.pre_traversal(head,""))
            self.subtrees(head.left)
            self.subtrees(head.right)



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
t.subtrees(t.root)