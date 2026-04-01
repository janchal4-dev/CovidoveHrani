import pygame
class MainSettings:
    def __init__(self,width,height):
        self.width = width
        self.height = height 
    def colors(self,color="black,white,red,blue,green"):
        color_dict = {
        "black": (5,5,3),
        "white": (255,255,255),
        "red": (255,0,0),
        "blue": (0,0,255),
        "green": (0,80,0)}
        return color_dict[color]
    def font_function(self,font, text, size, color1,color2=None):
        my_font = pygame.font.SysFont(font,size)
        if color2 == None:
            my_text = my_font.render(text,True, color1)
        else:
            my_text = my_font.render(text,True, color1, color2)
        my_text_rect = my_text.get_rect()
        return my_text,my_text_rect
    def sound(self,track):
        sound_jump = pygame.mixer.Sound(track)
        sound_jump.play()
    def line_creator(self,screen, count,color,first_pos,jump,width,screen_width):
        line_list = []
        tuple_to_list = list(first_pos)
        y = 80
        for one_line in range(0,count):
            if one_line == 0:
                y = 80
            elif one_line == 1:
                y+=180
            else:
                y+=jump
            line_list.append((screen,color,(-5,y),(screen_width+5,y),width))
        return line_list
