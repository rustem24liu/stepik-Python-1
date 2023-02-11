i = 0
while i < 5:
    a, b, = input().split()
    a = int(a)
    b = int(b)
    # a = int(input())
    # b = int(input())
    if a == 0 and b== 0:
        break

    print(a*b)
    i+=1