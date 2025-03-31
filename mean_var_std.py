import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    matrix = np.array([list[:3], list[3:6], list[6:]])
    matrix_mean_flat = np.mean(matrix)

    #Calculate Mean
    matrix_mean_a0 = [np.mean(matrix[i,:]) for i in range(3)]
    matrix_mean_a1 = [np.mean(matrix[:,i]) for i in range(3)]
    mean = [matrix_mean_a1, matrix_mean_a0, matrix_mean_flat]

    #Calculate Variance
    matrix_var_a0 = [np.var(matrix[i,:]) for i in range(3)]
    matrix_var_a1 = [np.var(matrix[:,i]) for i in range(3)]
    matrix_var_flat = np.var(matrix)
    variance = [matrix_var_a1, matrix_var_a0, matrix_var_flat]

    #Calculate Standard Deviation
    matrix_std_a0 = [np.std(matrix[i,:]) for i in range(3)]
    matrix_std_a1 = [np.std(matrix[:,i]) for i in range(3)]
    matrix_std_flat = np.std(matrix)
    standard_dev = [matrix_std_a1, matrix_std_a0, matrix_std_flat]

    #Calculate Max
    matrix_max_a0 = [np.max(matrix[i,:]) for i in range(3)]
    matrix_max_a1 = [np.max(matrix[:,i]) for i in range(3)]
    matrix_max_flat = np.max(matrix)
    matrix_max = [matrix_max_a1, matrix_max_a0, matrix_max_flat]

    #Calculate Min
    matrix_min_a0 = [np.min(matrix[i,:]) for i in range(3)]
    matrix_min_a1 = [np.min(matrix[:,i]) for i in range(3)]
    matrix_min_flat = np.min(matrix)
    matrix_min = [matrix_min_a1, matrix_min_a0, matrix_min_flat]

    #Calculate Sum
    matrix_sum_a0 = [np.sum(matrix[i,:]) for i in range(3)]
    matrix_sum_a1 = [np.sum(matrix[:,i]) for i in range(3)]
    matrix_sum_flat = np.sum(matrix)
    matrix_sum = [matrix_sum_a1, matrix_sum_a0, matrix_sum_flat]

    #Make Dict
    calculations = {"mean": mean, "variance": variance, "standard deviation": standard_dev, "max": matrix_max, "min": matrix_min, "sum": matrix_sum}



    return calculations
