def unflatten_dict(d):
    result={}
    for x in d:
        if len(x.split('.'))>1:
            y=x.split('.')[0]
            result[y]={x.split[1]}
                
