#chap3- problem 

import re

def make_slug(S):
    '''
    prints a string by removing
    special characters and spaces
    and between each words puts '-'

    '''
    s=re.split('\W*',S)
    st=''
    for x in s:
        if x!='':
            st+=x+'-'
    if st[-1]=='-':
        print st[:len(st)-1]
    else:
        print st

make_slug( '--hello- @ world--')
