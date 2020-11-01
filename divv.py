class Node:
    def _init_(self,value):
        self.value=value
        self.prev=None
        self.next=None

class DLL:
    def _init_(self):
        self.head=None

    def traverse(self):
        k=self.head
        while k is not None:
            print(k.value)
            k=k.next

    def append(self,value):
        if self.head is None:
            n=Node(value)
            self.head=n
        else:
            k=self.head
            n=Node(value)
            while k:
                temp=k
                k=k.next
            temp.next=n
            n.prev=temp

    def prepend(self,value):
        if self.head is None:
            n=Node(value)
            n.next=self.head
            self.head=n
        else:
            n=Node(value)
            n.next=self.head
            self.head.prev=n
            self.head=n

    def delete(self,val):
        k=self.head
        while k:
            if k.value==val:
                a=k.prev
                k.prev.next=k.next
                k.next.prev=a
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
        len_list=d.len()
        i=0
        k=self.head
        while i<len_list:
            if i==index:
                return (k.value)
            i+=1
            k=k.next

    def del_at_position(self,index):
        a=d.val_at_index(index)
        d.delete(a)

    def reverse(self):
        first=self.head
        curr=None
        while first:
            curr=first
            first.prev,first.next=first.next,first.prev
            first=first.prev
        self.head=curr

    def insert_at(self,value,index):
        a=d.len()
        i=0
        k=self.head
        n=Node(value)
        while i<a:
            if i==index:
                p=k.next
                k.next=n
                n.next=p
                n.prev=k
                n.next.prev=n
            i+=1
            k=k.next

d=DLL()
d.append(10)
d.append(20)
d.append(30)
d.append(40)
d.append(50)
d.traverse()

#   10<->20<->30<->40<->50