n = 5  # size of the matrix
matrix = [[0] * n for i in range(n)]  # initialize the matrix with zeros

count = 1  # variable to keep track of the current value to insert in the matrix
row_start = 0  # starting row index
row_end = n - 1  # ending row index
col_start = 0  # starting column index
col_end = n - 1  # ending column index

while row_start <= row_end and col_start <= col_end:
    # fill the top row from left to right
    for i in range(col_start, col_end + 1):
        matrix[row_start][i] = count
        count += 1
    row_start += 1
    
    # fill the right column from top to bottom
    for i in range(row_start, row_end + 1):
        matrix[i][col_end] = count
        count += 1
    col_end -= 1
    
    # fill the bottom row from right to left
    for i in range(col_end, col_start - 1, -1):
        matrix[row_end][i] = count
        count += 1
    row_end -= 1
    
    # fill the left column from bottom to top
    for i in range(row_end, row_start - 1, -1):
        matrix[i][col_start] = count
        count += 1
    col_start += 1

# print the matrix
for row in matrix:
    print(row)
