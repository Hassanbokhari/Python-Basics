### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(x=[]):
	top_list = find_cumulative_marks(x)
	len_o = len(top_list)
	a = 0
	io = []
	while a < len_o-1:
	    x = top_list[0][2]
	    y = top_list[1][2]
	    if x == y:
	        z = top_list[2][2]
	        if x < z:
	            top_list.remove(top_list[0])
	            top_list.remove(top_list[1])
	            a+=1
	    else:
	          if x < y:
    	              top_list.remove(top_list[0])
    	              a+=1
	          else:
    	              top_list.remove(top_list[1])
    	              a += 1
                      continue
            continue
	
	for i in range(0, len(top_list)):
	 m = top_list[i]
	 m = list(m)
	 del (m[2])
	 m = tuple(m)
	 io.append(m)
	return m
	
#### End OF MARKER
