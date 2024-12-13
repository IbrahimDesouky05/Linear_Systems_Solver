###############################################
################## Jacobian ###################
###############################################
# - This file has a helper function           #
# - This file has 1 main functions            #
# - The main Function calls the two helper    #
#   functions solving the given matrix using  #
#   Jacobi Iterative                          #
###############################################
# Libraries used #
import numpy as np
import math_helper_functions as m_h_f

############## Helper Functions #############

# This helper function takes corrected matrix, size, corrected solution vector, number of iterations needed, respectively and applies jacobian method to it returning answer vector
def jacob(matrix, size, v, iterations):

    # Important Note:: After following multiple guides when using the jacobian method all guides use the initial vector as zero vector
    x = np.zeros(size)      # Initializing the initial Vector

    # Iterative process
    for k in range(iterations):     # Repeats for the number of times required by the user
        x_new = np.copy(x)          # Copies the starting conditions

        for i in range(size):       # Loops for rows
            # Sum the terms for the ith equation except the diagonal term
            summ = 0
            for j in range(size):   # Loops for columns
                if j != i:          # Checks for diagonal element
                    summ += matrix[i][j] * x[j]     # Summation multiplied by the values of initial vector

            # Update the ith value
            x_new[i] = (v[i].item() - summ) / matrix[i][i].item()

        # Update the solution for the next iteration
        x = np.copy(x_new)

    return x        # Return answer vector

################ Main Function ################

def jacobian_method(matrix, v, iterations = 3):             # This function utilizes the 2 helper functions to solve the given matrix using jacobian method

    mat, vect, size = m_h_f.diagonally_dominate(matrix, v)        # Call of Helper function 1
    ans_vect = jacob(mat, size, vect, iterations)           # Call of Helper function 2

    return ans_vect         # Return of answer vector

###############################################
################## The End ####################
###############################################


