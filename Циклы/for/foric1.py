n = int(input())
m = int(input())
c = int(input())
t = int(input())


# print('\n\n\n\n')
arr = ["    "]
for w in range(c, t+1):
    arr.append(w)

for x in arr:
    print(x, end = "\t")
print() 


for i in range(n, m+1):
    print(i, end = '\t')
    for j in range(c, t+1):
        print(i*j, end= "\t")
    print()

"""
a = int(input().strip())
b = int(input().strip())
c = int(input().strip())
d = int(input().strip())

print('\t', end='')
for i in range(c, d+1):
    print(i, '\t', end='')
print()

for i in range(a, b+1):
    print(i, '\t', end='')
    for j in range(c, d+1):
        print(i*j, '\t', end='')
    print()
"""