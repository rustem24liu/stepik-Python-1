q =(input())
x = int(q)

a = x/10

b = x/100



res1 = int(q[0])+int(q[1])+int(q[2])
res2 = x%10 + int(a%10)+ int(b%10)
# print(res1)
# print(res2)
if res1 == res2:
    print("Счастливый")
else:
    print("Обычный")
