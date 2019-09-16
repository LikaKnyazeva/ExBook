import turtle
import time

t = turtle.Pen()


def my_circle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()


def my_star(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 19):
        if x % 2 == 0:
            t.forward(size)
            t.left(175)
        else:
            t.forward(size)
            t.left(225)
    if filled == True:
        t.end_fill()


# Задание из учебника №1

def octagon(size):
    for x in range(1, 9):
        t.forward(size)
        t.left(45)


# Задание из учебника №2

def special_octagon(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 9):
        t.forward(size)
        t.left(45)
    if filled == True:
        t.end_fill()


# Задание из учебника №3

def draw_star(size, points):
    for x in range(1, points):
        if x % 2 == 0:
            t.forward(size)
            t.left(72)
        else:
            t.forward(size)
            t.left(215)


def main():
    # Выполняем задание 3 из учебника
    draw_star(50, 11)
    time.sleep(3)
    t.reset()

    # Рисуем круг задавая цвет заполнения (функция работает для выбора цвета заполнения)
    my_circle(0.9, 0.4, 0)
    time.sleep(3)
    t.reset()

    # Сложная заполненная цветом и обведенная звезда
    t.color(0.9, 0.75, 0)
    my_star(100, 1)
    t.color(0, 0, 0)
    my_star(100, 0)
    time.sleep(3)
    t.reset()

    # Выполняем задание 1 из учебника
    octagon(50)
    time.sleep(3)
    t.reset()

    # Выполняем задание 2 из учебника
    t.color(1, 0.4, 0.8)
    special_octagon(50, 1)
    t.color(0, 0, 0)
    special_octagon(50, 0)
    turtle.done()


if __name__ == '__main__':
    main()
