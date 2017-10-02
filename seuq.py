#chap2-problem 15
def unique(L,key=None):
    L1=[]
    for x in L:
        L1.append(key(x))

    return list(set(L1))
print(unique(["python", "java", "Python", "Java"], key=lambda s: s.lower()))
    

