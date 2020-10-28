class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.up=None
        self.down=None

k=Node(10)
k.up=Node(2)
k.down=Node(8)
k.left=Node(6)
k.right=Node(4)

print(k.left.value)

     #    2
     #    |
     # 6--10--4
     #    |
     #    8