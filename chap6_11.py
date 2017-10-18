def vectorize(fun):
    def f(l):
        l1=[fun(x) for x in l]
        return l1
    return f
