import numpy as np

def enrtyMatrix():

    rows = int(input("Enter size of matrix"))

    matrix = []

    print("Enter the elements row by row, separated by spaces:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))  # Convert space-separated input to a list of integers
        while len(row) < rows:
            row.append(0)
        matrix.append(row)
    return matrix,rows

def invertableMatrix(mat):
    det = np.linalg.det(mat)
    if det == 0:
        return True
    else:
        return False


def InputMatrix():

    mat, size = enrtyMatrix()
    invertableFlag = invertableMatrix(mat)
    while invertableFlag:
        mat, size = enrtyMatrix()
        invertableFlag = invertableMatrix(mat)

    return mat, size


def inputVector():

    v = []

    row = list(map(float, input("Enter the elements row by row, separated by spaces:").split()))  # Convert space-separated input to a list of integers
    v.append(row)
    v = np.array(v)
    v = v.reshape(-1, 1)
    return v

def inputIterationCount():
    n = int(input("Enter number of iterations needed: "))
    return n

