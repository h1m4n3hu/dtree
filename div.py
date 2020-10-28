class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def traverse(self):
        k=self.head
        while k:
            print(k.value)
            k=k.next

    def append(self,value):
        if self.head is None:
            self.head=Node(value)
        else:
            k=self.head
            while k.next:
                k=k.next
            k.next=Node(value)

    def prepend(self,value):
        if self.head is None:
            self.head=Node(value)
        else:
            k=Node(value)
            k.next=self.head
            self.head=k

    def delete(self,val):
        k=self.head
        if k.value==val:
            self.head=k.next
        prev=None
        k=self.head
        while k:
            if k.value==val:
                prev.next=k.next
            prev=k
            k=k.next

    def index(self,val):
        i=0
        k=self.head
        while k:
            if k.value==val:
                return i
            i+=1
            k=k.next

    def len(self):
        i=0
        k=self.head
        while k:
            i+=1
            k=k.next
        return i

    def val_at_index(self,index):
        len_list=l.len()
        i=0
        k=self.head
        while i<len_list:
            if i==index:
                return (k.value)
            i+=1
            k=k.next

    def del_at_position(self,index):
        a=l.val_at_index(index)
        l.delete(a)

    def reverse(self):
        first=self.head
        curr=None
        while first is not None:
            k=first.next
            first.next,curr=curr,first
            first=k
        self.head=curr

    def insert_at(self,val,index):
        a=l.len()
        i=0
        k=self.head
        n=Node(val)
        while i<a:
            if i==index:
                temp=k.next
                k.next=n
                n.next=temp
            k=k.next
            i+=1

l=LL()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.traverse()

#   10->20->30->40->50->