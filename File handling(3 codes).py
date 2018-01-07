### YOUR CODE FOR line_count() FUNCTION GOES HERE ###
def line_count(directory, name, y=0):
	f = os.path.join(directory,name)
   	f = open(f)
   	count = 1
   	if y == 0:
	   	for line in f.readlines():
	   	    count += 1
	   	f.close()
	   	return (count)
	if y == True:
		f = open(name,'r')
		x = []
		for line in f:
    			x.append(line.strip())
		count = 0
		for i in range(0,len(x)):
    			if len(x[i]) >= 1:
        				count += 1
	return (count)



### YOUR CODE FOR character_count() FUNCTION GOES HERE ###
def character_count(directory, name, x = 0):
    if x == True:
    	fname = os.path.join(directory, name)
    	infile = open(fname, 'r')
    	characters = 0
    	for line in infile:
    		wlist = line.split( )
        	characters = characters + sum(len(word) for word in wlist)
    	return(characters)
    if x == 0:
    	fname = os.path.join(directory, name)
    	infile = open(fname, 'r')
    	characters = 0
    	for line in infile:
        	characters = characters + len(line)
    	return(characters)    	
#### End OF MARKER
            

### YOUR CODE FOR move_lines() FUNCTION GOES HERE ###
def move_lines(f_in, f_out, line):
    f_in = open(f_in)
    f_out = open(f_out, 'w+')
    l = []
    l = f_in.read().split('\n')
    for i in range(0, line):
        if i == line -1:
            f_out.write(l[i])
        else:
            f_out.write(l[i])
            f_out.write('\n')
    f_in.close()
    f_out.close()

#### End OF MARKER
