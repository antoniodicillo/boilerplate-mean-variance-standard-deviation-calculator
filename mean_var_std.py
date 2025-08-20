import numpy as np

def calculate(list):
    length = len(list)

    if length != 9:
        raise ValueError('List must contain nine numbers.');

    listNP = np.array([list[:3],list[3:6],list[6:]])
    
    mean = [np.mean(listNP, axis=0).tolist(), np.mean(listNP, axis=1).tolist(), np.mean(listNP.flatten())]
    variance = [np.var(listNP, axis=0).tolist(), np.var(listNP, axis=1).tolist(), np.var(listNP.flatten())]
    standard_deviation = [np.std(listNP, axis=0).tolist(), np.std(listNP, axis=1).tolist(), np.std(listNP.flatten())]
    max_value = [np.max(listNP, axis=0).tolist(), np.max(listNP, axis=1).tolist(), np.max(listNP.flatten())]
    min_value = [np.min(listNP, axis=0).tolist(), np.min(listNP, axis=1).tolist(), np.min(listNP.flatten())]
    sum_value = [np.sum(listNP, axis=0).tolist(), np.sum(listNP, axis=1).tolist(), np.sum(listNP.flatten())]

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': max_value,
        'min': min_value,
        'sum': sum_value
    };

    return calculations;