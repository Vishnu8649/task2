def lensort(L):
    L.sort(key=lambda x:len(x))
    return L

print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))
