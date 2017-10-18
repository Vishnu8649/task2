def count_change(t,c):
    ways = [1]+[0]*t
    print ways
    for x in c:
        for i in range(x, t+1):
            ways[i]+=ways[i-x]
    return ways[t]

print count_change(10,[1,5])
print count_change(10,[1,2])
print count_change(100,[5,4,10,25,50])
