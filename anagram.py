#chap2- problem 36

def anagram(L):
    '''
        input  list L
        output list of anagrams in L

    '''
    dlist=[tuple(sorted(tuple(x))) for x in L]
    k={}
    for x in range(len(L)):
        if tuple(sorted(tuple(L[x]))) in k:
                k[dlist[x]].append(L[x])
        else:
                k[dlist[x]]=[L[x]]
    return k.values()
 
print anagram(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
    
