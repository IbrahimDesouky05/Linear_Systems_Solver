import numpy as np


def diagonally_dominate(m, v):
    m = np.array(m)
    v = np.array(v)

    n = np.hstack((m, v))
    k = len(m)

    for i in range(k):
        if abs(m[i][i]) < abs(np.sum(m[i])):
            for j in range(i + 1, k):
                if abs(m[j][i]) > abs(np.sum(m[j]) - m[j][i]):
                    n[j], n[i] = n[i].copy(), n[j].copy()

    v = n[:,k]
    n = n[:,:-1]

    return n, v, k


def gaus(matrix, size, v, iterations, strt_value = None):

    if strt_value is None:
        x = np.zeros(size, dtype=float)
    elif np.isscalar(strt_value):  # If initial_guess is a single number
        x = np.full(size, strt_value, dtype=float)
    else:  # Otherwise, assume it's already an array or list
        x = np.array(strt_value, dtype=float)

    # Iterative process
    for k in range(iterations):
        for i in range(size):
            # Sum the terms for the ith equation except the diagonal term
            summ = 0.0
            for j in range(size):
                if j != i:
                    summ += matrix[i][j] * x[j]

            # Update the ith value using the most recent values
            x[i] = (v[i].item() - summ) / matrix[i][i].item()

    return x

def gauss_seidel_method(matrix, v, iterations,starting_values = None):

    mat, vect, size = diagonally_dominate(matrix, v)
    ans_vect = gaus(mat, size, vect, iterations,starting_values)

    return ans_vect
