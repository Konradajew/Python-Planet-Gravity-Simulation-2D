from tkinter import *
from things import SuperButton, SimScreen, BasicButton
from tkinter import messagebox
import time
from random import randint

DARK_BLUE = "#041562"
LIGHT_BLUE = "#11468F"
WHITE = "#EEEEEE"
RED = "#DA1212"
FONT = ("Impact", 20, "bold")


def simulation(window, number):
    window.destroy()
    simulation_window = SimScreen(Tk())

    def check_data(arg_list, screen):
        try:
            for _ in arg_list:
                float(_.get())
        except:
            messagebox.showinfo(title="Oops", message="Write numbers everywhere!")
            return None
        message = ""
        if float(arg_list[0].get()) <= 0:
            message += "Enter a positive mass!\n"
        if float(arg_list[5].get()) <= 0:
            message += "Enter a positive diameter!\n"
        if float(arg_list[5].get()) > 0 and float(arg_list[0].get()) > 0:
            color = (randint(1, 255), randint(1, 255), randint(1, 255))
            messagebox.showinfo(title="OK", message="Addition was successful!")
            planets.append(SimScreen.Planet(xcor=float(arg_list[1].get()), ycor=float(arg_list[2].get()),
                                            m=float(arg_list[0].get()), color=color, size=float(arg_list[5].get()),
                                            y_speed=float(arg_list[4].get()), x_speed=float(arg_list[3].get()),
                                            canvas=simulation_window.screen))
            screen.destroy()
            for planet in planets:
                planet.planet.showturtle()
                simulation_window.screen.update()
            return None
        messagebox.showinfo(title="Oops", message=message)

    def add_planet():
        add_planet_screen = Tk()
        add_planet_screen.title("Enter the parameters of the new body")
        Label(add_planet_screen, text="Mass:").grid(column=0, row=0)
        Label(add_planet_screen, text="Coordinate x:").grid(column=0, row=1)
        Label(add_planet_screen, text="Coordinate y:").grid(column=0, row=2)
        Label(add_planet_screen, text="x axis speed:").grid(column=0, row=3)
        Label(add_planet_screen, text="y axis speed:").grid(column=0, row=4)
        Label(add_planet_screen, text="Diameter:").grid(column=0, row=5)
        masa = Entry(add_planet_screen)
        x = Entry(add_planet_screen)
        y = Entry(add_planet_screen)
        x_vel = Entry(add_planet_screen)
        y_vel = Entry(add_planet_screen)
        size = Entry(add_planet_screen)
        masa.grid(column=1, row=0)
        x.grid(column=1, row=1)
        y.grid(column=1, row=2)
        x_vel.grid(column=1, row=3)
        y_vel.grid(column=1, row=4)
        size.grid(column=1, row=5)
        Label(add_planet_screen, text="*Sun mass").grid(column=2, row=0)
        Label(add_planet_screen, text="*AU").grid(column=2, row=1)
        Label(add_planet_screen, text="*AU").grid(column=2, row=2)
        Label(add_planet_screen, text="*1000").grid(column=2, row=3)
        Label(add_planet_screen, text="*1000").grid(column=2, row=4)
        Label(add_planet_screen, text="1 = 20pix").grid(column=2, row=5)
        ok_button = Button(add_planet_screen, text="OK")
        ok_button.config(width=40, command=lambda: check_data([masa, x, y, x_vel, y_vel, size], add_planet_screen))
        add_planet_screen.attributes("-topmost", True)
        ok_button.grid(column=0, row=6, columnspan=3)

        add_planet_screen.mainloop()

    def end_simulation(sim_win):
        global should_simulate
        should_simulate = False
        sim_win.screen = 0
        sim_win.master.destroy()

    def kill_window(sim_win):
        end_simulation(sim_win)
        menu()

    def draw_track():
        clear_track(planets)
        planet1.draw_track(planets)

    def clear_track(objects):
        for _ in objects:
            _.planet.clear()

    def start_sim():
        global should_simulate
        should_simulate = True
        while should_simulate:
            for planet in planets:
                planet.update_position(planets)
                planet.new_position()
            if planet1.draw_vec:
                for vector in planets:
                    vector.update_vector_position(planets)
            window.after(1, simulation_window.screen.update())

    simulation_window.screen.tracer(0)
    planet1 = SimScreen.Planet(xcor=0, ycor=0, m=1, color='yellow', size=1, y_speed=0, x_speed=0, canvas=simulation_window.screen)
    planet2 = SimScreen.Planet(xcor=-2, ycor=0, m=0.002, color='blue', size=0.5, y_speed=21, x_speed=0, canvas=simulation_window.screen)
    planet3 = SimScreen.Planet(xcor=-2.1, ycor=0, m=0.0000002, color='red', size=0.2, y_speed=23, x_speed=0, canvas=simulation_window.screen)
    planet4 = SimScreen.Planet(xcor=2.1, ycor=0, m=0.0000002, color='Purple', size=0.2, y_speed=-23, x_speed=0, canvas=simulation_window.screen)
    planet5 = SimScreen.Planet(xcor=2, ycor=0, m=0.002, color='DeepPink', size=0.5, y_speed=-21, x_speed=0, canvas=simulation_window.screen)
    planet6 = SimScreen.Planet(xcor=-2.05, ycor=0, m=0.00000001, color='green', size=0.1, y_speed=25, x_speed=0, canvas=simulation_window.screen)
    planet7 = SimScreen.Planet(xcor=2.05, ycor=0, m=0.00000001, color='LightYellow', size=0.1, y_speed=-25, x_speed=0, canvas=simulation_window.screen)
    planet8 = SimScreen.Planet(xcor=0, ycor=3, m=0.0001, color='Black', size=0.4, y_speed=0, x_speed=17, canvas=simulation_window.screen)
    planet9 = SimScreen.Planet(xcor=0, ycor=3.05, m=0.000000001, color='Gray', size=0.1, y_speed=0, x_speed=18, canvas=simulation_window.screen)
    planet10 = SimScreen.Planet(xcor=-0.5, ycor=0, m=0.00001, color='white', size=0.2, y_speed=23, x_speed=0, canvas=simulation_window.screen)
    planets = [planet1, planet2, planet3, planet4, planet5, planet6, planet7, planet8, planet9, planet10]
    planets = planets[0:number]

    if number == 2:
        planets = []
        simulation_window.screen.onkey(key='a', fun=add_planet)
        dodaj_planet = BasicButton(window=simulation_window.master, text="A-ADD PLANET", font=("Impact", 20, "bold"))
        dodaj_planet.create.config(width=12, command=add_planet)

    simulation_window.screen.listen()
    simulation_window.screen.onkey(key='Escape', fun=lambda: end_simulation(simulation_window))
    simulation_window.screen.onkey(key='m', fun=lambda: kill_window(simulation_window))
    simulation_window.screen.onkey(key='s', fun=start_sim)
    simulation_window.screen.onkey(key='t', fun=draw_track)
    simulation_window.screen.onkey(key='c', fun=lambda: clear_track(planets))
    simulation_window.screen.onkey(key='v', fun=lambda: planet1.draw_vector(planets))

    start = BasicButton(window=simulation_window.master, text="S-START", font=("Impact", 24, "bold"))
    start.create.config(command=start_sim)
    tor = BasicButton(window=simulation_window.master, text="T-Track Draw", font=("Impact", 24, "bold"))
    tor.create.config(command=draw_track)
    czysctor = BasicButton(window=simulation_window.master, text="C-Clear Track", font=("Impact", 24, "bold"))
    czysctor.create.config(command=lambda: clear_track(planets))
    wektor = BasicButton(window=simulation_window.master, text="V-VECTOR", font=("Impact", 24, "bold"))
    wektor.create.config(command=lambda: planet1.draw_vector(planets))
    main = BasicButton(window=simulation_window.master, text="M-MENU", font=("Impact", 24, "bold"))
    main.create.config(command=lambda: kill_window(simulation_window))
    esc = BasicButton(window=simulation_window.master, text="ESC - Leave", font=("Impact", 24, "bold"))
    esc.create.config(command=lambda: end_simulation(simulation_window))

    author = Label(text="Konradajew\nBig boy", bg=LIGHT_BLUE, fg=RED, pady=50, font=FONT)
    author.pack()
    for planet in planets:
        planet.planet.showturtle()
        simulation_window.screen.update()


def execute_option1(window):
    simulation(window, 3)


def execute_option2(window):
    simulation(window, 5)


def execute_option3(window):
    simulation(window, 8)


def execute_option4(window):
    simulation(window, 10)


def execute_option5(window):
    simulation(window, 2)


def menu():
    window = Tk()
    window.config(padx=500, pady=300, background=LIGHT_BLUE)
    window.title("Planet Simulation Python")

    option1 = SuperButton("3 PLANETS", window, 0, 0)
    option1.create.config(command=lambda: execute_option1(window))
    option2 = SuperButton("5 PLANETS", window, 1, 0)
    option2.create.config(command=lambda: execute_option2(window))
    option3 = SuperButton("8 PLANETS", window, 0, 1)
    option3.create.config(command=lambda: execute_option3(window))
    option4 = SuperButton("10 PLANETS", window, 1, 1)
    option4.create.config(command=lambda: execute_option4(window))
    option5 = SuperButton("N PLANETS", window, 2, 0)
    option5.create.config(command=lambda: execute_option5(window))
    option6 = SuperButton("LEAVE", window, 2, 1)
    option6.create.config(command=lambda: window.destroy())

    window.mainloop()


should_simulate = True
menu()
