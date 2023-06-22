x = int(input())

lst1 = []
lst2 = []
set1 = set()
set2 = set()

for i in range(x):
    d = input().lower().split(' ')
    lst1.extend(d)

y = int(input())

for i in range(y):
    q = input().lower().split(' ')
    lst2.extend(q)

for i in range(len(lst1)):
    set1.add(lst1[i])
for i in range(len(lst2)):
    set2.add(lst2[i])
    
answer = set2.difference(set1)
for x in answer:
    print(x)