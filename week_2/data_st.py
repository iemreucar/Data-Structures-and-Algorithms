class Node:
    def __init__(self,card) -> None:
        self.data=card
        self.next=None
        pass

class Stack:
    def __init__(self) -> None:
        self.head=None
        pass
    def push(self,data):
        newnode=Node(data)
        newnode.next=self.head
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        temp=self.head
        self.head=self.head.next
        return temp.data
    def size(self):
        traverser=self.head
        counter=0
        while (traverser != None):
            counter+=1
            traverser=traverser.next
        return counter
    