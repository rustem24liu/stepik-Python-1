import turtle
import random

# Задаем массив формы снежинки
flake = ["red", "orange", "yellow", "green", "blue", "purple", "white", "gray"]
branches = 5
branch_len = 10

# Создаем экран и черепашку
wn = turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.speed(0)

# Функция для рисования одной ветви снежинки
def branch():
    for i in range(10):
        t.color(random.choice(flake))
        for j in range(3):
            t.forward(branch_len)
            t.backward(branch_len)
            t.right(45)
        t.left(90)
        t.backward(branch_len)
        t.left(45)
    t.right(90)
    t.forward(branch_len)

# Рисуем все ветви снежинки
for i in range(branches):
    branch()
    t.right(360 / branches)

# Заканчиваем рисование
t.hideturtle()
wn.exitonclick()

