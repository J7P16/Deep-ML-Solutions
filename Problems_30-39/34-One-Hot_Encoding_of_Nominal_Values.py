import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	if (n_col is None):
		n_col = max(x) + 1
	encoding = []
	for num in x:
		row = []
		for i in range(n_col):
			if (i == num):
				row.append(1)
			else:
				row.append(0)
		encoding.append(row)
	return np.array(encoding).astype(float)