class Node:
    def __init__(self,name,number) -> None:
        self.name=name
        self.number=number
        self.next=None
        pass
#    def __ge__(self,nod):
#        return self.name>=nod.name
class LinkedList:
    def __init__(self) -> None:
        self.head=None
        pass
    def add(self,name,number):
        newnode=Node(name,number)
        if(not self.head):
            self.head=newnode
        else:
            if(newnode.name<self.head.name):
                newnode.next=self.head
                self.head=newnode
            else:
                traverser=self.head
                while (traverser.next):
                    if(newnode.name<traverser.next.name):
                        newnode.next=traverser.next
                        traverser.next=newnode
                        break
                    traverser=traverser.next
                if(not traverser.next):
                    traverser.next=newnode
                
    def remove(self,name):
        temp=None
        if (self.head):
            if(self.head.name==name):
                temp=self.head
                self.head=self.head.next
            else:
                traverser=self.head
                while(traverser.next):
                    if (name<traverser.next.name):
                        break
                    if(traverser.next.name==name):
                        temp=traverser.next
                        traverser.next=traverser.next.next
                        break
                    traverser=traverser.next
            if temp:
                del temp
    def update(self):
        None
    def index(self,x):
        traverser=self.head
        if (not traverser):
            return "",0
        for i in range(x):
            traverser=traverser.next
        return traverser.name,traverser.number
    def __getitem__(self,x):
        return self.index(x)
    def size(self):
        traverser=self.head
        counter=0
        while(traverser):
            counter+=1
            traverser=traverser.next
        return counter      
    def print(self):
        traverser=self.head
        while(traverser):
            print(traverser.name,traverser.number)
            traverser=traverser.next
        