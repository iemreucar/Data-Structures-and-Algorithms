def left(k):
    return 2*k+1
def right(k):
    return 2*k+2
def parent(k):
    return (k-1)//2

my_tree=["D","B","E","A","C","F","G"]

def inorder(k,tree):
    #left
    l=left(k)
    if l<len(tree):
        inorder(l,tree)
    #kendi
    print(tree[k],end=" ")
    #right
    r= right(k)
    if r<len(tree):
        inorder(r,tree)


inorder(0,my_tree)