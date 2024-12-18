###############################################
############### Input Handler #################
###############################################
# - This file has helper functions that       #
#   allows program to handle input            #
###############################################
# Libraries used #
import numpy as np


def enrtyMatrix():      # This function allows user to enter a matrix

    rows = int(input("Enter size of matrix: "))       # Inputs the matrix size

    matrix = []         # Initializes an empty matrix

    print("Enter the elements row by row, separated by spaces: ")

    for i in range(rows):       # Loops for each row

        row = list(map(int, input(f"Row {i+1}: ").split()))  # Convert space-separated input to a list of integers (row)

        while len(row) < rows:  # If no value is added it completes it with zeros
            row.append(0)

        matrix.append(row)      # Adds the entered row to the matrix

    return matrix,rows          # Returns the matrix, size respectively



def invertibleMatrix(mat):      # This function checks if the matrix is singular

    det = np.linalg.det(mat)        # Checking determinant to check for the singularity of matrix

    # If determinant  = 0       -----> Matrix Not Invertible
    # If determinant  =! 0       -----> Matrix Invertible

    if det == 0:
        return True
    else:
        return False



def iterationNumber():      # Allows User to input the number of iterations needed

    i = int(input("Enter number of iterations needed for iterative methods: "))

    return i



def gs_vector():            # Allows User to choice whether he needs initial vector

    choice = input("Do you want a starting vector? (y/n): ")         # Takes User choice

    if choice == "y":
        v = entryVector()       # Calls input vector function to input vector
        return v



def InputMatrix():      # This function utilizes the entryMatrix, invertibleMatrix functions to enter the function only and then does the needed checks on it

    mat, size = enrtyMatrix()       # Call of entryMatrix function
    invertableFlag = invertibleMatrix(mat)      # Checks whether the matrix is invertible or not

    while invertableFlag:       # Loops until user enters a usable matrix
        mat, size = enrtyMatrix()
        invertableFlag = invertibleMatrix(mat)

    return mat, size        # Returns  matrix, size respectively



def entryVector():      # This function allows user to input a vector

    v = []      # Initializes an empty Vector

    row = list(map(float, input("Enter the elements row by row, separated by spaces: ").split()))  # Convert space-separated input to a list of integers

    v.append(row)           # Adds the input data to the empty vector
    v = np.array(v)         # Converts the vector to the standard format
    v = v.reshape(-1, 1)    # Flips the Vector so that it can be used correctly

    return v        # Returns the vector

###############################################
################## The End ####################
###############################################
