###############################################
############ Math Helper Function #############
###############################################
# - This file has a helper function used by   #
#   iterative methods                         #
###############################################
# Libraries used #
import numpy as np


def inverseMatrix(mat):  # This function receives a matrix that we have already checked in input function is invertible

    inv_mat = np.array(np.linalg.inv(mat))  # Gets the inverse of the matrix

    return inv_mat  # Returns the inverse of the matrix



def diagonally_dominate(m, v):      # This helper function makes the matrix given diagonally dominant
    m = np.array(m)         # Makes sure that the matrix given is in the required format
    v = np.array(v)         # Makes sure that the vector given is in the required format

    n = np.hstack((m, v))   # Appends the vector to the end of the matrix so that when the rows inter change they vector values are updated
    k = len(m)              # Gets the number of rows in the matrix
    # NB:: n is now the matrix that contains the (matrix + solution vector) that we are going to work on

    # This loop takes the diagonal element and checks that it is bigger than the sum of the other elements in this row, if not it inter-changes the rows with a row that has the diagonal element bigger than the sum of the other elements in this row
    for i in range(k):                                          # iterates for the columns
        if abs(m[i][i]) < abs(np.sum(m[i])):                    # Checks for the diagonally dominant condition
            for j in range(i + 1, k):                           # iterates for the rows
                if abs(m[j][i]) > abs(np.sum(m[j]) - m[j][i]):  # Checks that |diagonal value| > |Sum(all row elements except diagonal one)|
                    n[j], n[i] = n[i].copy(), n[j].copy()       # Interchanging the required rows

    v = n[:,k]                                                  # Extracts the solution vector again
    n = n[:,:-1]                                                # Removes the solution vector from the corrected matrix

    return n, v, k      # Returns the corrected matrix, corrected vector, size respectively

###############################################
################## The End ####################
###############################################