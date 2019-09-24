from tkinter import *
import random
import time

tk = Tk()

# Создание полотна по личным меркам
print("Input width your canvas: ")
w = int(input())
print("Input height your canvas: ")
h = int(input())
canvas = Canvas(tk, width=w, height=h)
canvas.pack()


def hello():
    print('Hello!')


def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)


def line_on_canvas():
    canvas.create_line(0, 0, 500, 500)
    canvas.create_arc(10, 160, 200, 240, extent=135, style=ARC)


def create_text():
    canvas.create_text(150, 100, text="Был один человек из Тулузы")
    canvas.create_text(130, 120, text='Что сидел на огромном арбузе.', fill='red')
    canvas.create_text(150, 150, text='Он сказал: "Это ужас,', font=('Times', 15))
    canvas.create_text(200, 200, text='Но бывает и хуже:', font=('Helvetica', 20))
    canvas.create_text(220, 250, text='Вон мой братец сидит', font=('Courier', 22))
    canvas.create_text(220, 300, text='На медузе".', font=('Courier', 30))


def rectangle_on_canvas():
    canvas.create_rectangle(10, 10, 50, 50)


def show_picture():
    way = 'pika\\giphy.gif'
    my_image = PhotoImage(file=way)  # не понимаю вообще почему это не работает(
    canvas.create_image(0, 0, anchor=NW, image=my_image)
    for x in range(0, 100):
        canvas.move(1, 5, 0)
        tk.update()
        time.sleep(0.05)
    for x in range(0, 100):
        canvas.move(1, 0, 5)
        tk.update()
        time.sleep(0.05)
    for x in range(0, 100):
        canvas.move(1, -5, 0)
        tk.update()
        time.sleep(0.05)
    for x in range(0, 100):
        canvas.move(1, 0, -5)
        tk.update()
        time.sleep(0.05)
    tk.mainloop()

def game_with_canvas():
    print("Input how much rectangle do you want: ")
    count = int(input())
    for x in range(0, count):
        random_rectangle(400, 400, 'red')
        random_rectangle(400, 400, 'green')
        random_rectangle(400, 400, 'yellow')


def animation():
    canvas.create_polygon(10, 10, 10, 60, 50, 35)
    for x in range(0, 100):
        canvas.move(1, 5, 0)
        tk.update()
        time.sleep(0.05)
    for x in range(0, 100):
        canvas.move(1, 0, 5)
        tk.update()
        time.sleep(0.05)
    for x in range(0, 100):
        canvas.move(1, -5, 0)
        tk.update()
        time.sleep(0.05)
    for x in range(0, 100):
        canvas.move(1, 0, -5)
        tk.update()
        time.sleep(0.05)


# Как вместо этого использовать словарь?
def use_some_function():
    state = input()
    if state == "game":
        game_with_canvas()
    elif state == "rectangle":
        rectangle_on_canvas()
    elif state == "line":
        line_on_canvas()
    elif state == "text":
        create_text()
    elif state == "image":
        show_picture()
    elif state == "animation":
        animation()


# def use_some_function(state):
#     {
#         "game": game_with_canvas(),
#         "rectangle": rectangle_on_canvas(),
#         "line": line_on_canvas()
#     }[state]

def triangle(wight, height, fill_color):
    x1 = random.randrange(wight)
    y1 = random.randrange(height)
    x2 = x1
    y2 = y1 + random.randrange(10, 100)
    x3 = x1 + random.randrange(10, 100)
    y3 = y2 - random.randrange(10, 50)
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=fill_color)


def random_triangle():
    print("Input count of triangle: ")
    count = int(input())
    for x in range(0, count):
        triangle(500, 500, "green")
        triangle(500, 500, "red")
        triangle(500, 500, "blue")


def main():
    # Создание кнопки
    btn = Button(tk, text="Push me!", command=hello)
    btn.pack()
    # random_triangle()
    # animation()
    show_picture()
    # print("Input nessesary state:")
    #     # use_some_function()
    tk.mainloop()


if __name__ == '__main__':
    main()
