#!/usr/bin/python3
def max_integer(my_list=[]):
	if len(my_list) == 0:
	    return None

	max_val = my_list[0]

	for integer in my_list:
	    if integer > max_val:
	        max_val = integer
	
	return max_val
