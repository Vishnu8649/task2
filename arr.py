#chap2- problem 29

def array(n,m):
    '''
    input- n (number of rowa)
           m (number of columns)
    output- two dimensional array
            of order nxm with all 
            None values   

    '''
    a=[[None for x in range(m)] for x in range(n)]
    return a
