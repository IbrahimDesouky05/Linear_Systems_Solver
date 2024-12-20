###############################################
############### Input Handler #################
###############################################
# - This file has helper functions that       #
#   allows program to handle input            #
###############################################
# Libraries used #
import numpy as np


def enrtyMatrix():     
    
    rows = int(input("Enter size of matrix: "))       

    matrix = []         

    print("Enter the elements row by row, separated by spaces: ")

    for i in range(rows):      

        row = list(map(int, input(f"Row {i+1}: ").split()))  

        while len(row) < rows: 
            row.append(0)

        matrix.append(row)      
        
    return matrix,rows          



def invertibleMatrix(mat):      

    det = np.linalg.det(mat)        
    # If determinant  = 0       -----> Matrix Not Invertible
    # If determinant  =! 0       -----> Matrix Invertible

    if det == 0:
        return True
    else:
        return False



def iterationNumber():     

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

