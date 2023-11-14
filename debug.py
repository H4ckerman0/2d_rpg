import pygame
import os

pygame.init()

def debug(info, y = 0, x = 0):

    display = pygame.display.get_surface()

    font = pygame.font.Font(None,50)

    debug_display = font.render(str(info),True,"white")
    debug_rect = debug_display.get_rect(topleft = (x,y))

    pygame.draw.rect(display,"black",debug_rect)
    display.blit(debug_display,debug_rect)

current_path = os.path.dirname(__file__)
print(current_path)
path = os.path.join(current_path,"test_2d_rpg")
print(type(path))