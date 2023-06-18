n = int(input())
arr = [[0 for j in range(n)] for i in range(n)]

cnt = 1
f = 0
m = 1
k = 0
while cnt <= n:
    for i in range(n):
        for j in range(i):
            if abs(i - j) == cnt:
                arr[i][j] = cnt
                arr[j][i] = cnt
    cnt+=1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()