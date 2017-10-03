#chap2- problem 30
def parse_csv(filename):
    '''
    parsing comma seperated values

    '''
    f=open(filename,'r')
    d=f.read().split()
    new=[]
    for x in d:
        new.append(x.split(','))
    return new

print(parse_csv('a.txt'))
