###############################################
############### Gaussian Seidel ###############
###############################################
# - This file has helper functions            #
# - This file has 1 main function             #
# - The main function calls the two helper    #
#   functions solving the given matrix using  #
#   Gaussian Seidel Iterative method          #
###############################################
# Libraries used #
import numpy as np
import matplotlib.pyplot as plt
import math_helper_functions as m_h_f
import time

################ Helper Functions #############

# This helper function takes a corrected matrix, size, corrected solution vector,
# number of iterations, and starting vector (optional) and applies the Gauss-Seidel method.
def gauss(matrix, size, v, exact_sln, strt_value=None):
    if strt_value is None:                          # No initial vector passed, start from zero vector
        x = np.zeros(size, dtype=float)
    elif np.isscalar(strt_value):                   # If initial guess is a single number, initialize all elements with it
        x = np.full(size, strt_value, dtype=float)
    else:                                           # Otherwise, use the provided starting vector
        x = np.array(strt_value, dtype=float)

    # Stopping Flag
    flag = True

    # Store the solution progress for plotting
    solution_progress = [x.copy()]

    # Iterative process for Gauss-Seidel method
    while flag:                     # Repeats for the number of times required

        for i in range(size):                       # Loop through rows
            # Sum the terms for the ith equation except the diagonal term
            summ = 0.0
            for j in range(size):                   # Loop through columns
                if j != i:                          # Exclude diagonal element
                    summ += matrix[i][j] * x[j]     # Summation of terms

            # Update the ith value using the most recent values
            x[i] = (v[i].item() - summ) / matrix[i][i].item()

        flag = m_h_f.check_done(size, exact_sln, x)
        solution_progress.append(x.copy())  # Record solution at each iteration

    return x, solution_progress  # Return answer vector and progress


################ Main Function ################

def gauss_seidel_method(matrix, v, exact_sln, starting_values=None):

    mat, vect, size = m_h_f.diagonally_dominate(matrix, v)  # Call of Helper function 1
    ans_vect, solution_progress = gauss(mat, size, vect, exact_sln, starting_values)  # Call of Helper function 2

    iteration_count = len(solution_progress)

    # Plot convergence of solutions
    m_h_f.plot_convergence(solution_progress, "Convergence of Gauss-Seidel Method")


    return ans_vect, iteration_count # Return answer vector

###############################################
################## The End ####################
###############################################
