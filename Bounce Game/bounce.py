import random
import time
import tkinter
from tkinter import *

root_window = tkinter.Tk()
root_window.title("Bounce Game © Sawrav Chowdhury")
root_window.iconbitmap("bouncing.ico")
root_window.wm_attributes(
    "-topmost",
    1)  # This means that our game window is in front of all window forcely
root_window.resizable(0, 0)
n = -285

canvas = Canvas(
    root_window,
    height=600,
    width=600,
    bd=0,
    highlightthickness=0,
    bg="#1E1E1E",
)
canvas.pack()
canvas.update()


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(5, 5, 55, 55, fill=color)
        self.canvas.move(self.id, 300, 300)
        startpoint = [-3, -2, -1, 1, 2, 3]
        random.shuffle(startpoint)
        self.x = startpoint[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, position):
        paddle_position = self.canvas.coords(self.paddle.id)
        if position[2] >= paddle_position[0] and position[
                0] <= paddle_position[2]:
            if position[3] >= paddle_position[1] and position[
                    3] <= paddle_position[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        position = self.canvas.coords(self.id)  #[x1,y1.x2,y2]
        print(position)
        if position[1] <= 0:
            self.y = 3
        if position[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(300,
                               100,
                               text="Game Over",
                               font=("Paytone One", 20),
                               fill='#fff')
            canvas.create_text(300,
                               150,
                               text="Your Score is:",
                               font=("Paytone One", 20),
                               fill='#fff')
            canvas.create_text(300,
                               190,
                               text=n,
                               font=("Verdana", 20),
                               fill='#fff')

        if position[0] <= 0:
            self.x = 3
        if position[2] >= self.canvas_width:
            self.x = -3
        if self.hit_paddle(position) == True:
            self.y = -3


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 30, fill=color)
        self.canvas.move(self.id, 300, 450)
        self.x = 0
        self.canvcanas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        position = self.canvas.coords(self.id)
        print(position)
        if position[0] <= 0:
            self.x = 0
        if position[2] >= self.canvcanas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3


paddle = Paddle(canvas, '#F7D420')
ball = Ball(canvas, paddle, '#EA4E5B')

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        n = n + 1
    root_window.update_idletasks()
    root_window.update()
    time.sleep(0.01)

root_window.resizable(0, 0)
root_window.mainloop()
