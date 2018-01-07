### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(x):
    if x == []:
     return []
    if x == None:
     return None
    x.sort
    f = []
    len_o = len(x)
    c = 0
    for i in range(0, len_o):
        a = list(x[i])
            
        l = len(a)
        for s in range(0,l):
            
            if a[s] == None:
                
                a.remove(None)
                a.insert(s,0)
                continue             
        b = sum(a[2:])
        del (a[2:])
        a.append(b)
        a = tuple(a)
        f.append(a)

    return f
    
#### End OF MARKER
