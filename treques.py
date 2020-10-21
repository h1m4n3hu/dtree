class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

l=[]

class Tree:
    def __init__(self,root):
        self.root=root
        self.sum=0
        self.s=""

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
        s=0
        l.append(self.root)
        while l:
            k=l.pop()
            s+=k.value
            if k.right:
                l.append(k.right)
            if k.left:
                l.append(k.left)
        return s

    def sum_left(self):
        s=0
        l.append(self.root)
        while len(l)>0:
            node=l.pop()
            if node.right:
                l.append(node.right)
            if node.left:
                l.append(node.left)
                s+=node.left.value
        return s

    def level_travel(self):
        l.append(self.root)
        l2=[]
        #res=""
        while l:
            #res+=str(l[-1].value)+" "
            l2.append(l[-1].value)
            node=l.pop()
            if node.left:
                l.insert(0,node.left)
            if node.right:
                l.insert(0,node.right)
        print(l2)

    def leaf_sum(self,node):
        if node.left or node.right:
            if node.left.value==2 or node.right.value==2:
                self.sum+=node.value
        if node.left:
            self.leaf_sum(node.left)
        if node.right:
            self.leaf_sum(node.right)
        print(self.sum)

    def leaves(self,head):
        if head:
            pass
        if head.left:
            self.leaves(head.left)
        else:
            self.sum+=head.value
            print(head.value)
        if head.right:
            self.leaves(head.right)
        #return self.sum

    def inorder_list(self,head):
        if head.left:
            self.inorder_list(head.left)
        if head.value:
            l.append(head)
        if head.right:
            self.inorder_list(head.right)
        return l

    def inorder_successor(self,value):
        l=self.inorder_list(self.root)
        j=0
        for i in l:
            if i.value==value:
                print(l[j+1].value)
            j+=1

    def height(self,head):
        if head is None:
            return 0
        else:
            lt=self.height(head.left)
            rt=self.height(head.right)
            return 1+max(lt,rt)

    def spiral_level(self):
        l.append(self.root)
        while l:
            k=l.pop()
            if t.level_of_a_node(t.root,k.value,0)%2==0:
                if k.left:
                    l.insert(0,k.left)
                if k.right:
                    l.insert(0,k.right)
                print(k.value)
            if t.level_of_a_node(t.root,k.value,0)%2!=0:
                if k.right:
                    l.insert(0,k.right)
                if k.left:
                    l.insert(0,k.left)
                print(k.value)
        #not complete. try on your own in future if you are seeing this

    def level_of_a_node(self,head,value,lev):
        if head.value==value:
            self.sum=lev
        if head.right:
            self.level_of_a_node(head.right,value,lev+1)
        if head.left:
            self.level_of_a_node(head.left,value,lev+1)
        return self.sum

    def child_sum(self,k):
        if k:
            if k.left and k.right:
                if k.left.value+k.right.value==k.value:
                    print(str(k.left.value)+"+"+str(k.right.value)+"="+str(k.value))
            if k.left:
                self.child_sum(k.left)
            if k.right:
                self.child_sum(k.right)

    def sum_tree(self,k):
        if k:
            if k.left and k.right:
                print(k.left.value+k.right.value==k.value)
            if k.left:
                self.sum_tree(k.left)
            if k.right:
                self.sum_tree(k.right)

    def diameter(self,k):
        if k is None:
            return 0
        else:
            lt = self.height(k.left)
            rt = self.height(k.right)
            return 1+lt+rt

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
