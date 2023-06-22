n = int(input())

d = []
x = 0
y = 0
for i in range(n):
    z = input().split(' ')
    d.extend(z)

for i in range(len(d)):
    if i % 2 != 0:
        d[i] = int(d[i])
for i in range(len(d)):
    if d[i] == 'север':
        y += d[i+1]
    if d[i] == 'юг':
        y -= d[i+1]
    if d[i] == 'восток':
        x += d[i+1]
    if d[i] == 'запад':
        x -= d[i+1]

print(x, y)