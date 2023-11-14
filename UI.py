import pygame
from settings import *

class UI():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

        self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
        self.stamina_bar_rect = pygame.Rect(10,35,STAMINA_BAR_WIDTH,BAR_HEIGHT)

        self.weapon_graphics = []
        for val in weapon_data.values():
            full_path = val["graphic"]
            image = pygame.image.load(full_path)
            self.weapon_graphics.append(image)

        self.magic_graphics = []
        for val in magic_data.values():
            full_path = val["graphic"]
            image = pygame.image.load(full_path)
            self.magic_graphics.append(image)

    def show_bar_stats(self,current_stat,max_stat,bar_rect,color):
        bg_rect = bar_rect

        current_stat_ratio = current_stat / max_stat
        current_width = bar_rect.width * current_stat_ratio
        current_rect = bar_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface,BG_BAR_COLOR,bg_rect)
        pygame.draw.rect(self.display_surface,color,current_rect)
        pygame.draw.rect(self.display_surface,BORDER_COLOR,bar_rect,3)

    def show_selection_box(self,top,left,is_switching):
        box_rect = pygame.Rect(top,left,WEAPON_BOX_SIZE,WEAPON_BOX_SIZE)
        pygame.draw.rect(self.display_surface,BG_BAR_COLOR,box_rect)
        if is_switching:
            pygame.draw.rect(self.display_surface,BORDER_COLOR_ACTIVE,box_rect,3)
        else:
            pygame.draw.rect(self.display_surface,BORDER_COLOR,box_rect,3)
        return box_rect

    def weapon_display(self,weapon_index,is_switching):
        box_rect = self.show_selection_box(10,640,is_switching)
        weapon_image = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_image.get_rect(center = box_rect.center)
        self.display_surface.blit(weapon_image,weapon_rect)

    def magic_display(self,magic_index,is_switching):
        box_rect = self.show_selection_box(70,650,is_switching)
        magic_image = self.magic_graphics[magic_index]
        magic_rect = magic_image.get_rect(center = box_rect.center)
        self.display_surface.blit(magic_image,magic_rect)

    def show_exp_stat(self,exp):
        x = self.display_surface.get_size()[0] - 20

        text_surf = self.font.render(str(int(exp)),False,EXP_TEXT_COLOR)
        text_rect = text_surf.get_rect(topright = (x,10))

        pygame.draw.rect(self.display_surface,BG_BAR_COLOR,text_rect)
        pygame.draw.rect(self.display_surface,BORDER_COLOR,text_rect,3)
        self.display_surface.blit(text_surf,text_rect)

    def display(self,player):
        self.show_bar_stats(player.health,player.stats["health"],self.health_bar_rect,HEALTH_BAR_COLOR)
        self.show_bar_stats(player.stamina,player.stats["stamina"],self.stamina_bar_rect,STAMINA_BAR_COLOR)

        self.weapon_display(player.weapon_index,player.weapon_switching)
        self.magic_display(player.magic_index,player.magic_switching)

        self.show_exp_stat(player.exp)