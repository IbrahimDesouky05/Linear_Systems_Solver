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



def gs_vector():            

    choice = input("Do you want a starting vector? (y/n): ")         

    if choice == "y":
        v = entryVector()       
        return v



def InputMatrix():      

    mat, size = enrtyMatrix()       
    invertableFlag = invertibleMatrix(mat)     
    while invertableFlag:       
        mat, size = enrtyMatrix()
        invertableFlag = invertibleMatrix(mat)

    return mat, size       



def entryVector():     

    v = []      

    row = list(map(float, input("Enter the elements row by row, separated by spaces: ").split()))  # Convert space-separated input to a list of integers

    v.append(row)           
    v = np.array(v)        
    v = v.reshape(-1, 1)    

    return v        

