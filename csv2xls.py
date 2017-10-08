#chap3- problem 13
import tablib,sys

def ctox():
    '''
    exports a given csv file to xls file    

    '''
    csv=sys.argv[-2]
    xls=sys.argv[-1]
    data=tablib.Dataset()
    with open(csv,'r') as f:
        data.csv=f.read()
    with open(xls,'wb') as f:
        f.write(data.xls)

ctox()    
