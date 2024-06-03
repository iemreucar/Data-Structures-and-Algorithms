import time

class TreeNode:
    def __init__(self,value) -> None:
        self.val=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root=None

    def add(self,file,length):
        try:
            f=open(file)
            all_list=f.read().split()
            for value in all_list[0:length*2:2]:
                newnode=TreeNode(value)
                if self.root==None:
                    self.root=newnode
                else:
                    self._add(self.root,newnode)
            f.close()
        except FileNotFoundError:
            print("data.txt is not found")
    
    def _add(self,root_node,newnode):
        if newnode.val<=root_node.val:
            if root_node.left==None:
                root_node.left=newnode
            else:
                self._add(root_node.left,newnode)
        else:
            if newnode.val>root_node.val:
                if root_node.right==None:
                    root_node.right=newnode
                else:
                    self._add(root_node.right,newnode)

    def search(self,value):
        self.counter=0
        self._search(self.root,value)
    
    def _search(self, comparison, value):
        self.counter+=1
        start=time.perf_counter()
        if not comparison:
            print(value,"couldn't found in", self.counter,"comparisons")
            end=time.perf_counter()
            print("BST time:",end-start)
        elif comparison.val==value:
            print(value,"has been found in", self.counter,"comparisons")
            end=time.perf_counter()
            print("BST time:",end-start)
        elif value<comparison.val:
            self._search(comparison.left,value)
        else:
            self._search(comparison.right,value)





class ModdedLists():
    def __init__(self) -> None:
        self.list1k=[]
        self.list10k=[]
        self.list100k=[]
        self.list1m=[]

    def add_to_list(self,file):
        try:
            f=open(file)
            all_list=f.read().split()
            for i in all_list[0:2000:2]:
                self.list1k.append(i)
            for i in all_list[0:20000:2]:
                self.list10k.append(i)
            for i in all_list[0:200000:2]:
                self.list100k.append(i)
            for i in all_list[0::2]:
                self.list1m.append(i)
            f.close()

        except FileNotFoundError:
            print("data.txt file is not in the folder")

                                
    def list_search(self, target):
        counter = 0
        found=False
        start=time.perf_counter()
        for i in self.list1k:
            counter += 1
            if i == target:
                print(target, "has been found in", counter, "comparisons")
                found=True
                break  
        if not found:
            print(target, "couldn't be found in", counter, "comparisons")
        end=time.perf_counter()
        print("1k time:",end-start)

        counter = 0
        found=False
        start=time.perf_counter()
        for i in self.list10k:
            counter += 1
            if i == target:
                print(target, "has been found in", counter, "comparisons")
                found=True
                break
        if not found:
            print(target, "couldn't be found in", counter, "comparisons")
        end=time.perf_counter()
        print("10k time:",end-start)

        counter = 0
        found=False
        start=time.perf_counter()
        for i in self.list100k:
            counter += 1
            if i == target:
                print(target, "has been found in", counter, "comparisons")
                found=True
                break
        if not found:
            print(target, "couldn't be found in", counter, "comparisons")
        end=time.perf_counter()
        print("100k time:",end-start)

        counter = 0
        found=False
        start=time.perf_counter()
        for i in self.list1m:
            counter += 1
            if i == target:
                print(target, "has been found in", counter, "comparisons")
                found=True
                break
        if not found:
            print(target, "couldn't be found in", counter, "comparisons")
        end=time.perf_counter()
        print("1m time:",end-start)
        
        

                


hw2_list=ModdedLists()
hw2_list.add_to_list("data.txt")
hw2_list.list_search("Olivia14757")

hw2_bst=BinarySearchTree()
hw2_bst.add("data.txt",1000000)
hw2_bst.search("Elijah25727")
hw2_bst.search("Sophia13519")
hw2_bst.search("Mia47028")
hw2_bst.search("Theodore35587")
hw2_bst.search("Isabella2790")
hw2_bst.search("Olivia14757")






