n = input()
m = input()
k = input()
l = input()
lst1 = []
lst2 = []
result1 = ''
result2 = ''
for i in range(len(n)):
    lst1.append(n[i])
    lst2.append(m[i])

for i in range(len(k)):
    for j in range(len(lst1)):
        if k[i] == lst1[j]:
            result1+=lst2[j]
for i in range(len(l)):
    for j in range(len(lst2)):
        if l[i] == lst2[j]:
            result2+=lst1[j]
print(result1)
print(result2)

