import sys,inspect

def mydoc():
    mod=sys.argv[-1]
    f=__import__(mod)
    print 'Help on module',mod
    print '\nDESCRIPTION\n\n',f.__doc__
    func=[]
    for x in dir(f):
        d=getattr(f,x)
        if inspect.isfunction(d):
            func.append(x+'()')
    if len(func)==0:
        print '\n'
    else:
        print '\nFUNCTIONS\n'
        for x in func:
            print x

mydoc()
