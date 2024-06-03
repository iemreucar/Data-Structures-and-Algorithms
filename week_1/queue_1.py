class queue:    #FIFO first in first out
    def __init__(self) -> None:
        self.array=[]
    def push(self,x):
        self.array.append(x)
    def pop(self):
        #self.array.pop(0)
        temp = self.array[0]
        del self.array[0]
        return temp
    def peek(self):
        return self.array[0]
    def isEmpty(self):
        return len(self.array)==0
    def size(self):
        return len(self.array)
    
class stack:    #LIFO last in first out
    def __init__(self) -> None:
        self.array=[]
    def push(self,x):
        self.array.append(x)
    def pop(self):
        #self.array.pop(-1)
        if not self.isEmpty():
            temp = self.array[-1]
            del self.array[-1]
            return temp
        else:
            print("NAN")
    def peek(self):
        return self.array[-1]
    def isEmpty(self):
        return len(self.array)==0
    def size(self):
        return len(self.array)    


if __name__=="__main__":
    my_structure=queue()
    my_structure.push(3)
    my_structure.push(5)
    my_structure.push(8)

    while not my_structure.isEmpty():
        print(my_structure.pop())