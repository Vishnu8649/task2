#chap2- problem 13

def lensort(L):
    L.sort(key=lambda x:len(x))
    return L

print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))
