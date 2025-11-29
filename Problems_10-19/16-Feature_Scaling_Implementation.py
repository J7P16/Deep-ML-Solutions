import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
    dataS, dataN = data.astype(float), data.astype(float)

    # Standardization
    for feature in range(len(dataS[0])):
        # calculate mean of feature
        mean = 0
        for x in range(len(dataS)):
            mean += dataS[x][feature]
        mean /= len(dataS)
        # calculate standard deviation of feature
        std = 0
        for x in range(len(dataS)):
            std += (dataS[x][feature] - mean) ** 2
        std = (std / len(dataS)) ** 0.5
        # standardize feature data
        for x in range(len(dataS)):
            dataS[x][feature] = (dataS[x][feature] - mean) / std
    
    # Min-Max Normalization
    for feature in range(len(dataN[0])):
        # find min/max values
        feature_col = []
        for x in range(len(dataN)):
            feature_col.append(dataN[x][feature])
        minX, maxX, = min(feature_col), max(feature_col)
        # normalize feature data
        # using a shorter equation since min/max range is [0,1]
        for x in range(len(dataN)):
            dataN[x][feature] = (dataN[x][feature] - minX) / (maxX - minX)

    return np.round(dataS, 4).tolist(), np.round(dataN, 4).tolist()