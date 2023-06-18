n, m = [int(i) for i in input().split()]
arr = [[int(j) for j in input().split()] for i in range(n) ]
a, b = [int(j) for j in input().split()]

def doks(arr, a, b):
    for i in range(len(arr)):
        arr[i][a] , arr[i][b] = arr[i][b] , arr[i][a]

doks(arr, a, b)

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()