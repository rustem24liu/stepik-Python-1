'''n = int(input())
m = int(input())
arr = [[int(i) for i in input().split()]*m] * n

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = ' ')
    print()'''

'''n = int(input())
a = []
i = 1
while i != 0:
    a.append([int(j) for j in input().split()])
    
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()
'''

# n = int(input())
a = []
# for i in range(n):
i =1
while i != 0:
    row = input().split()
    if row == 'end':
        break
    else:
        for i in range(len(row)):
            if(type(row) == (str)):
                row[i] = int(row[i])
        if(type(row) != (str)):
            a.append(row)

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == 'end':
            continue
        else:
            print(a[i][j], end = ' ')
    print()