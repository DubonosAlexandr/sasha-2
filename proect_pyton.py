from tkinter import *
import time
import random
from math import *

tk = Tk()
tk.title('SHARIK')
# tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=1980, height=1080, highlightthickness=0)
canvas.pack()
tk.update()


class Ball_0:

    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(20, 20, 40, 40, fill=color)
        self.canvas.move(self.id, 200, 100)
        starts = [-3, -5, 5, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(750, 400, text='Вы проиграли', font=('Courier', 100), fill='red')
        if self.hit_paddle(pos) == True:
            self.y = -2
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2


class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(20, 20, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-2, -1, 1, 2]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -4
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = (random.randint(5, 13))
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(750, 400, text='Вы проиграли', font=('Courier', 100), fill='red')
        if self.hit_paddle(pos) == True:
            self.y = -(random.randint(5, 13))
            self.x = ((-1) ** (random.randint(0, 10))) * (random.randint(5, 13))
        if pos[0] <= 0:
            self.x = (random.randint(5, 13))
            self.y *= (random.randint(1, 2))
        if pos[2] >= self.canvas_width:
            self.x = -(random.randint(5, 13))
            self.y *= (random.randint(1, 2))


class Ball_1:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(40, 40, 25, 25, fill=color)
        self.canvas.move(self.id, 100, 100)
        starts = [-3, -4, 4, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -4
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(750, 400, text='Вы проиграли', font=('Courier', 100), fill='red')
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(110, 10, 310, 35, fill="#1f1", width=2)
        start_1 = [40, 60, 90, 120, 150, 180, 200]
        random.shuffle(start_1)
        self.starting_point_x = start_1[0]
        self.canvas.move(self.id, self.starting_point_x, 700)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.started = False
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    def turn_right(self, event):
        self.x = 15

    def turn_left(self, event):
        self.x = -15

    def start_game(self, event):
        self.started = True

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0


class Score:

    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(1500, 10, text=self.score, font=('Courier', 15), fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)


score = Score(canvas, 'green')
paddle = Paddle(canvas, 'Blue')
# ball3 = Ball_1(canvas, paddle, score, 'red')
# ball1 = Ball_0(canvas, paddle, score, 'black')
ball2 = Ball(canvas, paddle, score, 'yellow')
while not ball2.hit_bottom:  # чтобы добавить мячиков и если однин из них падал игра бы тоже заканчивалась нужно через ор добовлять их сюда
    if paddle.started == True:
        # ball1.draw()
        ball2.draw()
        # ball3.draw()
        # paddle.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.001)

time.sleep(3)
