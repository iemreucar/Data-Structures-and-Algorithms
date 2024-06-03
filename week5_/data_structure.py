class Node:
    def __init__(self,x) -> None:
        self.data=x
        self.left=None
        self.right=None

class NodeGeneric:
    def __init__(self,x) -> None:
        self.data=x
        self.children=[]

class BinaryTree:
    def __init__(self) -> None:
        self.root=None
    def preorder(self):
        self._preorder(self.root)

    def _preorder(self,node):
        print(node.data,end=" ")
        if node.left:
            self._preorder(node.left)
        if node.right:
            self._preorder(node.right)


    def inorder(self):
        self._inorder(self.root)
    def _inorder(self):
        self._inorder()

    def postorder(self):
        self._postorder(self.root)
    def _postorder(self,node):

        