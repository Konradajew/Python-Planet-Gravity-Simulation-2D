import tkinter as tk
import turtle
import math


DARK_BLUE = "#041562"
LIGHT_BLUE = "#11468F"
WHITE = "#EEEEEE"
RED = "#DA1212"
FONT = ("Impact", 36, "bold")

AU = 1.496e11
MS = 2e30
G = 6.6738e-11
TIME_STEP = 24*3600  # Simulation speed
SCALE = 125 / AU  # SCALE
PI = 3.141592


class SuperButton:
    def __init__(self, text, window, column=1, row=1):
        self.border = tk.LabelFrame(window, bd=6, bg=DARK_BLUE)
        self.border.grid(column=column, row=row, padx=50, pady=30)
        self.create = tk.Button(self.border, text=text, width=10, height=1,
                                bg=WHITE, fg=DARK_BLUE, font=FONT)
        self.create.grid(column=column, row=row)


class BasicButton:
    def __init__(self, text, window, font):
        self.border = tk.LabelFrame(window, bd=6, bg=DARK_BLUE)
        self.border.pack()
        self.create = tk.Button(self.border, text=text, width=10, height=1,
                                bg=WHITE, fg=DARK_BLUE, font=font, pady=20, padx=20)
        self.create.pack()


class SimScreen:
    def __init__(self, master):
        self.master = master
        self.master.config(bg=LIGHT_BLUE)
        self.master.title("Planet Simulation")
        self.canvas = tk.Canvas(master, highlightbackground=DARK_BLUE)
        self.canvas.config(width=1500, height=900)
        self.canvas.pack(side=tk.RIGHT)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.colormode(255)
        self.screen.bgcolor(LIGHT_BLUE)

    class Planet:
        def __init__(self, xcor, ycor, m, x_speed, y_speed, size, color, canvas):
            super().__init__()
            self.draw_vec = False
            self.vector = turtle.RawTurtle(canvas)
            self.vector.penup()
            self.vector.hideturtle()
            self.vector.color(color)
            self.vector.pensize(2)
            self.planet = turtle.RawTurtle(canvas, shape="circle")
            self.planet.color(color)
            self.planet.penup()
            self.planet.pensize(size * 20)
            self.xcor = xcor * AU
            self.ycor = ycor * AU
            self.m = m * MS
            self.x_speed = x_speed * 1000
            self.y_speed = y_speed * 1000
            self.planet.shapesize(size)
            self.planet.hideturtle()
            self.draw = True
            self.new_position()

        def new_position(self):
            x = self.xcor * SCALE
            y = self.ycor * SCALE
            self.planet.goto(x, y)

        def attraction_force(self, other):
            distance_x = other.xcor - self.xcor
            distance_y = other.ycor - self.ycor
            distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
            force = (G * self.m * other.m) / (distance ** 2)
            alpha = math.atan2(distance_y, distance_x)
            force_y = force * math.sin(alpha)
            force_x = force * math.cos(alpha)
            return force_x, force_y

        def update_position(self, planets):
            total_fx = 0
            total_fy = 0
            for planet in planets:
                if self == planet:
                    continue

                fx, fy = self.attraction_force(planet)
                total_fx += fx
                total_fy += fy

            self.x_speed += total_fx / self.m * TIME_STEP
            self.y_speed += total_fy / self.m * TIME_STEP

            self.xcor += self.x_speed * TIME_STEP
            self.ycor += self.y_speed * TIME_STEP

        def draw_track(self, planets):
            self.draw = not self.draw
            if self.draw:
                for planet in planets:
                    planet.planet.penup()
            else:
                for planet in planets:
                    planet.planet.pendown()

        def draw_vector(self, planets):
            self.draw_vec = not self.draw_vec
            if self.draw_vec:
                for planet in planets:
                    planet.vector.pendown()
                    planet.vector.goto(planet.xcor*SCALE+int(planet.x_speed/1000), planet.ycor*SCALE+int(planet.y_speed/1000))
            else:
                for planet in planets:
                    planet.vector.penup()
                    planet.vector.clear()

        def update_vector_position(self, planets):
            for vector in planets:
                vector.vector.clear()
                vector.vector.penup()
                sx = vector.xcor*SCALE
                sy = vector.ycor*SCALE
                kx = sx + int(vector.x_speed / 1000)
                ky = sy + int(vector.y_speed / 1000)
                xd = sx - kx
                yd = sy - ky
                r = math.atan2(xd, yd)
                dist = 7
                vector.vector.goto(sx, sy)
                vector.vector.pendown()
                vector.vector.goto(kx, ky)
                vector.vector.goto(kx + dist * math.sin(r - PI / 6), ky + dist * math.cos(r - PI / 6))
                vector.vector.goto(kx, ky)
                vector.vector.goto(kx + dist * math.sin(r + PI / 6), ky + dist * math.cos(r + PI / 6))
