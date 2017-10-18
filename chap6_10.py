import time

def profile(f):
    def f1(x,d=f):
        s=time.time()
        d(x)
        c=time.time()
        print 'time taken: ', c-s,'sec'
        return d(x)
    return  f1

def fib(n):
     if n is 0 or n is 1:
         return 1
     else:
         return fib(n-1) + fib(n-2)


d=profile(fib)
print d(20)
