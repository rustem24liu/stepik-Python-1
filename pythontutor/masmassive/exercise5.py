n = int(input())
arr = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if i + j == n-1:
            arr[i][j] = 1
        elif (i+j) >= n:
            arr[i][j] = 2
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()