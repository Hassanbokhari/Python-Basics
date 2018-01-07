### YOUR CODE FOR get_types_counts() FUNCTION GOES HERE ###
def get_types_counts(x):
	t = x.items()
	dictionary = {}
	for k,v in t:
		a = len(v)
		dictionary[k] = a
	
	return dictionary
#### End OF MARKER


### YOUR CODE FOR get_types() FUNCTION GOES HERE ###
def get_types(d):
	return d.keys()

#### End OF MARKER


### YOUR CODE FOR get_author_count() FUNCTION GOES HERE ###
def get_author_count(x, b):
    count = 0
    for k in x:
        for i in x[k]:
            
        
            t=i['author']
            if t['username'] == b:
                count+=1
    return count

#### End OF MARKER


