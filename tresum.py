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

    def chilsum(self,head):
        if head and head.right and head.left:
            print(head.value==head.right.value+head.left.value)
            self.chilsum(head.left)
            self.chilsum(head.right)

    def levelof(self,root,val,lev=1):
        if root:
            if root.value==val:
                self.num+=lev
            self.levelof(root.left,val,lev+1)
            self.levelof(root.right,val,lev+1)
        return self.num

    def unfulltree(self,head):
        if head:
            if not head.left and head.right or not head.right and head.left:
                print(head.value)
            self.unfulltree(head.left)
            self.unfulltree(head.right)

    def nosibling(self,head):
        if head:
            if head.left and not head.right:
                print(head.left.value)
            if head.right and not head.left:
                print(head.right.value)
            self.nosibling(head.left)
            self.nosibling(head.right)

    def lvl_of_nodes(self,head,l):
        if head:
            print(head.value,"is at level",l)
            self.lvl_of_nodes(head.left,l+1)
            self.lvl_of_nodes(head.right,l+1)

    def cousins(self,head,value,level):
        if head:
            if level==2:
                print(head.value)
            self.cousins(head.left,value,level+1)
            self.cousins(head.right,value,level+1)

    def root2leaf(self):
        pass

t=Tree()
t.root=Node(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.right.left=Node(6)
t.root.right.right=Node(7)
t.cousins(t.root,4,1)