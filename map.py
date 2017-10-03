#chap2 -problem 25

def map(f, L):
    '''
    implementation of map()

    '''
    m=[f(x) for x in L]
    return m
print(map(lambda x:x*x, range(5)))
