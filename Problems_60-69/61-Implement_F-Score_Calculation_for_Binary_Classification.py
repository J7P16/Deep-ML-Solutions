import numpy as np

def f_score(y_true, y_pred, beta):
    """
    Calculate F-Score for a binary classification task.
    :param y_true: Numpy array of true labels
    :param y_pred: Numpy array of predicted labels
    :param beta: The weight of precision in the harmonic mean
    :return: F-Score rounded to three decimal places
    """
    true_positives, positive_samples, predicted_positives = 0, 0, 0
    for i in range(len(y_true)):
        if (y_pred[i] == 1 and y_true[i] == 1):
            true_positives += 1
        if (y_true[i] == 1):
            positive_samples += 1
        if (y_pred[i] == 1):
            predicted_positives += 1
    recall = true_positives / positive_samples
    precision = true_positives / predicted_positives
    F_score = (1 + beta ** 2) * ((precision * recall) / (beta ** 2 * precision + recall))
    return np.round(F_score, 3)