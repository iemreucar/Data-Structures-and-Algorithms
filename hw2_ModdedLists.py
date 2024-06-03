import time
class Node():
    def __init__(self,customers,offers) -> None:
        self.customers=customers
        self.offers=offers


class ModdedLists():
    def __init__(self) -> None:
        self.list1k=[]
        self.list10k=[]
        self.list100k=[]
        self.list1m=[]

    def add_to_list(self,file):
        try:
            f=open(file)

            all_list=f.read().split()
            for i,j in zip(all_list[0:2000:2],all_list[1:2000:2]):
                self.list1k.append(Node(i,j))
            for i,j in zip(all_list[0:20000:2],all_list[1:20000:2]):
                self.list10k.append(Node(i,j))
            for i,j in zip(all_list[0:200000:2],all_list[1:200000:2]):
                self.list100k.append(Node(i,j))
            for i,j in zip(all_list[0::2],all_list[1::2]):
                self.list1m.append(Node(i,j))
            f.close()

        except FileNotFoundError:
            print("data.txt file is not in the folder")

                    
    def list_search(self, target):
        counter = 0
        found=False
        start=time.perf_counter()
        for i in range (len(self.list1k)):
            counter += 1
            if self.list1k[i].customers == target:
                print(target, "has been found in", counter, "comparisons")
                found=True
                break  
        if not found:
            print(target, "couldn't be found in", counter, "comparisons")
        end=time.perf_counter()
        print("1k time:",end-start)

        counter = 0
        found=False
        start=time.perf_counter()
        for i in range (len(self.list10k)):
            counter += 1
            if self.list10k[i].customers == target:
                print(target, "has been found in", counter, "comparisons")
                found=True
                break
        if not found:
            print(target, "couldn't be found in", counter, "comparisons")
        end=time.perf_counter()
        print("10k time:",end-start)

        counter = 0
        found=False
        start=time.perf_counter()
        for i in range (len(self.list100k)):
            counter += 1
            if self.list100k[i].customers == target:
                print(target, "has been found in", counter, "comparisons")
                found=True
                break
        if not found:
            print(target, "couldn't be found in", counter, "comparisons")
        end=time.perf_counter()
        print("100k time:",end-start)

        counter = 0
        found=False
        start=time.perf_counter()
        for i in range (len(self.list1m)):
            counter += 1
            if self.list1m[i].customers == target:
                print(target, "has been found in", counter, "comparisons")
                found=True
                break
        if not found:
            print(target, "couldn't be found in", counter, "comparisons")
        end=time.perf_counter()
        print("1m time:",end-start)
        