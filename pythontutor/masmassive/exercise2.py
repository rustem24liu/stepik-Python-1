n = int(input())
# arr= [[0]*n]*n
arr = [['.' for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] ='*'
        if i+j == len(arr)-1:
            arr[i][j] = '*'
        arr[i][n//2] = '*'
        arr[n//2][j] = '*'
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print() 