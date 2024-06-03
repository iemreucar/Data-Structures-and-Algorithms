from hw2_ModdedLists import ModdedLists
from hw2_BinarySearchTree import BinarySearchTree

hw2_list=ModdedLists()
hw2_list.add_to_list("data.txt")
hw2_list.list_search("Elijah25727")
hw2_list.list_search("Sophia13519")
hw2_list.list_search("Mia47028")
hw2_list.list_search("Theodore35587")
hw2_list.list_search("Isabella2790")
hw2_list.list_search("Olivia14757")



hw2_bst=BinarySearchTree()
hw2_bst.add("data.txt",1000)
hw2_bst.search("Elijah25727")
hw2_bst.search("Sophia13519")
hw2_bst.search("Mia47028")
hw2_bst.search("Theodore35587")
hw2_bst.search("Isabella2790")
hw2_bst.search("Olivia14757")