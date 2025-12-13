import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
    maxScore = max(scores)
    probabilities = []
    summation_term = 0
    for score in scores:
        summation_term += np.exp(score - maxScore)
    for score in scores:
        log_softmax_output = score - maxScore - np.log(summation_term)
        probabilities.append(log_softmax_output)
    return np.round(np.array(probabilities), 4)