''''a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a[1])
print(a[1][2])'''

# Generation

n = 3
a = [[0]*n for i in range(n)]
print(a[0][0])
a[0][0] = 5

for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j], end = ' ')
    print()

