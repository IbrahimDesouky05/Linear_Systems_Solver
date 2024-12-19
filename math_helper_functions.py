###############################################
############ Math Helper Function #############
###############################################
# - This file has a helper function used by   #
#   iterative methods                         #
###############################################
# Libraries used #
import numpy as np
import matplotlib.pyplot as plt

def inverseMatrix(mat):  # This function receives a matrix that we have already checked in input function is invertible

    inv_mat = np.array(np.linalg.inv(mat))  # Gets the inverse of the matrix

    return inv_mat  # Returns the inverse of the matrix



def diagonally_dominate(m, v):      # This helper function makes the matrix given diagonally dominant
    m = np.array(m)         # Makes sure that the matrix given is in the required format
    v = np.array(v)         # Makes sure that the vector given is in the required format

    v = v.reshape(-1,1)     # VERY IMPORTANT This line allows the conversion between the format of the GUI and the Format of the math functions
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

def check_done(size, exact_sln, current_sln):

    count = 0
    stop_crit = 0.00005

    for i in range (size):
        error_value = (exact_sln[i] - current_sln[i]) / exact_sln[i]
        if abs(error_value) <= abs(stop_crit):
            count = count + 1

    if count == size:
        return False

    return True

# Function to plot the convergence of solutions
def plot_convergence(solution_progress, title):

    iterations = len(solution_progress)
    solution_progress = np.array(solution_progress).T  # Transpose for easier plotting

    plt.figure(figsize=(8, 6))
    for i, solution in enumerate(solution_progress):
        plt.plot(range(iterations), solution, marker='o', linestyle='-', label=f'Variable {i+1}')

    plt.title(title)
    plt.xlabel("Iteration")
    plt.ylabel("Solution Values")
    plt.legend()
    plt.grid(True)
    #plt.show()         # Used in debugging
    plt.savefig(title)


def invertibleMatrix(mat):      # This function checks if the matrix is singular

    det = np.linalg.det(mat)        # Checking determinant to check for the singularity of matrix

    # If determinant  = 0       -----> Matrix Not Invertible
    # If determinant  =! 0       -----> Matrix Invertible

    if det == 0:
        return True
    else:
        return False

###############################################
################## The End ####################
###############################################