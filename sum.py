#Chap2 -Problem 2,3

def sum(L):
    if type(L[0])==str:
        s=''
    else:
        s=0
    for x in L:
        s+=x
    return s

print(sum([1,2,3]))
print(sum(['aaa','bbb','ccc']))
