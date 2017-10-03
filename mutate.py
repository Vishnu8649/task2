#chap2- problem 32
import string
def mutate(s):
    '''
    input : string
    output: words which are the mutations 
            of the string 

    '''
    d=[]
    for x in list(string.ascii_lowercase)+['']:
        for a in  range(len(s)):
            c=''
            if a==0:
                c=x+s[1:]
            elif a<len(s)-1:
                c=s[:a+1]+x+s[a+2:]
            else :
                c=s[:a]+x
            d.append(c)
    d1=[]
    for x in range(len(s)):
        if x==len(s)-1:
            c=s[x]+s[1:x]+s[0]
        elif x==0:
            c=s[1]+s[0]+s[2:]
        else:
            c=s[:x]+s[x+1]+s[x]+s[x+2:]
        d.append(c)
    return list(set(d))
