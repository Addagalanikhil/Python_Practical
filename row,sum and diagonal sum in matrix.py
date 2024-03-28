def matrix_sum(matrix):
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(col) for col in zip(*matrix)]
    diag_sum = sum(matrix[i][i] for i in range(len(matrix)))

    for i in range(len(matrix)):
        print(f"Sum of {i + 1} row: {row_sums[i]}")
    
    for i in range(len(matrix[0])):
        print(f"Sum of {i + 1} column: {col_sums[i]}")
    
    print(f"Diagonal sum: {diag_sum}")

# Input Matrix
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# Calculate and Display Sums
matrix_sum(a)
