#chap2-problem 16
def exsort(L):
    def fun(s):
        d=s.split('.')
        return d[1]
    L.sort(key=fun)
    return L
print(exsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))
