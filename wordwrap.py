#chap2- problem 22

import sys

def wordwrap():

    '''
    input text file and width

    output prints lines wraped at word\
    boundaries with length < = width    

    '''
    f=open(sys.argv[-2],'r')
    width=int(sys.argv[-1])
    d=f.readlines()
    words=[]
    for x in d:
        words.append(x.split())
    for x in words:
        count=0
        ln=0
        w=''
        for a in x:
            ln+=len(a)+1
        if ln>width:
            for a in x:
                if (count+len(a))>=width:
                    count=0
                    w+='\n'
                w+= a+ ' '
                count+=len(a)+1
            print w,
        else:
            for a in x:
                print a,
        print ''

wordwrap()
