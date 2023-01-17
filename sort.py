import math
a = int(input())
b = int(input())
c = int(input())
res1 = max(a, b, c)
res2 = min(a, b, c)
print(res1)
print(res2)
print(a+b+c-res1-res2)
# if a != res1 and a != res2:
#     print(res1)
#     print(res2)
#     print(a)
# elif b != res1 and b != res2:
#     print(res1)
#     print(res2)
#     print(b)
# elif c != res1 and c != res2:
#     print(res1)
#     print(res2)
#     print(c)
# elif a == res1 and a!= res2 and c != res1 and c == res2 and b == res1 and b != res2:
#     print(res1)
#     print(res2)
#     print(b)
# elif a == res1 and a!= res2 and b != res1 and b == res2 and c == res1 and c != res2:
#     print(res1)
#     print(res2)
#     print(c)
# elif b == res1 and b!= res2 and a != res1 and a == res2 and c == res1 and c != res2:
#     print(res1)
#     print(res2)
#     print(b)
# else:
#     print(a)
#     print(b)
#     print(c)