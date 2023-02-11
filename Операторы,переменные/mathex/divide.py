x = float(input())
y = float(input())
if y == 0:
    print("Invalid system")
    y = float(input("Введите не нулевое значение "))
    if y == 0:
        print("Пошол ты в жопу")
    else:
        print(x/y)
else:
    print(x/y)