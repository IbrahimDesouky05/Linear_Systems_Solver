###############################################
############## LU decomposition ###############
###############################################
# - This file has 2 helper functions          #
# - This file has 1 main functions            #
# - The main Function calls the two helper    #
#   functions solving the given matrix using  #
#   LU decomposition method                   #
###############################################
# Libraries used #
import numpy as np
import math_helper_functions as m_h_f

############## 2 Helper Functions #############

def lu_decomposition(matrix, size):     # This helper function takes the matrix and its size and decomposes it into L and U matrices

    # Convert the input to a NumPy array used format
    matrix = np.array(matrix, dtype=float)

    L = np.eye(size)  # Initialize L as an identity matrix of given size
    U = matrix.copy()  # Copy the input matrix for U

    for i in range(size):       # Loops for columns

        if U[i][i] == 0:

            raise ValueError(f"Pivot element U[{i}][{i}] is zero. Matrix is singular.")        # Used before applying the input singularity check not currently needed

        # This section essentially does elementary row operations reducing the U matrix to a upper triangular matrix
        for j in range(i + 1, size):        # Loops for columns

            multiplier = U[j][i] / U[i][i]          # Calculates the multiplier for the current row
            L[j][i] = multiplier            # Saves the current multiplier in the L matrix

            # Update the row in U to zero out the element below the pivot
            U[j] = U[j] - multiplier * U[i]

    return L, U         # Returns the L and U matrices respectively



################ Main Function ################

def lu(matrix, size, V):        # This function utilizes the 2 helper functions to solve the given matrix using LU decomposition

    L, U = lu_decomposition(matrix, size)       # Call of Helper function 1

    L_inverse = m_h_f.inverseMatrix(L)        # Call of Helper function 1
    U_inverse = m_h_f.inverseMatrix(U)        # Call of Helper function 1

    ans_vector = np.dot(U_inverse, np.dot(L_inverse, V))        # Solving to get answer vector

    return ans_vector       # Return of answer vector

###############################################
################## The End ####################
###############################################