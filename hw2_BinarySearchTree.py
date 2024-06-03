import time

class TreeNode:
    def __init__(self,value,offer) -> None:
        self.val=value
        self.offer=offer
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root=None

    def add(self,file,length):
        try:
            f=open(file)
            all_list=f.read().split()
            for value,offer in zip(all_list[0:length*2:2],all_list[1:length*2:2]):
                newnode=TreeNode(value,offer)
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
