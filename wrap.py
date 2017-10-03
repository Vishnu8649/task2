#chap2- problem 21
import sys

def wrap():
    '''
    inputs file and width 
    outputs wraps lines longer\ 
    than width

    ''' 
    f=open(sys.argv[-2],'r')
    width=int(sys.argv[-1])
    fd=f.readlines()
    for x in fd:
        count=0
        d=''
        if len(x)>width:
            for a in x:
                count+=1
                if count%width==0:
                    d+='\n'
                d+= a
            print d,
        else:
            print x,
wrap()
