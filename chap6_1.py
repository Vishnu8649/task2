def product(a,b):
    if a<0 and b<0:
        b=-b
        a=-a
    elif b<0 and a>=0:
        a=-a
        b=-b
    if b==1:
        return a
    else:
        return a+product(a,b-1)

print product(25,-40)
