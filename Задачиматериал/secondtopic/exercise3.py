

arr = [str(i) for i in input().split()]
n = input()
length = arr.count(n)
res = []

for i in range(length):
    if len(res) == 0:
        res.append(arr.index(n))
        arr.pop(int(arr.index(n)))
    elif 0 <= len(res) < length:
        res.append(int(arr.index(n))+i)
        arr.pop(int(arr.index(n)))
    elif len(res) == length:
        res.append(int(arr.index(n)+i))
        arr.pop(int(arr.index(n)))
if len(res) == 0:
    print("Отсутствует")
else:
    for i in range(len(res)):
        print(res[i], end = ' ')

# print(res)

