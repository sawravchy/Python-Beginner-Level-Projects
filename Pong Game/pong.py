import tkinter
import random
import time
from tkinter import *
counter = 0
counter1 = 0

root_window = tkinter.Tk()
root_window.title("Pong Game © Sawrav Chowdhury")
root_window.iconbitmap("pong.ico")
root_window.wm_attributes("-topmost",1)#This means that our game window is in front of all window forcely
root_window.resizable(0,0)
n = -285



canvas = Canvas(
root_window,
height = 500,
width = 500,
bd = 0,
highlightthickness = 0,
bg = "#1E1E1E",


)

canvas.pack()
canvas.update()


canvas.create_line(250,0,250,600, fill = "#F5F6F8" )
class Ball:
    def __init__(self,canvas,color,paddle,paddleone):
        self.canvas=canvas
        self.paddle = paddle
        self.paddleone = paddleone
        self.id = canvas.create_oval(5,5,55,55,fill = color)
        self.canvas.move(self.id,220,270)
        startposition = [-3,3]
        random.shuffle(startposition)
        self.x = startposition[0]
        self.y = -3
        self.canvas_height= self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        position = self.canvas.coords(self.id)
        if position[1]<=0:
            self.y = 3
        if position[3]>= self.canvas_height:
            self.y =-3
        if position[0]<=0:
            self.x = 3
            self.score(True)
        if position[2]>= self.canvas_width:
            self.x = -3
            self.score(False)
        if self.hit_paddle(position) == True:
            self.x = 3
        if self.hit_paddleone(position) == True:
            self.x = -3
    def hit_paddle(self,position):
        paddle_position =self.canvas.coords(self.paddle.id)
        if position[1]>= paddle_position[1] and position[1]<=paddle_position[3]:
            if position[0]>= paddle_position[0] and position[0]<=paddle_position[2]:
                return True
            return False
    def hit_paddleone(self,position):
        paddle_position=self.canvas.coords(self.paddleone.id)
        if position[1]>= paddle_position[1] and position[1]<=paddle_position[3]:
            if position[2]>= paddle_position[0] and position[2]<=paddle_position[2]:
                return True
            return False
    def score(self,val):
        global counter
        global counter1
        if val == False:
            a=self.canvas.create_text(125,40,text = counter,font = ("Paytone One",20),fill= "#F1F1F1")
            canvas.itemconfig(a,fill = "#1E1E1E")
            counter += 1
            a=self.canvas.create_text(125,40,text = counter,font = ("Paytone One",20),fill= "#F1F1F1")
        
        if val == True:
            a=self.canvas.create_text(375,40,text = counter1,font = ("Paytone One",20),fill = "#F1F1F1")
            canvas.itemconfig(a,fill = "#1E1E1E")
        
            counter1 += 1
            a=self.canvas.create_text(375,40,text = counter1,font = ("Paytone One",20),fill= "#F1F1F1")


class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,150,30,250,fill=color)
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('w',self.turn_left)
        self.canvas.bind_all('s',self.turn_right)


    def draw(self):
        self.canvas.move(self.id,0,self.y)
        position = self.canvas.coords(self.id)
        if position[1]<=0:
            self.y =0
        if position[3]>=500:
            self.y= 0
    def turn_left(self,event):
        self.y = -3
    def turn_right(self,event):
        self.y = 3


class Paddleone:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(470,150,500,250,fill=color)
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Down>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Up>',self.turn_right)
    
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        position = self.canvas.coords(self.id)
        if position[1]<=0:
            self.y =0
        if position[3]>=500:
            self.y= 0
    def turn_left(self,event):
        self.y = 3
    def turn_right(self,event):
        self.y = -3


    


paddle = Paddle(canvas,'#F2CE22')
paddleone = Paddleone(canvas,'#F18A35')
ball = Ball(canvas, '#E94D52',paddle,paddleone)
while 1:
    
    paddle.draw()
    paddleone.draw()
    ball.draw()
    root_window.update_idletasks()   
    time.sleep(0.01)
    root_window.update()
    for i in range(0,10):
        if counter == 10 or counter1 == 10:
            if counter <counter1:
                canvas.create_rectangle(0,0,500,500,fill="#1E1E1E")
                canvas.create_text(250,200,text="Orange Paddle Win" ,font =("Paytone One",20),fill = '#CBCDD3')
                canvas.create_text(250,240,text="Score Board: " ,font =("Paytone One",20),fill = '#FF2100')
                canvas.create_text(250,280,text="Orange Paddle : "+str(counter1) ,font =("Paytone One",20),fill = '#F18A35')
                canvas.create_text(250,320,text="Yellow Paddle : "+str(counter) ,font =("Paytone One",20),fill = '#F2CE22')
            elif counter == counter1:
                canvas.create_rectangle(0,0,500,500,fill="#1E1E1E")
                canvas.create_text(300,190,text="Draw" ,font =("Paytone One",20),fill = '#fff')
            elif counter>counter1:
                canvas.create_rectangle(0,0,500,500,fill="#1E1E1E")
                canvas.create_text(250,200,text="Yellow Paddle Win" ,font =("Paytone One",20),fill = '#CBCDD3')
                canvas.create_text(250,240,text="Score Board: " ,font =("Paytone One",20),fill = '#FF2100')
                canvas.create_text(250,320,text="Orange Paddle : "+str(counter1) ,font =("Paytone One",20),fill = '#F18A35')
                canvas.create_text(250,280,text="Yellow Paddle : "+str(counter) ,font =("Paytone One",20),fill = '#F2CE22')
            
                




root_window.mainloop()

