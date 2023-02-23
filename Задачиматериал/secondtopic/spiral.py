

n = int(input())

arr = [[-1 for j in range(n)] for i in range(n)]

cnt = 1

row_start = 0
row_end = n-1
column_start = 0
column_end = n-1
while row_start <= row_end and column_start <= column_end:
    for i in range(column_start, column_end+1):
        arr[row_start][i] = cnt
        cnt+=1
    row_start+=1
    for i in range(row_start, row_end+1):
        arr[i][column_end] = cnt
        cnt+=1
    column_end-=1
    for i in range(column_end, column_start-1, -1):
        arr[row_end][i] = cnt
        cnt+=1
    row_end-=1
    for i in range(row_end, row_start-1, -1):
        arr[i][column_start] = cnt
        cnt+=1
    column_start+=1
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()