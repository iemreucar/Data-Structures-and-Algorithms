class Node:
    def __init__(self,value) -> None:
        self.val=value
        self.next_node=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.new_links_created= False
    def add(self,value):
        newnode=Node(value)
        if not self.head:
            self.head=newnode
        else:
            current=self.head
            while current.next_node:
                current=current.next_node
            current.next_node=newnode

    def build_index(self,func):
        traverser=self.head
        while traverser:
            traverser.new_next_node=traverser.next_node
            traverser=traverser.next_node
        func()
        self.new_links_created = True

    def remove_index(self):
        traverser=self.head
        while traverser:
            traverser.new_next_node=None
            traverser=traverser.next_node
        self.new_links_created = False

    def sort(self):
        self.head_str=self.head
        traverser=self.head_str
        comparison1=self.head_str
        comparison2=self.head_str.new_next_node
        prev=None
        length=0
        while traverser:
            traverser=traverser.new_next_node
            length+=1
        for _ in range (length*length):     #bubble sort'a yeni head(head_str) siralamasi ve normal siralama girdigi icin length^2 alinir. 
            if self.head_str and self.head_str.new_next_node:
                    comparison1=self.head_str
                    comparison2=self.head_str.new_next_node
                    traverser=self.head_str
                    if not self._sorting(comparison1,comparison2):
                        comparison1.new_next_node=comparison2.new_next_node
                        comparison2.new_next_node=traverser
                        self.head_str=comparison2
                    else:
                        while self._sorting(comparison1,comparison2):
                            prev=comparison1
                            comparison1=comparison1.new_next_node
                            comparison2=comparison2.new_next_node
                            traverser=traverser.new_next_node
                        if comparison2!=None: 
                            traverser=comparison1
                            comparison1.new_next_node=comparison2.new_next_node
                            comparison2.new_next_node=comparison1
                            prev.new_next_node=comparison2
            else:
                return
            
    def _sorting(self,val1,val2):
        if val1==None or val2==None:
            return False 
        if  val1.val<=val2.val:
            return True
        else:
            return False 
        
    def print_indexed(self):
        if not self.new_links_created:
            print("linked list is not sorted")
            current=self.head
            while current:
                print(current.val, end=("-->"))
                current=current.next_node
            print ("None")
        else: 
            print("linked list is sorted")
            current=self.head_str
            while current:
                print(current.val, end=("-->"))
                current=current.new_next_node
            print ("None")


my_list=LinkedList()
my_list.add("Tolga")
my_list.add("Duygu")
my_list.add("Murat")
my_list.add("Ali")
my_list.add("Ufuk")
my_list.print_indexed()
my_list.build_index(my_list.sort)
my_list.print_indexed()
my_list.remove_index()
my_list.print_indexed()

