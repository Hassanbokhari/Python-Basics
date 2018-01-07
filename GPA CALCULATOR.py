### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###
def get_grade(x):
	if(x == 'A+'):
		return 4.00
	elif(x == 'A'):
		return 4.00
	elif(x == 'A-'):
		return 3.67
	elif(x == 'B+'):
		return 3.33
	elif(x == 'B'):
		return 3.00
	elif(x == 'B-'):
		return 2.67
	elif(x == 'C+'):
		return 2.33
	elif(x == 'C'):
		return 2.00
	elif(x == 'C-'):
		return 1.67
	elif(x == 'D+'):
		return 1.33
	elif(x == 'D'):
		return 1.00
	elif(x == 'F'):
		return 0.00
	else:
		return None
		
def calculate_sgpa(x=[]):
	if x == ([]):
		return 0
	if x == None:
		return None
	if type(x) == str:
		y = get_grade(x)
		return y
	l = len(x)
	l = int(l)
	sum = 0.00
	for counter in range(0, l):
		if get_grade(x[counter]) == None:
			return None
		else:
			sum += get_grade(x[counter])
	gpa = sum / l
	return gpa
	
#### End OF MARKER

### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted(grades, weightage):
	if type(grades) == str and type(weightage) == int:
		d = get_grade(grades)
		g = (d*weightage)/weightage
		return g
	g = len(grades)
	w = len(weightage)
	sum_g = 0
	sum_w = 0
	if (g != w):
		return None
	else:
		for count in range(0, g):
			if get_grade(grades[count])== None:
				return None
			else:
				num = get_grade(grades[count]) * weightage[count]
				sum_g = sum_g + num
				sum_w = sum_w + weightage[count]
			
	gpa_w = sum_g / sum_w
	return gpa_w

#### End OF MARKER
