def group(L,s):
    L1=[]
    c=0
    while(c<len(L)):
        d=0
        sub=[]
        while(d<s):
            if c<len(L):
                sub.append(L[c])
                c+=1
                d+=1
            else:
                break
        L1.append(sub)
    return L1

print(group([1,2,3,4,5,7,8,11],3))
            
