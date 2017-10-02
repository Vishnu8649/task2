def cumulative_product(L):
    L1=[]
    d=0
    for x in L:
        d+=x
        L1.append(d)
    return L1
print (cumulative_product([1,3,4,5,6,2]))
