#chap2- problem 26

def filter(f,L):

    '''
    implementation of filter()

    '''
    f=[x for x in L if f(x)==True]
    return f

print(filter(lambda x :x%2==0,range(10)))
