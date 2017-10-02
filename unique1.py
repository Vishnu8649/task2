def unique(L,key=None):
    L1=[]
    for x in L:
        if key(x) not in L1:
            L1.append(key(x))
    return L1
print(unique(["python", "java", "Python", "Java"], key=lambda s: s.lower()))
    

