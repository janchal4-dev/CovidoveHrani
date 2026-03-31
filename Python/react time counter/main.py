import pygame
import random
pygame.init()

WIDTH = 1920
HEIGHT = 1080
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
DISPLAY = pygame.display
DISPLAY.set_caption("Catch the ball")

#barvy
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,80,0)

# random position
def rand_pos(wid,hei):
    object_wid = random.randint(40,wid-40)
    object_hei = random.randint(40,hei-40)
    if object_wid < 300 and object_hei <100:
        if object_wid < 300:
            object_wid = 300
        if object_hei < 100:
            object_hei = 100
    return(object_wid,object_hei)


#vložení obrázku
ball_img = pygame.image.load("img/ball.png")
ball_img_rect = ball_img.get_rect()
ball_img_rect.center = rand_pos(WIDTH,HEIGHT)

# print(rand_pos(WIDTH,HEIGHT)[1])

#rychlost
fps = 144
clock = pygame.time.Clock()

def font_function(font, text, size, color1,color2=None):
    my_font = pygame.font.SysFont(font,size)
    global my_text
    if color2 == None:
        my_text = my_font.render(text,True, color1)
    else:
        my_text = my_font.render(text,True, color1, color2)
    global my_text_rect
    my_text_rect = my_text.get_rect()

lest_continue = True
mouse_down = False

# counting
times_passed = 0
full_react_time = 0
avg_react_time = 0
first_tic = True
tic_count = 0
last_tic = 0
current_tic = 0
# print(pygame.time.get_ticks())
while lest_continue == True:

    font_function("TimesNewRoman",f"AVG react time: {round(avg_react_time/1000,3)} s",30,white)
    my_text_rect.bottomleft = (0, 50)
    SCREEN.blit(my_text,my_text_rect)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lest_continue = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False

        if mouse_down == True:  
            mouse_pos = pygame.mouse.get_pos()
            object_x = ball_img_rect.x
            object_y = ball_img_rect.y

            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            if abs(mouse_x-object_x) < 70 and abs(mouse_y-object_y) < 70:
                # print(clock.get_time())
                if first_tic:
                    tic_gotten = 0
                    last_tic = pygame.time.get_ticks()
                    first_tic = False
                else:
                    tic_gotten = pygame.time.get_ticks()
                    current_tic = tic_gotten - last_tic
                    last_tic = tic_gotten
                    full_react_time += current_tic
                    times_passed+=1 
                    avg_react_time = (full_react_time)/times_passed 
                    print(avg_react_time/1000)           
                ball_img_rect.center = rand_pos(WIDTH,HEIGHT)

    clock.tick(fps)
    SCREEN.blit(ball_img,ball_img_rect)
    DISPLAY.update()
    SCREEN.fill(black)
pygame.quit()