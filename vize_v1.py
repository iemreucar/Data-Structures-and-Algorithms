#DEPTH SEARCH VE BREADTH SEARCH

#2. soru container=yapi()
# for i in range(6):
#     container.push(i*i)
# for i in range(6):
#     value=container.pop()
#     print(value)
# 0 1 2 3 4 5
# 0 1 4 9 16 25

# queue: 0 1 4 9 16 25 # ilk giren ilk cikar
# stack: 25 16 9 4 1 0 # son giren ilk cikar

# preorder
# kendi sol sag
# postorder
# sol sag kendi
# inorder
# sol kendi sag
    
# BST'nin özellikleri sola kucukesit saga buyukler 
# ve her parent'in 2 cocuktan fazlasi olamaz

class Node():
    def __init__(self,name,sinif,phone) -> None:
        self.name=name
        self.sinif=sinif
        self.phone=phone
        self.next=None

class LinkedList():
    def __init__(self) -> None:
        self.head=None
        self.ptrA=None
        self.ptrB=None
        self.ptrC=None
    def add(self,name,sinif,phone):
        newnode=Node(name,sinif,phone)
        
        if self.head==None:
            self.head=newnode
        else:
                traverser=self.head
                while traverser.next:
                    traverser=traverser.next
                traverser.next=newnode
                pass
        temp=self.head
        if self.ptrA==None and temp.sinif=="A":
            self.ptrA=newnode        
            while not temp.sinif=="A":
                temp=temp.next
            self.ptrA.next=newnode
        elif self.ptrB==None and temp.sinif=="B":
            self.ptrB=newnode        
            while not temp.sinif=="B":
                temp=temp.next
            self.ptrB.next=newnode
        elif self.ptrC==None and temp.sinif=="C":
            self.ptrC=newnode        
            while not temp.sinif=="C":
                temp=temp.next
            self.ptrC.next=newnode
    def delete(self,name):
        temp=None
        if(self.head):
            if(name==self.head.name):
                temp=self.head
                self.head=self.head.next
                del temp
            else:
                traverser=self.head
                while (traverser.next):
                    if(name==traverser.next.name):
                        temp=traverser.next
                        traverser.next=traverser.next.next
                        del temp
                        return
                    traverser=traverser.next
    def printlist(self):
        traverser=self.head
        while traverser:
            print(traverser.name,end=("-->"))
            traverser=traverser.next
        print("None")
    def printlistA(self):
        traverser=self.ptrA
        while traverser:
            print(traverser.name,end=("-->"))
            traverser=traverser.next
        print("None")



my_list=LinkedList()
my_list.add("ceren","A","436332")
my_list.add("etyceren","A","42236332")
my_list.add("safceren","A","4154136332")
my_list.add("dceren","B","1436332")
my_list.add("sfgdceren","B","1436332")
my_list.add("hrfddceren","B","1436332")
my_list.add("zceren","C","2436332")
# my_list.add("44")
# my_list.add("122")
# my_list.add("244")
# my_list.add("422")
# my_list.add("544")
my_list.printlist()
my_list.printlistA()
# my_list.delete("hrfddceren")
my_list.printlist()
my_list.printlistA()

