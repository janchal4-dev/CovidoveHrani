import pygame
import random
from classes import MainSettings
import sys
pygame.init()


main_settings = MainSettings(2560,1440)
SCREEN = pygame.display.set_mode((main_settings.width, main_settings.height))
DISPLAY = pygame.display
DISPLAY.set_caption("My game")

#barvy
# main_settings.colors()

#exit button
exit_button = pygame.Rect(main_settings.width-220,main_settings.height-100,200,80)

crosshair_img = pygame.image.load("img/crosshair.png")
crosshair_img_rect = crosshair_img.get_rect()

tru_fal = [True,False]
#terč
target_img = pygame.image.load("img/target0.png")
target_img_rect = target_img.get_rect()
#definice pozic
target_locations = [195,395,595,795]

text0 = main_settings.font_function("Tahoma","Shot the target",70,main_settings.colors("white"))
my_text0 = text0[0]
my_text_rect0 = text0[1]
my_text_rect0.center = (main_settings.width//2, 35)

#rychlost
fps = 144
clock = pygame.time.Clock()

#lines creator
lines_list = main_settings.line_creator(SCREEN,5,(main_settings.colors("white")),(-5,80),200,4,main_settings.width)


def rand_pos(wid,hei):
    wid = random.randint(0+20,wid-20)
    hei = random.randint(0+20,hei)
    return wid,hei

pygame.mouse.set_visible(False)
# gun_rect.center = (main_settings.width//2,main_settings.height//2)
lest_continue = True
gun_img_num = 0
wait = -1
last_gun_num = 0
target_shot = True
location_left = True
num_of_shot_targets = 0
while lest_continue == True:
    text1 = main_settings.font_function("Tahoma",f"Targets shot: {num_of_shot_targets}",45,main_settings.colors("white"))
    my_text1 = text1[0]
    my_text_rect1 = text1[1]
    my_text_rect1.center = (200, 35)
    gun = pygame.image.load(f"img/gun_move/gun-{22}.png")
    gun = pygame.transform.scale(gun,(600,600))
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        if event.type == pygame.QUIT:
            lest_continue = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                lest_continue = False
        if event.type == pygame.MOUSEMOTION:
            if mouse_y < 110:
                mouse_y = 110
            crosshair_img_rect.center = (mouse_x,mouse_y)
        if event.type == pygame.MOUSEBUTTONDOWN:
            targ_x = target_img_rect.x
            targ_y = target_img_rect.y

            # end of the line
            btn_exit_x = exit_button.x
            btn_exit_y = exit_button.y
            if (abs(mouse_x-btn_exit_x)<=200) and (abs(mouse_y-btn_exit_y)<=80):
                lest_continue = False

            if abs((mouse_x-targ_x)<90) and abs((mouse_y-targ_y)<90):
                main_settings.sound("sounds/shotgun.mp3")
                num_of_shot_targets+=1
                text1 = main_settings.font_function("Tahoma",f"Targets shot: {num_of_shot_targets}",45,main_settings.colors("white"))
                my_text1 = text1[0]
                my_text_rect1 = text1[1]
                my_text_rect1.center = (200, 35)
                while gun_img_num < 22:
                    if gun_img_num < 5:
                        crosshair_img = pygame.image.load(f'img/red_crosshair.png')
                    else:
                        crosshair_img = pygame.image.load("img/crosshair.png")
                    if gun_img_num > 9:
                        target_img_rect.x = 5000
                        target_img = pygame.image.load(f"img/target{random.randint(0,3)}.png")
                    wait+=1
                    if wait%10 == 0:
                        gun_img_num+=1

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEMOTION:
                            mouse_pos = pygame.mouse.get_pos()
                            mouse_x = mouse_pos[0]
                            mouse_y = mouse_pos[1]
                            if mouse_y < 110:
                                mouse_y = 110
                            crosshair_img_rect.center = (mouse_x,mouse_y)
                    gun = pygame.image.load(f"img/gun_move/gun-{gun_img_num}.png")
                    gun = pygame.transform.scale(gun,(600,600))
                    last_gun_num = gun_img_num
                    SCREEN.fill(main_settings.colors("black"))
                    SCREEN.blit(gun,gun_rect)
                    for x in range(0,5):
                        first_line = lines_list[x]
                        pygame.draw.line(first_line[0],first_line[1],first_line[2],first_line[3],first_line[4])
                    text2 = main_settings.font_function("Tahoma","Quit game",40,main_settings.colors("white"))
                    my_text2 = text2[0]
                    my_text_rect2 = text2[1]
                    # my_text_rect2.center = (main_settings.width//2, 35)
                    my_text_rect2.center = (main_settings.width-122, main_settings.height-65)
                    pygame.draw.rect(SCREEN, main_settings.colors("red"), exit_button)
                    SCREEN.blit(my_text0,my_text_rect0)
                    SCREEN.blit(my_text1,my_text_rect1)
                    SCREEN.blit(my_text2,my_text_rect2)
                    SCREEN.blit(target_img,target_img_rect)
                    SCREEN.blit(crosshair_img,crosshair_img_rect)
                    DISPLAY.flip()
                    clock.tick(fps)
                    target_shot = True
                gun_img_num = 0
                # print(mouse_y)
    crosshair_img = pygame.image.load("img/crosshair.png")
    gun = pygame.transform.scale(gun,(600,600))
    last_gun_num = gun_img_num
    gun_rect = gun.get_rect()
    gun_rect.center = (main_settings.width//2,main_settings.height//2+420)
    SCREEN.fill(main_settings.colors("black"))
    SCREEN.blit(gun,gun_rect)
    for x in range(0,5):
        first_line = lines_list[x]
        print(first_line)
        pygame.draw.line(first_line[0],first_line[1],first_line[2],first_line[3],first_line[4])
    pygame.draw.rect(SCREEN, main_settings.colors("red"), exit_button)
    if target_shot == True:
        target_shot = False
        target_img_rect.center = (random.randint(0,main_settings.width),target_locations[random.randint(0,3)])
        target_x_pos = target_img_rect.x
        location_left = tru_fal[random.randint(0,1)]
    if target_x_pos < -20:
        location_left = False

    elif target_x_pos > main_settings.width+20:
        location_left = True

    if location_left == True:
        target_x_pos-=5
    else:
        target_x_pos+=5

    text2 = main_settings.font_function("Tahoma","Quit game",40,main_settings.colors("white"))
    my_text2 = text2[0]
    my_text_rect2 = text2[1]
    # my_text_rect2.center = (main_settings.width//2, 35)
    my_text_rect2.center = (main_settings.width-122, main_settings.height-65)
    target_img_rect.x = target_x_pos
    my_text_rect2.center = (main_settings.width-122, main_settings.height-65)
    SCREEN.blit(my_text2,my_text_rect2)
    SCREEN.blit(my_text1,my_text_rect1)
    SCREEN.blit(my_text0,my_text_rect0)
    SCREEN.blit(target_img,target_img_rect)
    SCREEN.blit(crosshair_img,crosshair_img_rect)
    DISPLAY.flip()
    clock.tick(fps)
pygame.quit()