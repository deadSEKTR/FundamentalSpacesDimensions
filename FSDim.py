import numpy as np

def calculate_subspace_dimensions(matrix):
    # Get the number of rows and columns of the matrix
    m, n = matrix.shape
    
    # Calculate the rank of the matrix
    rank = np.linalg.matrix_rank(matrix)
    
    # Calculate the dimension of the column space
    col_space_dim = rank
    
    # Calculate the dimension of the null space
    null_space_dim = n - rank
    
    # Calculate the dimension of the row space
    row_space_dim = rank
    
    # Calculate the dimension of the left null space
    left_null_space_dim = m - rank
    
    return col_space_dim, null_space_dim, row_space_dim, left_null_space_dim

# Example usage
matrix = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0]])

col_dim, null_dim, row_dim, left_null_dim = calculate_subspace_dimensions(matrix)

print("Dimension of the column space:", col_dim)
print("Dimension of the null space (nullity):", null_dim)
print("Dimension of the row space:", row_dim)
print("Dimension of the left null space (left nullity):", left_null_dim)
