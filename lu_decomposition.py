###############################################
############## LU decomposition ###############
###############################################
# - This file has 2 helper functions          #
# - This file has 1 main function             #
# - The main function calls the two helper    #
#   functions solving the given matrix using  #
#   LU decomposition method                   #
###############################################
# Libraries used #
import numpy as np
import matplotlib.pyplot as plt
import math_helper_functions as m_h_f
import time

############## 2 Helper Functions #############

def lu_decomposition(matrix, size):     
    """
    Decomposes a matrix into L (lower triangular) and U (upper triangular) matrices.
    Tracks the progression for visualization.
    """
    # Convert the input to a NumPy array used format
    matrix = np.array(matrix, dtype=float)

    L = np.eye(size)  # Initialize L as an identity matrix
    U = matrix.copy()  # Copy the input matrix for U

    progression = [U.copy()]  # Track progression of U matrix during decomposition

    for i in range(size):       
        if U[i][i] == 0:
            raise ValueError(f"Pivot element U[{i}][{i}] is zero. Matrix is singular.")        

        for j in range(i + 1, size):        
            multiplier = U[j][i] / U[i][i]  
            L[j][i] = multiplier            

            # Update the row in U to zero out the element below the pivot
            U[j] = U[j] - multiplier * U[i]
            progression.append(U.copy())  # Track progression after each row operation

    return L, U, progression  


################### Plot Function ###################

def plot_lu_progression(progression):
    """
    Plots the progression of the U matrix as LU decomposition is performed.
    Each step shows the U matrix evolving towards upper triangular form.
    """
    num_steps = len(progression)
    fig, axes = plt.subplots(1, num_steps, figsize=(num_steps * 4, 4))

    if num_steps == 1:  # Handle single-step case
        axes = [axes]

    for idx, U_matrix in enumerate(progression):
        ax = axes[idx]
        cax = ax.matshow(U_matrix, cmap='viridis')
        fig.colorbar(cax, ax=ax)
        ax.set_title(f"Step {idx + 1}")
        ax.axis('off')

    plt.suptitle("LU Decomposition Progression (U Matrix)")
    plt.show()


################ Main Function ################

def lu(matrix, size, V):        

    L, U, progression = lu_decomposition(matrix, size)  

    # Plot the decomposition progression
    #plot_lu_progression(progression)       # Canceled 3ashan eh de ya me3alem

    # Calculate solution
    L_inverse = m_h_f.inverseMatrix(L)  
    U_inverse = m_h_f.inverseMatrix(U)  

    ans_vector = np.dot(U_inverse, np.dot(L_inverse, V))

    return ans_vector


###############################################
################## The End ####################
###############################################
