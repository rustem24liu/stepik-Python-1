n, m = (input().split())
n  = int(n)
m  = int(m)
arr = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    arr.append(row)
maxi = -9999999999
resx = 0
resy = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if(maxi < arr[i][j]):
            maxi = arr[i][j]
            resx = i
            resy = j

print(resx, resy)
for i in range(len(arr)):
    for j in range(len(arr[i])):
                pass
