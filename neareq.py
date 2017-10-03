#chap2- problem 33
import string
def nearly_equal(b,s):
    '''
    input :=> b,s(strings)
    output:=> True if b is a single mutation of s
              else false

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
    return b in d
print nearly_equal('python', 'pearl')
print nearly_equal('perl', 'pearl')
print nearly_equal('python', 'jython')

