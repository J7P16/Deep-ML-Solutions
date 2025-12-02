import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	correct_predictions = 0
	for i in range(len(y_pred)):
		if (y_true[i] == y_pred[i]):
			correct_predictions += 1
	accuracy = correct_predictions / len(y_pred)
	return accuracy