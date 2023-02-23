a = {}
for i in range(int(input())):
    b = int(input())
    if b not in a:
        a[b] = f(b)
    print(a[b])