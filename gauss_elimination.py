###############################################
############# Gaussian Elimination ############
###############################################
# - This file has a helper functions          #
# - This file has 1 main functions            #
# - The main Function calls the two helper    #
#   functions solving the given matrix using  #
#   Gaussian Elimination                      #
###############################################
# Libraries used #
import numpy as np
import math_helper_functions as m_h_f
import numpy as np
import matplotlib.pyplot as plt
import math_helper_functions as m_h_f

############## a Helper Functions #############

def dotProduct(Imat, Sln_Vector):       # This function multiplies the inverted matrix by the solution vector and returns the answer vector

    ans_vector = np.dot(Imat, Sln_Vector)       # The multiplication step of inverted matrix and the solution vector
    return ans_vector       # Returns the answer vector
############## Plotting Iterations Function 
def plot_iterations_vs_efficiency(iterations, efficiencies):
    """
    Plots the number of iterations against efficiency.
    """
    plt.figure(figsize=(8, 6))
    plt.plot(iterations, efficiencies, marker='o', linestyle='-', color='b')
    plt.title("Gaussian Elimination: Iterations vs Efficiency")
    plt.xlabel("Number of Iterations")
    plt.ylabel("Efficiency (%)")
    plt.grid(True)
    plt.show()
################ Main Function ################
def GaussElimination(matrix, v):        # This function utilizes the 2 helper functions to solve the given matrix using gaussian elimination

    i_m = m_h_f.inverseMatrix(matrix)         # Call of Helper function 1
    V = dotProduct(i_m, v)              # Call of Helper function 2

    return(V)       # Return of answer vector

###############################################
################## The End ####################
###############################################