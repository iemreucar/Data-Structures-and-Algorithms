from binarysearchtree import Customer, BST
from listsearch import Customer, CustomerList

path = "data.txt"

customers = CustomerList()
#customers = BST()

customers.createfromfile(path,100000)


customers.search("Elijah25727")
customers.search("Sophia13519")
customers.search("Mia47028")
customers.search("Theodore35587")
customers.search("Isabella2790")
customers.search("Olivia14757")

