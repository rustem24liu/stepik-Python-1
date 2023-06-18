n, m = input().split()
n = int(n)
m = int(m)
arr = [['.' for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if (i+j) % 2 != 0:
            arr[i][j] = '*'

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()