n = int(input())

arr = [[-1 for j in range(n)] for i in range(n)]

cnt = 1
f = 0
k = 1
while n*n >= cnt:
    for i in range(n):
        if(arr[f][i] == -1):
            arr[f][i] = cnt
            cnt+=1
    for i in range(k, n):
        if(arr[i][n-f-1] == -1):
            arr[i][n-f-1] = cnt
            cnt+=1
    for i in range(f, n):
        if(arr[n-f-1][n-i-1] == -1):
            arr[n-f-1][n-i-1] = cnt
            cnt+=1
    for i in range(f, n):
        if(arr[n-i-1][f] == -1):
            arr[n-i-1][f] = cnt
            cnt+=1
    f+=1
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()