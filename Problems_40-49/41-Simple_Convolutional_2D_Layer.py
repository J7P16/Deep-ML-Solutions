import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	input_height, input_width = input_matrix.shape
	kernel_height, kernel_width = kernel.shape

    # Your code here
    # applying padding
	if (padding > 0):
		padded_input = np.pad(input_matrix, ((padding, padding), (padding, padding)), mode="constant", constant_values = 0)
	else:
		padded_input = input_matrix
	padded_height, padded_width = padded_input.shape
	
    # computing output dimensions
	output_height = ((padded_height - kernel_height) // stride) + 1
	output_width = ((padded_width - kernel_width) // stride) + 1
	
    # convolution operation
	output_matrix = np.zeros((output_height, output_width))
	for r in range(output_height):
		for c in range(output_width):
			total = 0
			for kr in range(kernel_height):
				for kc in range(kernel_width):
					indexR, indexC = r * stride + kr, c * stride + kc
					total += padded_input[indexR][indexC] * kernel[kr][kc]
				output_matrix[r][c] = total
				
	return output_matrix