class Node:
    def __init__(self,value) -> None:
        self.val=value
        self.next_node=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def add(self,value):
        newnode=Node(value)
        if not self.head:
            self.head=newnode
        else:
            current=self.head
            while current.next_node:
                current=current.next_node
            current.next_node=newnode

    def a(self):
        c1=self.head
        c2=self.head.next_node
        temp=self.head

        c1=c2.next.node
        c2=temp
        temp=c2

        
        pass


my_list=LinkedList()
my_list.add("5")
my_list.add("15")
my_list.add("25")
my_list.add("35")
my_list.add("45")
my_list.a