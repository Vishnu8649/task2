#chap2-problem 6
def reverse(L):
    i=-1
    L1=[]
    while(L!=[]):
        L1.append(L.pop())
    return L1
print(reverse(reverse([1,2,3,4])))
