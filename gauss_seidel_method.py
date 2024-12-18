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

################ Helper Functions #############

# This helper function takes a corrected matrix, size, corrected solution vector,
# number of iterations, and starting vector (optional) and applies the Gauss-Seidel method.
def gauss(matrix, size, v, iterations, strt_value=None):
    if strt_value is None:                          # No initial vector passed, start from zero vector
        x = np.zeros(size, dtype=float)
    elif np.isscalar(strt_value):                   # If initial guess is a single number, initialize all elements with it
        x = np.full(size, strt_value, dtype=float)
    else:                                           # Otherwise, use the provided starting vector
        x = np.array(strt_value, dtype=float)

    # Store the solution progress for plotting
    solution_progress = [x.copy()]

    # Iterative process for Gauss-Seidel method
    for k in range(iterations):                     # Repeats for the number of times required
        for i in range(size):                       # Loop through rows
            # Sum the terms for the ith equation except the diagonal term
            summ = 0.0
            for j in range(size):                   # Loop through columns
                if j != i:                          # Exclude diagonal element
                    summ += matrix[i][j] * x[j]     # Summation of terms

            # Update the ith value using the most recent values
            x[i] = (v[i].item() - summ) / matrix[i][i].item()

        solution_progress.append(x.copy())  # Record solution at each iteration

    return x, solution_progress  # Return answer vector and progress


# Function to plot the convergence of solutions
def plot_convergence(solution_progress):
    """
    Plots the solution values at each iteration to show convergence.
    """
    iterations = len(solution_progress)
    solution_progress = np.array(solution_progress).T  # Transpose for easier plotting

    plt.figure(figsize=(8, 6))
    for i, solution in enumerate(solution_progress):
        plt.plot(range(iterations), solution, marker='o', linestyle='-', label=f'Variable {i+1}')

    plt.title("Convergence of Gauss-Seidel Method")
    plt.xlabel("Iteration")
    plt.ylabel("Solution Values")
    plt.legend()
    plt.grid(True)
    plt.show()


################ Main Function ################

def gauss_seidel_method(matrix, v, iterations, starting_values=None):
    """
    This function solves a matrix using the Gauss-Seidel method.
    It also plots the convergence of the solution.
    """
    mat, vect, size = m_h_f.diagonally_dominate(matrix, v)  # Call of Helper function 1
    ans_vect, solution_progress = gauss(mat, size, vect, iterations, starting_values)  # Call of Helper function 2

    # Plot convergence of solutions
    plot_convergence(solution_progress)

    return ans_vect  # Return answer vector

###############################################
################## The End ####################
###############################################
