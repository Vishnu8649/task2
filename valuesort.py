#chap2- problem 37

def valuesort(dic):
    '''

    sort values of a dictionary based on the key

    '''
    key=dic.keys()
    key.sort()
    val=[]
    for x in key:
        val.append(dic[x])
    return val
    
print(valuesort({'x': 1, 'y': 2, 'a': 3}))
