import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
    if (seed is not None):
        np.random.seed(seed)
    # creating an array of all indices for number of samples in X
    indices = np.arange(X.shape[0])
    # shuffling the indices
    np.random.shuffle(indices)
    # advanced indexing to return lists of shuffled samples/labels
    return X[indices], y[indices]