from turtle import Turtle, Screen
from threading import Timer
import keyboard  # using module keyboard
import threading
import time
# from pynput.keyboard import Key, Controller
# artificial_keyboard = Controller()

# def keyboard_function(key):
#     d = False
#     while True:  # making a loop
#         try:  # used try so that if user pressed other than the given key error will not be shown
#             if keyboard.is_pressed(f"{key}"):  # if key 'q' is pressed 
#                 print(f'You Pressed {key} Key!')
#                 d = True
#                 # return d
#                 break  # finishing the loop
                
#         except:
#             break  # if user pressed a key other than the given key the loop will break


# keyboard_function("a")

# keyboard_function("w")

# keyboard_function("w")

screen = Screen()
screen.bgcolor("green")
screen.title("Snake game")
screen.setup(800,800)
screen.tracer(False)

square = Turtle()
square.shape("square")
# square.penup()
square.pensize(10)
square.pencolor("blue")


square0 = Turtle()
square0.shape("square")
square0.color("white")
square0.pensize(10)
square0.pencolor("green")
square0.penup()
square0.goto(-20,0)
square0.pendown()


def key_function():
    return(keyboard.read_key())

# def forward():
#     print("w")
#     square.forward(10)
#     screen.update()

# artificial_keyboard.press("a")
# artificial_keyboard.release("a")

counter = 0
body_list = []
catch_upper = [(0,0), (0,0), (0,0)]
right_side = bool
second_counter = 0

while True:
    second_counter += 1
    print(second_counter)
    if counter > 2:
        counter = 0
    # t = threading.Timer(2.0, forward)
    # t.start()
    #      
    pressed_a = keyboard.is_pressed("a") 
    pressed_d = keyboard.is_pressed("d")
    pressed_esc = keyboard.is_pressed("esc")
    # print(pressed)
        # print(pressed)
    # print(key_function())

    supervisor = pressed_a or pressed_d or pressed_esc 

    # if supervisor != False and (square.pos()>=(50.00,0.00) or second_counter != 1) !=False:
    if supervisor != False:
        if keyboard.read_key() == "a":
        # if pressed_a:
            print("a")
            catch_upper[counter] = square.pos()
            right_side = False
            print(f"čtverec:{catch_upper}")
            counter+=1
            square.left(90)
            square.forward(5)
            # square0.forward(20)
            # square0.left(90)
            screen.update()
            # supervisor = False
            


        # elif keyboard.read_key() == "d":
        elif pressed_d:
            print("d")
            catch_upper[counter] = square.pos()
            right_side = True
            print(f"čtverec:{catch_upper}")
            counter+=1
            square.left(270)
            square.forward(5)
            # square0.forward(20)
            # square0.left(270)
            screen.update()
            

        # elif keyboard.read_key() == "esc":
        elif pressed_esc:
            print("Goodbye")
            screen.bye()
                    
        else:
            print("sleep")
            square.forward(5)
            screen.update()




    else:
        time.sleep(0.2)
        # print(catch_upper)
        print(f"čtverec0: {square0.pos()}")
        square.forward(5)

        if square0.pos() == catch_upper[0] or square0.pos() == catch_upper[1] or square0.pos() == catch_upper[2]:
            if right_side == False:
                square0.left(90)
                square0.forward(5)
            elif right_side == True:
                square0.left(270)
                square.forward(5)
        
        square0.forward(5)
        screen.update()
