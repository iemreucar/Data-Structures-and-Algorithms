from data_structure import *

my_tree=BinaryTree()

my_tree.root=Node("D")
my_tree.left=Node("B")
my_tree.right=Node("A")
my_tree.left.right=Node("C")


temp=Node("E")
temp.left=Node("F")
temp.right=Node("G")
my_tree.root.right=temp

