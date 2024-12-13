###############################################
############### Gaussian Seidel ###############
###############################################
# - This file has a helper functions          #
# - This file has 1 main functions            #
# - The main Function calls the two helper    #
#   functions solving the given matrix using  #
#   Gaussian Seidel Iterative                 #
###############################################
# Libraries used #
import numpy as np
import math_helper_functions as m_h_f

################ Helper Functions #############

# This helper function takes corrected matrix, size, corrected solution vector, number of iterations needed, if needed(starting vector) respectively and applies gauss seidel method to it returning answer vector
def gauss(matrix, size, v, iterations, strt_value = None):

    if strt_value is None:                          # Checks that There isn't any passed initial vector, if none is passed it starts from zero vector
        x = np.zeros(size, dtype=float)
    elif np.isscalar(strt_value):                   # If initial_guess is a single number, it completes the rest as zeros
        x = np.full(size, strt_value, dtype=float)
    else:                                           # Otherwise, a starting vector is given
        x = np.array(strt_value, dtype=float)

    # Iterative process for gauss seidel method
    for k in range(iterations):     # Repeats for the number of times required by the user
        for i in range(size):       # Loops for rows
            # Sum the terms for the ith equation except the diagonal term
            summ = 0.0
            for j in range(size):   # Loops for columns
                if j != i:          # Checks for diagonal element
                    summ += matrix[i][j] * x[j]     # Summation multiplied by the values of initial vector

            # Update the ith value using the most recent values
            x[i] = (v[i].item() - summ) / matrix[i][i].item()

    return x        # Return answer vector


################ Main Function ################

def gauss_seidel_method(matrix, v, iterations,starting_values = None):      # This function utilizes the 2 helper functions to solve the given matrix using gauss seidel

    mat, vect, size = m_h_f.diagonally_dominate(matrix, v)                        # Call of Helper function 1
    ans_vect = gauss(mat, size, vect, iterations,starting_values)           # Call of Helper function 2

    return ans_vect         # Return of answer vector

###############################################
################## The End ####################
###############################################