import itertools as it

def perm(L):
    d=[]
    for x in it.permutations(L):
        d.append(list(x))
    return d

print perm([1,2,3])
