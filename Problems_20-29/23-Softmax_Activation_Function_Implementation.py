import math

def softmax(scores: list[float]) -> list[float]:
	# Your code here
	probabilities = []
	summation = 0
	for score in scores:
		summation += math.e ** score
	for score in scores:
		probabilities.append(round(math.e ** score / summation, 4))
	return probabilities