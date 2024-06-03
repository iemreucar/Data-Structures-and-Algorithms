class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self) -> None:
        self.root=None
    def add(self,data):
        newnode=Node(data)
        if self.root==None:
            self.root=newnode
        else:
            self._add(self.root,newnode)
    def _add(self,current,newnode):
        if newnode.data<=current.data:
            if current.left:
                self._add(current.left,newnode)
            else:
                current.left=newnode
        else:
            if current.right:
                self._add(current.right,newnode)
            else:
                current.right=newnode
    def search(self,data):
        self.counter=0
        return  self._search(self.root,data)
    def _search(self,current,data):
        self.counter+=1
        if not current:
            print("not found",data,"in",self.counter,"comparisons")
            return None
        elif current.data==data:
            print("found it", data,"in",self.counter,"comparisons")
            return data, self.counter
        elif data<current.data:
            return self._search(current.left,data)
        else:
            return self._search(current.right,data)

        