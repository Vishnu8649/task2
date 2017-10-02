def dup(L):
    L1=[]
    for x in L:
        if count(x,L)>1 and x not in L1:
            L1.append(x)
    return L1
        
def count(x,L):
    c=0
    for i in L:
        if i==x:
            c+=1
    return c

print(dup([1,2,4,2,1,3,7,5]))
