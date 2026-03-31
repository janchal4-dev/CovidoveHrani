from turtle import Turtle, Screen
import random
import math
import time
import keyboard
import pygame

#popup okno
from tkinter import *
import tkinter as tk
from tkinter import messagebox


screen = Screen()
screen.tracer(False)
screen.bgcolor("grey")

# nastavování čáry
line = Turtle()
line.penup()
line.pensize(3)
line.goto(-5000,-21)
line.pendown()
line.goto(5000,-21)

#skóre
score_text = Turtle()
score_text.color("white")
score_text.penup()
score_text.hideturtle()


# # dinosaurus
# class Dinosaurus:
#     def __init__(self):
#         self.dinik = Turtle()
#         self.dinik.shape("square")
#         self.dinik.shapesize(2.9)
#         self.dinik.penup()

#     def dino_jump(self):
#         for y in range(0,200):
#             dinik.sety(y)
#             screen.update()
#             time.sleep(0.01)


#     def dino_move(self):
#         screen.listen()
#         self.dinik.setx(-int(math.floor(x_screen/2))+120)
#         # screen.onkeypress(self.dino_jump, "w")
#         # screen.onkeypress(self.dino_jump, "W")
#         # screen.onkeypress(self.dino_jump, "Up")
#         screen.onkeypress(self.dino_jump, "space")



# def dino_jump(tim, height): 
# # def dino_jump():
#     # height = 200
#     # tim = 0.01
#     dinik.sety(100)
#     screen.update()
#     time.sleep(2)
#     dinik.sety(0)
#     screen.update()
#     # for y in range(0,height):
#     #     dinik.sety(y)
#     #     screen.update()
#     #     time.sleep(tim)
#     # for y in range(height,-1,-1):
#     #     dinik.sety(y)
#     #     screen.update()
#     #     time.sleep(tim)
#     return True

# def dino_move(tim, height):
#     screen.listen()
#     dinik.setx(-int(math.floor(x_screen/2))+120)
#     # screen.onkeypress(self.dino_jump, "w")
#         # screen.onkeypress(self.dino_jump, "W") 
#     # screen.onkeypress(dino_jump, "Up")
#     screen.onkeypress(lambda: dino_jump(tim, height), "space")

def moving_cubes(x,barrier_height_change):
    # barrier.shapesize(random.randint(1,3))
    barrier.setx(x)
    # newbarier = Turtle()
    # newbarier.setx(x)
    # barrier_list = []
    # for z in range(0, random.randint(1,10)):
    #     barrier_list.append(new_body)
    #     barrier_list[z].setx(100*z)

    # barrier.shapesize(1.5)
    # barrier.setx(x)
    # for x in range (1000,-1000,-10):
    #     print(x)
    #     barrier.setx(x)
    #     screen.update()
    #     time.sleep(0.001)
    
    if barrier_height_change == True:
        barrier_width = random.randint(1,2)
        barrier.shapesize(barrier_width, random.randint(1,3), 0)
        if barrier_width == 1:
            barrier.sety(-barrier_width*20/2)
        elif barrier_width == 2:
            barrier.sety(0)
        # print(barrier.shapesize())


dinik = Turtle()
dinik.shape("turtle")
dinik.shapesize(1.9)
dinik.penup()

barrier = Turtle()
barrier.penup()
barrier.shape("square")
barrier.sety(-10)
barrier.setx(100)

# barrier_b = Turtle()
# barrier_b.penup()
# barrier_b.shape("square")
# barrier_b.sety(-9)
# barrier_b.setx(100)
# asdf = Dinosaurus() 
x = int(math.floor(screen.window_width())/2)
control = 0
downer = 0
above_waiter = 0.0
score_counter = 0

y = (random.randint(100,400))
barrier_height_change = False

#zvuk
pygame.init()
sound_file = "D:\DokumentyD\Referáty a prokekty\Python - pokročilý\google game in turtle/arcadesound.mp3"
pygame.mixer.music.load(sound_file)

def play_sound():
    pygame.mixer.music.play()

