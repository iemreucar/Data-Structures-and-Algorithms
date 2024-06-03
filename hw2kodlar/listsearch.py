from timeit import default_timer as timer

class Customer:
    def __init__(self,name,offer):
        self.name = name
        self.offer = offer
        self.next = None   

class CustomerList:
    def __init__(self):
        self.head = None

    def createfromfile(self,filepath, n):
        with open(filepath) as fp:
            data = fp.readlines()[:n]
            for d in data:
                if d[-1] == "\n":
                    d = d[:-1]
                name, offer = d.split(" ")
                self.add(name, offer)

    def add(self, name, offer):
        newcustomer = Customer(name, offer)
        if not self.head:
            self.head = newcustomer
        else:
            traverser = self.head
            while traverser.next:
                traverser = traverser.next
            traverser.next = newcustomer


    def search(self, name):
        start = timer()
        self.counter = 0
        traverser = self.head
        while traverser:
            self.counter += 1
            if traverser.name == name:
                end = timer()
                return print("Found ", name, "in", self.counter, "comparisons", " - time:", (end-start))
            else:
                traverser = traverser.next
        end = timer()
        return print("Not found", name, "in", self.counter, "comparisons", " - time:", (end-start))
        
    