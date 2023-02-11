n = int(input())
m = int(input())

arr = []
for i in range(n, m+1):
    if i % 3 == 0:
        arr.append(i)
sum  = 0
for x in arr:
    sum += x
print(sum/len(arr))
