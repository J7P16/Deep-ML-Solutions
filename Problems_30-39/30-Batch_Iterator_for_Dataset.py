import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
    batches = []
    index, count = 0, 0
    if (y is not None):
        X_batch, y_batch = [], []
        # filling in by batch size
        while (index < len(X)):
            X_batch.append(X[index])
            y_batch.append(y[index])
            count += 1
            if (count % batch_size == 0):
                batches.append([X_batch, y_batch])
                X_batch, y_batch = [], []
            index += 1
        # filling in remaining samples and labels
        if (len(X_batch) != 0):
            batches.append([X_batch, y_batch])
    else:
        X_batch = []
        # filling in by batch size
        while (index < len(X)):
            X_batch.append(X[index])
            count += 1
            if (count % batch_size == 0):
                batches.append(X_batch)
                X_batch = []
            index += 1
        # filling in remaining samples
        if (len(X_batch) != 0):
            batches.append(X_batch)
    return batches