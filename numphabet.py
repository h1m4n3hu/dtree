class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def prepend(self,value):
        if self.head is None:
            self.head=Node(value)
        else:
            k=Node(value)
            k.next=self.head
            self.head=k

    def show(self):
        first=self.head
        while first:
            print(first.value)
            first=first.next

l=LL()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.show()