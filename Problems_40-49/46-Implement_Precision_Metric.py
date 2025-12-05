import numpy as np
def precision(y_true, y_pred):
	# Your code here
    true_positives, false_positives = 0, 0
    for i in range(len(y_true)):
        if (y_pred[i] == 1):
            if (y_true[i] == 1):
                true_positives += 1
            else: 
                false_positives += 1
    precision = true_positives / (true_positives + false_positives)
    return precision
