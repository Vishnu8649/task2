def unique(L):
    L1=[]
    for x in L:
        if x not in L1:
            L1.append(x)
    return L1

print(unique([1,1,6,4,3,6,5,4]))
