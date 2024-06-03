from timeit import default_timer as timer

class Customer:
    def __init__(self, name, offer) ->None:
        self.name = name 
        self.offer = offer
        self.left = None
        self.right = None

class BST:
    def __init__(self) ->None:
        self.root = None
    
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
        if self.root == None:
            self.root = newcustomer
        else:
            self._add(self.root, newcustomer)

    #def add içinde çalışacak recursive olan fonksiyon
    def _add(self, current, newcustomer):
        if newcustomer.name<= current.name:
            if current.left:
                self._add(current.left, newcustomer)
            else:
                current.left = newcustomer
        else:
            if current.right:
                self._add(current.right, newcustomer)
            else:
                current.right = newcustomer
    

    def search(self, name):
        start = timer()
        self.counter = 0
        result = self._search(self.root, name)
        if result is None:
            end = timer()
            print("Not found", name, "in", self.counter, "comparisons", " - time:", (end-start))
        else:
            end = timer()
            print("Found ", name, "in", self.counter, "comparisons", " - time:", (end-start))
        return result
        
    
    def _search(self, current, name):
        self.counter += 1
        if not current:
            return None
        elif current.name == name:
            return name, self.counter
        elif name < current.name:
            return self._search(current.left, name)
        else:
            return self._search(current.right, name)

        