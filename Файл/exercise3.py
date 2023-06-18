with open("input3.txt", "r", encoding="utf-8") as file:
    d = file.read().split('\n')

q = []
for i in range(len(d)):
    q.append(d[i].split(';'))

res1 = []
sum = 0
res2 = []
for i in range(len(q)):
    res1.append((int(q[i][1]) + int(q[i][2]) + int(q[i][3]))/3)
for j in range(1, 4):
    for i in range(len(q)):
        sum += int(q[i][j])
    res2.append(sum)
    sum = 0

out = open('output3.txt', 'w')

for i in range(len(res1)):
    print('%.9f' % res1[i], sep = '\n', file = out)

for i in range(len(res2)):
    res2[i] = res2[i]/len(q)
    
for i in range(len(res2)):
    print('%.9f' % float(res2[i]), end = ' ', file = out)



