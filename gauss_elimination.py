import numpy as np

def inverseMatrix(mat):

        inv_mat = np.array(np.linalg.inv(mat))
        return inv_mat

def dotProduct(Imat, Sln_Vector):
    ans_vector = np.dot(Imat, Sln_Vector)
    return ans_vector

def GaussElimination(matrix, v):
    i_m = inverseMatrix(matrix)
    V = dotProduct(i_m, v)
    return(V)

