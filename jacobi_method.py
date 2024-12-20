###############################################
################## Jacobian ###################
###############################################
# - This file has a helper function           #
# - This file has 1 main function             #
# - The main function calls the helper        #
#   function solving the given matrix using   #
#   Jacobi Iterative Method                   #
###############################################
# Libraries used #
import numpy as np
import math_helper_functions as m_h_f
import time

############## Helper Functions #############

# This helper function takes a corrected matrix, size, corrected solution vector,
# and the number of iterations, applying the Jacobi method and tracking progress.
def jacob(matrix, size, v, exact_sln, strt_value=None):

    if strt_value is None:  # No initial vector passed, start from zero vector
        x = np.zeros(size, dtype=float)
    elif np.isscalar(strt_value):  # If initial guess is a single number, initialize all elements with it
        x = np.full(size, strt_value, dtype=float)
    else:  # Otherwise, use the provided starting vector
        x = np.array(strt_value, dtype=float)

    # Stopping flag
    flag = True

    solution_progress = [x.copy()]  # Store solution progress for plotting

    # Iterative process
    while flag:     # Repeat for the specified number of iterations

        x_new = np.copy(x)          # Copy the starting conditions

        for i in range(size):       # Loop through rows
            # Sum the terms for the ith equation except the diagonal term
            summ = 0
            for j in range(size):   # Loop through columns
                if j != i:          # Exclude diagonal element
                    summ += matrix[i][j] * x[j]

            # Update the ith value
            x_new[i] = (v[i].item() - summ) / matrix[i][i].item()

        # Update the solution for the next iteration
        x = np.copy(x_new)

        flag = m_h_f.check_done(size, exact_sln, x)
        solution_progress.append(x.copy())  # Store solution progress

    return x, solution_progress  # Return the final answer vector and progress


################ Main Function ################

def jacobian_method(matrix, v, exact_sln, strt_value=None):

    mat, vect, size = m_h_f.diagonally_dominate(matrix, v)  # Call helper function
    ans_vect, solution_progress = jacob(mat, size, vect,exact_sln,strt_value)  # Call helper function

    iteration_count = len(solution_progress)

    # Plot convergence of solutions
    m_h_f.plot_convergence(solution_progress, "Convergence of Jacobian Method")


    return ans_vect, iteration_count # Return the final solution vector

