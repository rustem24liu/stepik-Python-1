arr = [str(i) for i in input().split()]
res = []
for x in arr:
    res.append(x.lower())

d = {}

for i in range(len(res)):
    if res[i] in d:
        d[res[i]] += 1
    else:
        d[res[i]] = 1

for key , value in d.items():
    print(key, value, sep = ' ')
