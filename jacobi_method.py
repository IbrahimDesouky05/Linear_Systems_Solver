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




def jacob(matrix, size, v, iterations):
    x = np.zeros(size)

    # Iterative process
    for k in range(iterations):
        x_new = np.copy(x)

        for i in range(size):
            # Sum the terms for the ith equation except the diagonal term
            summ = 0
            for j in range(size):
                if j != i:
                    summ += matrix[i][j] * x[j]

            # Update the ith value
            x_new[i] = (v[i].item() - summ) / matrix[i][i].item()

        # Update the solution for the next iteration
        x = np.copy(x_new)

    return x

def jacobian_method(matrix, v, iterations = 3):

    mat, vect, size = diagonally_dominate(matrix, v)
    ans_vect = jacob(mat, size, vect, iterations)

    return ans_vect



# m = np.array([[1, 40, 2, 3], [5, 1, -1, 0], [2, -1, 10, 100], [1, 2, 50, -1]])
# v = np.array([ [0], [8], [15], [30] ])

#print(jacobian_method(m, v))
#print(np.array( [1.7,0.0,0.0,0.0],dtype=float))


