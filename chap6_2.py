def flatten_dict(d,dx=None, result=None):
    if result is None:
        result={}
    for x in d:
        if isinstance(d[x],dict):
            flatten_dict(d[x],x,result)
        elif dx is not None:
            result[str(dx)+'.'+str(x)]=d[x]
        else:
            result[x]=d[x]
    return result

print flatten_dict({'a': 1, 'b': {'x':{'a': 2}, 'y': 3}, 'c': 4})
