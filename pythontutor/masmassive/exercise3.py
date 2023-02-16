n , m = input().split()
n = int(n)
m = int(m)
arr = [['.' for j in range(m)] for i in range(n)]
if n % 2 !=0:
    c = m-1
    for i in range(n):
        for j in range(m):
            while c != 0:
                arr[i][c-1] = '*'
                c-=1
        

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
        # print(i, end = ' ')
        # print(j, end = ' ')
    print()