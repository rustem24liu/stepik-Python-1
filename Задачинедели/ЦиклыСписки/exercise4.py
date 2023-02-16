i = 2
arr = []
while i != 0:
    row = input().split()
    if row == 'end':
        break
    else:
        for i in range(len(row)):
            if(type(row) == (str)):
                row[i] = int(row[i])
        if(type(row) != str):
            arr.append(row)
x = 'end'
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 'end':
            continue
        else:
            print(arr[i][j], end = ' ')
    print()
