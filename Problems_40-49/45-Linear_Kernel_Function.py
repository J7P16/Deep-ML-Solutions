import numpy as np

def kernel_function(x1, x2):
	# Your code here
	linear_kernel = 0
	for i in range(len(x1)):
		linear_kernel += x1[i] * x2[i]
	return linear_kernel