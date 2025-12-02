import numpy as np

def make_diagonal(x):
	# Your code here
	diagonal_matrix = []
	for i in range(len(x)):
		diagonal_row = []
		for j in range(len(x)):
			if (j == i):
				diagonal_row.append(x[i])
			else:
				diagonal_row.append(0)
		diagonal_matrix.append(diagonal_row)
	return diagonal_matrix