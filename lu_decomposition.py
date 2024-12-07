import numpy as np

def lu_decomposition(matrix, size):
    # Convert the input to a NumPy array with dtype=float for compatibility
    matrix = np.array(matrix, dtype=float)
    L = np.eye(size)  # Initialize L as an identity matrix of given size
    U = matrix.copy()  # Copy the input matrix for U

    for i in range(size):
        if U[i][i] == 0:
            raise ValueError(f"Pivot element U[{i}][{i}] is zero. Matrix requires pivoting or is singular.")
        for j in range(i + 1, size):
            multiplier = U[j][i] / U[i][i]
            L[j][i] = multiplier
            # Update the row in U to zero out the element below the pivot
            U[j] = U[j] - multiplier * U[i]
    return L, U

def inverseMatrix(mat):
    det = np.linalg.det(mat)
    if det == 0:
        print("The matrix is non - invertible, please re-enter the matrix")
    else:
        print("The matrix is invertible")
        inv_mat = np.array(np.linalg.inv(mat))
        return inv_mat

def lu(matrix, size, V):
    L, U = lu_decomposition(matrix, size)
    L_inverse = inverseMatrix(L)
    U_inverse = inverseMatrix(U)
    ans_vector = np.dot(U_inverse, np.dot(L_inverse, V))
    return ans_vector
