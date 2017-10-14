class reverse_iter:
    def __init__(self,l):
        self.i=-1
        self.n=-len(l)
        self.l=l

    def __iter__(self):
        return self

    def next(self):
        if self.i>=self.n:
            i=self.i
            self.i-=1
            return self.l[i]
        else:
            raise StopIteration()

it = reverse_iter([1, 2, 3, 4])

print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
