# s = []
with open('input2.txt', "r") as file:
    s = file.read().split()

d = {}


for i in range(len(s)):
    s[i] = s[i].lower()
    x = s.count(s[i])
    d[s[i]] = x

q = []
res = {}
maxi = max(d.values())

for i, j in d.items():
    if j == maxi:
        res[i] = j
# print(res)
maxi2 = min(res.keys())

# print(maxi2, maxi)

with open("output2.txt", "w") as out:
    out.write(maxi2)
    out.write(' ')
    out.write(str(maxi))


