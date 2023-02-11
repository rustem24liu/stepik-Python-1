x = int(input())
a = 0
while a <= x:
    print("*" * a, end = '\n')
    a = a + 1




'''new way to solve this'''
n = int(input())
stars = '*'
while len(stars) <= n:
    print(stars)
    stars += '*'
i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1
