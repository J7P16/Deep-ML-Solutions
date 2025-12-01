import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	B, C = np.array(B), np.array(C)
	inverse_C = np.linalg.inv(C)
	P = inverse_C @ B
	return np.round(P, 4).tolist()