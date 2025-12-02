import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
    maxScore = max(scores)
    probabilities = []
    summation = 0
    for score in scores:
        summation += np.exp(score - maxScore)
    for score in scores:
        log_softmax_output = score - maxScore - np.log(summation)
        probabilities.append(log_softmax_output)
    return np.round(np.array(probabilities), 4)