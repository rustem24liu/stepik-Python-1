"""
Вывести сумму всех нечетных числе от a до b (включая обе границы)
"""
n = int(input())
m = int(input())
sum = 0
for i in range(n, m+1):
    if i % 2 != 0:
        sum+=i
print(sum)

a, b = (input()).split()
a = int(a)
b = int(b)
sum1 = 0
if a % 2 == 0:
    a+=1
else:
    for i in range(a, b+1, 2):
        sum1+=i

print(sum)