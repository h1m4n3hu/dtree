class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def append(self,value):
        new=Node(value)
        if self.head is None:
            self.head=new
        else:
            first=self.head
            while first.next:
                first=first.next
            first.next=new

    def show(self):
        first=self.head
        while first:
            print(first.value)
            first=first.next

    def show_iter(self,k):
        print(k.value)
        if k.next:
            self.show_iter(k.next)

    def from_end(self,n):
        k1=self.head
        k2=self.head
        i=0
        while i<n:
            k2=k2.next
            i+=1
        #print(k2.value)
        while k2.next:
            k2=k2.next
            k1=k1.next
        print(k1.value)

l=LL()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.from_end(1)