while True: 
    barrier_height_change = False
    score_counter+=1
    x_screen = int(math.floor(screen.window_width()))
    y_screen = int(math.floor(screen.window_height()))
    # print(f"x: {x}")
    # print(f"x_screen: {x_screen}")
    # print((x - x_screen/2))
    if (x - x_screen/2) == 0:
        # print("yeah")
        ground = []
        for a in range(0,100):
            ground.append(Turtle())
            ground[a].penup()
            ground[a].shape("square")
            ground[a].shapesize(0.1)
            ground[a].sety(-20-random.randint(2,5))
            # ground[a].hideturtle()
    for a in range(99,-1,-1):
        # if ground[a].xcor() - x_screen/2 < 5 and ground[a].xcor() < 0:
        #     print(a)
        # print(f"a: {a}")
        #     ground[a].setx(x_screen/2)
        # ground[99-a].color("white")
        
        if ground[a].xcor() + x_screen/2 <5:
            # print(f"a: {a}")
            # print(x)
            # ground[a].setx(x)
            if 99-a == 0:
                ground[a].setx(ground[0].xcor()+10)
            else:
                ground[a].setx(ground[a+1].xcor()+20)
            # print(f"ground pos {ground[99-a].xcor
        else:
            ground[a].setx(x-20*a)
    # print(ground[0].xcor())
    score_text.clear()
    score_text.setposition(-40,y_screen/2-50)
    score_text.write(f"Your score: {score_counter}", font=("Arial", 16, "bold"))

    dinik.setx(-int(math.floor(x_screen/2))+120)
    if x <= (-int(math.floor(x_screen/2))):
        x = int(math.floor(x_screen/2))
        barrier_height_change = True
    x-=10
    
    #zjištění zda se nedotkli čtverec s želvou
    if dinik.distance(barrier) < 35:
        screen.bgcolor("red")
        # time.sleep(3)
        # Create a tkinter window
        window = tk.Tk()

        # Hide the main window
        window.withdraw()

        # Show a popup window with a message
        messagebox.showinfo(f'Snake Game', f'{30*" "}You lost!{40*" "}')

        # Close the tkinter window
        window.destroy()   

        screen.bye()


    if control !=0:
        control+=20
    # print(control)
    # print(f"above waiter {above_waiter}")
    #control slouží k jumpu
    if control >= 80:
        above_waiter+=0.6 
        if above_waiter < 5:
            control = 80
            # print("yes")
        else:
            above_waiter = 0
            control = 0
            downer-=20
        # control = 0
        # downer-=20

    # print(f"first {downer}")

    if downer !=0 and downer!=-10:
        downer-=20

    # print(f"second {downer}")

    if downer <-80:
        downer = 0

    # print(f"third {downer}")
    # asdf.dino_move()
    
    if keyboard.is_pressed('space') or keyboard.is_pressed("Up") or keyboard.is_pressed("w"):
        # print("Space key is pressed")
        # dino_jump(0.01, 70)
        play_sound()
        control+=20
    # print(f"fourth {downer}")

    # print(control)
    if control !=0:
        dinik.sety(control)
    
    # print(f"fifth {downer}")

    if downer >= -80 and downer < 0:
        dinik.sety(80+downer)
        # print("a")
    
    # print(f"sixth {downer}")

    
    # dino_move(0.001, 80)-
    # moving_cubes(x)
    moving_cubes(x,barrier_height_change)
    screen.update()
    if score_counter < 250:
        time.sleep(0.035)
        # print("a")
    elif score_counter < 500:
        time.sleep(0.03)
        # print("b")
    elif score_counter < 750:
        time.sleep(0.025)
        # print("c")
    elif score_counter < 1000:
        time.sleep(0.015)
        # print("d")
    elif score_counter < 1250:
        time.sleep(0.01)
        # print("e")
    elif score_counter < 1500:
        time.sleep(0.005)
        # print("f")
    elif score_counter < 1750:
        time.sleep(0.0025)
        # print("g")
    else:
        time.sleep(0.00015)
        # print("h")
    # time.sleep(0.001)

# screen.exitonclick()
