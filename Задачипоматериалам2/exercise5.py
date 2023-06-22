with open('input.txt', 'r', encoding='utf-8') as file:
    d = file.read().split('\n')

lst = []
q = {}

for i in range(len(d)):
    lst.append(d[i].split('\t'))

for i in range(len(lst)-1, -1, -1):
    if lst[i][0].isdigit() and 1 <= int(lst[i][0]) <= 11:
        key = int(lst[i][0])
        value = int(lst[i][2])
        if key in q:
            q[key].append(value)
        else:
            q[key] = [value]

out = open('output.txt', 'w')

for k in range(1, 12):
    if k in q:
        mean = sum(q[k]) / len(q[k])
        print(k, mean, end=' ', file=out)
    else:
        print(k, '-', end=' ', file=out)
    print(file=out)

out.close()
