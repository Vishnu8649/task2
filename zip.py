#chap2-problem 25

def zip(L1,L2):
    '''
    implementation of zip function    

    '''

    ln1=len(L1)
    ln2=len(L2)
    if ln1>ln2:
        d=[(L1[x],L2[x]) for x in range(ln2)]
        return d
    else:
        d=[(L1[x],L2[x]) for x in range(ln1)]
        return d

print(zip([1, 2, 3], [ "b", "c"]))
