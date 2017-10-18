def tree_reverse(L):
    d=[]
    for x in reversed(L):
        if isinstance(x,list):
            d.append(tree_reverse(x))
        else:
            d.append(x)
    return d

print tree_reverse([1, 2, [3, 4, [5]]])
