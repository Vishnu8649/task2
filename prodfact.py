def product(L):
    p=1
    for x in L:
        p*=x
    return p

def factorial(x):
    return product(range(1,x+1))

print(factorial(6))
