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
import matplotlib.pyplot as plt
import math_helper_functions as m_h_f

############## Helper Functions #############

# This helper function takes a corrected matrix, size, corrected solution vector,
# and the number of iterations, applying the Jacobi method and tracking progress.
def jacob(matrix, size, v, iterations):
    x = np.zeros(size)  # Initialize the initial vector as zero

    solution_progress = [x.copy()]  # Store solution progress for plotting

    # Iterative process
    for k in range(iterations):     # Repeat for the specified number of iterations
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
        solution_progress.append(x.copy())  # Store solution progress

    return x, solution_progress  # Return the final answer vector and progress


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

    plt.title("Convergence of Jacobi Method")
    plt.xlabel("Iteration")
    plt.ylabel("Solution Values")
    plt.legend()
    plt.grid(True)
    plt.show()


################ Main Function ################

def jacobian_method(matrix, v, iterations=3):
    """
    Solves a system of linear equations using the Jacobi method
    and plots the convergence of solutions.
    """
    mat, vect, size = m_h_f.diagonally_dominate(matrix, v)  # Call helper function
    ans_vect, solution_progress = jacob(mat, size, vect, iterations)  # Call helper function

    # Plot convergence of solutions
    plot_convergence(solution_progress)

    return ans_vect  # Return the final solution vector

###############################################
################## The End ####################
###############################################