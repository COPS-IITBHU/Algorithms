l = [ 2,3,4,5,6,8]

n = len(l)
curr_max = 0
for i in n:
	# TODO Fill Code here
	if l[i] > curr_max:
		curr_max = l[i]
		
print("Max element is ", curr_max)


