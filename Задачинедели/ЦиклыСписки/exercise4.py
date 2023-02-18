arr =[]

while True:
    row = input()
    if row == 'end':
        break
    res = []
    for i in row.split():
        res.append(int(i))
    arr.append(res)

new = [[0 for j in range(len(arr[i]))] for i in range(len(arr))]

for i in range(len(arr)):
    for j in range(len(arr[i])):    

        if len(arr) == 1 and len(arr[i]) == 1:
            new[i][j] = arr[i][j]*4
        if(i == 0 and j == 0 and len(arr) != 1 and len(arr[i]) != 1):
            new[0][0] = arr[i][j+1] + arr[i+1][j] + arr[len(arr)-1][j] + arr[i][len(arr[i])-1]

        if(i == 0 and j == len(arr[i])-1 and len(arr) != 1 and len(arr[i]) != 1):
            new[0][len(arr[i])-1] = arr[i][j-1] + arr[i+1][j] + arr[len(arr)-1][len(arr[i])-1] + arr[0][0]

        if(i == len(arr)-1 and j == 0 and len(arr) != 1 and len(arr[i]) != 1):
            new[len(arr)-1][0] = arr[len(arr)-i-1][len(arr)-i-1]+ arr[i][j+1]+arr[i-1][j]+arr[i][len(arr[i])-1]

        if((i == len(arr)-1) and j == len(arr[i])-1 and len(arr) != 1 and len(arr[i]) != 1):
            new[len(arr)-1][len(arr[i])-1] = arr[i][j-1]+arr[i-1][j] + arr[len(arr)-1-i][len(arr[i])-1] + arr[len(arr)-1][len(arr[i])-1-j]

    
        if j == 0 and i != 0 and i != len(arr)-1 and len(arr) != 1 and len(arr[i]) != 1:
            new[i][j] = arr[i-1][j] + arr[i+1][j] + arr[i][j+1] + arr[i][len(arr[i])-1]

        if i == 0 and j != 0 and j != len(arr[i])-1 and len(arr) != 1 and len(arr[i]) != 1:
            new[i][j] = arr[i][j-1]+arr[i][j+1]+arr[i+1][j]+arr[len(arr)-1][j]

        if i == len(arr)-1 and j != 0 and j != len(arr[i])-1 and len(arr) != 1 and len(arr[i]) != 1:
            new[i][j] = arr[i][j-1]+ arr[i][j+1] + arr[i-1][j]+arr[0][j]

        if j == len(arr[i])-1 and i != len(arr)-1 and i != 0 and len(arr) != 1 and len(arr[i]) != 1:
            new[i][j] = arr[i-1][j] +  arr[i+1][j]+arr[i][j-1]  + arr[i][0]
        if((i != 0 and j != 0 and i != 0 and j != len(arr[i])-1 and i != len(arr)-1 and j != 0  and i != len(arr)-1) and j != len(arr[i])-1 and len(arr) != 1 and len(arr[i]) != 1):
            new[i][j] = arr[i][j+1] + arr[i][j-1] + arr[i-1][j] + arr[i+1][j]
        if i == 0 and len(arr) == 1 and len(arr[i]) > 1:
            # print(i, j, end  = " " )
            # print(arr[i][j], sep = '')
            if(i == 0 and j == 0):
                new[i][j] = (arr[i][j] + arr[i][j]) +arr[i][j+1] + arr[i][len(arr[i])-1]
            if(i == 0 and j == len(arr[i])-1):
                new[i][j] = arr[i][j]+arr[i][j]+arr[i][j-1]+arr[i][0]
            if i == 0 and j != len(arr[i])-1:
                new[i][j] = arr[i][j]+arr[i][j]+arr[i][j-1]+arr[i][j+1]
        if j == 0 and len(arr[i]) == 1 and len(arr) >1:
            if i == 0 and j == 0:
                new[i][j] = arr[i][j]+arr[i][j] + arr[len(arr)-1][j]+arr[i+1][j]
            if i == len(arr)-1 and j == 0:
                new[i][j] = arr[i][j]+arr[i][j]+arr[0][j]+arr[i-1][j]
            if j == 0 and i != 0 and i != len(arr)-1:
                new[i][j] = arr[i][j]+arr[i][j]+arr[i-1][j]+arr[i+1][j]
for i in range(len(new)):
    for j in range(len(new[i])):
        print(new[i][j], end = ' ')
    print()