def izip(l1,l2):
    new=[]
    if len(l1)<len(l2):
        for x in range(len(l1)):
            new.append((l1[x],l2[x]))
    else:
        for x in range(len(l2)):
            new.append((l1[x],l2[x]))
    return iter(new)

