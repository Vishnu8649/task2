#chap2- problem 27

def triplets(n):
    d=[]
    if n>2:
        d= [(x,y,x+y) for x in range(1,n)\
        for y in range(1,n) if (x+y)<n]
    d1=d[:]
    k=[]
    for a in d1:
        (x,y,z)=a
        if (y,x,z) not in k:
            k.append(a)
    return k

print(triplets(10))
            
