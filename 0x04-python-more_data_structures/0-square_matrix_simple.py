#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    # Iterate over the elements in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Square the element and store it in the new matrix
             new_matrix[i][j] = matrix[i][j] ** 2
     return new_matrix

