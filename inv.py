#chap2- problem 38

def invertdict(dic):
    '''
        input : dictionary with unique values
        output: dictiony with keys as values and 
                values as keys 

    '''
    key=dic.keys()
    new={}
    for x in key:
        new[dic[x]]=x
    return new

print(invertdict({'x': 1, 'y': 2, 'z': 3}))
