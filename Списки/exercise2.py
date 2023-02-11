i = 0
arr = [int(i) for i in input().split()]
res = []
if len(arr) == 1:
    print(arr[0])
else:
    for x in range(len(arr)):
        if x == 0:
            res.append(arr[x+1] + arr[len(arr)-1])
        elif x!=0 and x!=len(arr)-1:
            res.append(arr[x-1]+arr[x+1])
        elif x == len(arr)-1:
            res.append(arr[x-1]+arr[0])
    for y in res:
        print( y, end = ' ')