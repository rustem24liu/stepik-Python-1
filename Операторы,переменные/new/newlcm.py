a = int(input())
b = int(input())
res = a

while res % b != 0:
    res += a

print(res)