import numpy as np

def inverseMatrix(mat):
    det = np.linalg.det(mat)
    if det == 0:
        print("The matrix is non - invertible, please re-enter the matrix")
    else:
        print("The matrix is invertible")
        inv_mat = np.array(np.linalg.inv(mat))
        return inv_mat

def dotProduct(Imat, Sln_Vector):
    ans_vector = np.dot(Imat, Sln_Vector)
    return ans_vector

def GaussElimination(matrix, size, v):
    i_m = inverseMatrix(matrix)
    V = dotProduct(i_m, v)
    return(V)

