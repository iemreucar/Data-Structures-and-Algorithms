from data_structure import Node,BST

values=[2,8,5,6,0,1,9,6,4,3]

my_tree=BST()

for v in values:
    my_tree.add(v)


my_tree.search(7)
my_tree.search(8)
my_tree.search(9)
my_tree.search(-1)