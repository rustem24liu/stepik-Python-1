'''
Даны размеры поля для игры в сапер и координаты мин,
стоящих на этом поле. Вывестиполе игры на экран.
'''
n, m, k = (int(i) for i in input().split())

arr = [[0 for j in range(m)] for i in range(n)]

for i in range(k):
    row, column  = (int(i) for i in input().split())
    arr[row-1][column-1] = -1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    if 0 <= ai < n and 0 <= aj < m:
                        if arr[ai][aj] == -1:
                            arr[i][j] += 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == -1:
            print('*', end = '')
        elif arr[i][j] == 0:
            print('.', end = '')
        else:
            print(arr[i][j], end = '')
    print()