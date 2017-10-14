def peep(it):
    it1=list(it)
    x=it1[0]
    i=it1[:]
    return x,iter(i)

it=iter(range(5))
x,it1=peep(it)
print x, list(it1)
