def myenum(it):
    lis=list(it)
    new=[]
    for x in range(len(lis)):
        new.append((x,lis[x]))
    return iter(new)

