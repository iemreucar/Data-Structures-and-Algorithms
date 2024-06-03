##doxygen report for your codes

from data_structure import LinkedList

my_list=LinkedList()
print(my_list.index(0))

my_list.add("boey",35)
my_list.add("del piero",35)
my_list.add("kazmakazim",35)
print(my_list.index(2))

my_list.add("amrabat",35)
my_list.add("totti",35)
my_list.add("zabaleta",35)
print(my_list.index(0))
print(my_list.index(1))
print(my_list.index(2))
print(my_list.index(3))

print(my_list.size())
my_list.print()

my_list.remove("del piero")
my_list.print()

my_list.remove("totti")
my_list.print()

