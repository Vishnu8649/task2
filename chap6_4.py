def treemap(f,l):
    L=[]
    for x in l:
        if isinstance(x,list):
            L.append(treemap(f,x))
        else:
            L.append(f(x))
    return L

print treemap(lambda x: x*x*x, [1, 2, [3, 4, [5]]])
