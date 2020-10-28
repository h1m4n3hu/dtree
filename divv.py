class Node:
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None

class DLL:
    def __init__(self):
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
            temp=k
            if k.value==val:
                temp.next=k.next
                k.next.prev=temp
            k=k.next

d=DLL()
d.append(10)
d.append(20)
d.append(30)
d.append(40)
d.append(50)
d.delete(30)
d.traverse()

#   10<->20<->30<->40<->50
#   10<->20<->40