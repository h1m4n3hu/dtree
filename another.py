lst=[1,2,3,5,8,13]
def fibb(lst):
    if lst[2]:
        if lst[0]+lst[1]==lst[2]:
            print(lst[0],lst[1],lst[2])

    if len(lst)>3:
        fibb(lst[1:])

fibb(lst)







# i=0
# while i<5:
#     print(i)
#     i+=1




































class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self,root):
        self.root=root
        self.sum=0
        self.s=0

    def children_sum(self,head):
        k=head
        if k and k.right and k.left:
            if k.left.value+k.right.value==k.value:
                print(k.left.value,k.right.value,k.value)

        if k.left:
            self.children_sum(k.left)

        if k.right:
            self.children_sum(k.right)

    #       9
    #      / \
    #     2   7
    #    /\  / \
    #   1 1  3  4











t=Tree(Node(9))
t.root.left=Node(2)
t.root.right=Node(7)
t.root.left.left=Node(1)
t.root.left.right=Node(1)
t.root.right.left=Node(3)
t.root.right.right=Node(4)
t.children_sum(t.root)



