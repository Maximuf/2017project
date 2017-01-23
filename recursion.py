
def replicate_recur(a, b):
    if not isinstance(a, int):
        raise ValueError
    if(b==[]):
        raise ValueError
    if a <= 0:
        return []
    res = replicate_recur(a -1, b)
    res.append(b)
    return res
def replicate_iter(a, b):
    if not isinstance(a, int):
        raise ValueError
    if(b==[]):
        raise ValueError
    res = []
    for i in range(a):
        res.append(b)
    return res
    a, b = (3, 5)
    try:
        return replicate_recur(a, b)
    except ValueError:
        print ("Wrong 'a' type")
    try:    
        return replicate_iter(a, b)
    except ValueError:
        print ("Wrong 'a' type")
