x = int(input())
if x % 10 == 0 or x % 10 == 5 or x % 10 == 6 or x % 10 == 7 or x % 10 == 8 or x % 10  == 9 or x % 100 == 11 or x % 100 == 12 or x % 100 ==13 or x%100 == 14:
    print(x, "программистов")
elif x % 10 == 2 or x % 10 == 3 or x % 10 == 4:
    print(x, "программиста")
elif x % 10 == 1 or x % 100 != 11:
    print(x, "программист" )
