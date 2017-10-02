#chap2-problem7

def min(L):
    m=L[0]
    for x in L:
        if x<m:
            m=x
    return m

def max(L):
    mx=L[0]
    for x in L:
        if x>mx:
            mx=x
    return mx
print(min([5,2,1,3]))
print(max([2,5,8,3]))
