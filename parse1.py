#chap2- problem 31

def parse(filename,deli,com):
    '''
    parser seperated by delimiter and
    ignore comments    

    '''
    f=open(filename,'r')
    d=f.read().split('\n')
    p=[]
    for x in d:
        if x!='':
            if x[0]!=com:
                p.append(x.split(deli))
  
    return p   
       
print(parse('b.txt','!','#')) 
