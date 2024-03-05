def fundamental_spaces(matrix):
    # Convert the matrix to NumPy array
    A = np.array(matrix)
    
    # Column space
    column_space_dim = np.linalg.matrix_rank(A)
    
    # Null space
    null_space_dim = A.shape[1] - column_space_dim
    
    # Row space (same as column space of the transpose)
    row_space_dim = np.linalg.matrix_rank(A.T)
    
    # Left null space (null space of the transpose)
    left_null_space_dim = A.shape[0] - row_space_dim
    
    return {
        "Row space dimension": row_space_dim,
        "Column space dimension": column_space_dim,
        "Null space dimension": null_space_dim,
        "Left null space dimension": left_null_space_dim
    }
# Input matrix here
matrix = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

spaces = fundamental_spaces(matrix)
for space, dim in spaces.items():
    print(f"{space}: {dim}")
