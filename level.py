import pygame
from settings import *
from Tile import Tile
from Player import Player
from Weapon import Weapon
from support import *
from UI import UI

pygame.init()

class Level:
    def __init__(self):
        
        #self.display_surf = pygame.display.get_surface()
        self.visible_group = YSortCameraGroup()
        self.obstacle_group = pygame.sprite.Group()
        self.create_map()
        self.current_attack = None

        self.ui = UI()

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_group])

    def create_magic(self,style,impact,cost):
        print(style)
        print(impact)
        print(cost)

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def create_map(self):

        layouts = {

            "border": import_csv_layout(GAME_PATH + r"\map\map0\map_0_kumoland_border.csv")

        }

        for type,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index,col in enumerate(row):
                    y = row_index * 64
                    x = col_index * 64
                    if col != "-1":
                        if type == "border":
                            Tile((x,y),[self.obstacle_group],"invisible")

        self.player = Player(
            (1300,1280),
            [self.visible_group],
            self.obstacle_group,
            self.create_attack,
            self.destroy_attack,
            self.create_magic)

    def run(self):
        self.visible_group.custom_draw(self.player)
        self.visible_group.update()
        self.ui.display(self.player)

class YSortCameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_display_width = self.display_surface.get_size()[0] // 2
        self.half_display_height = self.display_surface.get_size()[1] // 2

        self.floor_surf = pygame.image.load(GAME_PATH + r"\graphics\kumo_map.png").convert()
        self.floor_rect = self.floor_surf.get_rect(topleft =  (0,0))

    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - self.half_display_width
        self.offset.y = player.rect.centery - self.half_display_height

        offset_rect = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,offset_rect)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_rect = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_rect)