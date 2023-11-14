import pygame
from settings import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups):
        super().__init__(groups)
        
        direction = player.player_status.split("_")[0]
        full_path = GAME_PATH + f"\graphics\weapon\{player.weapon}\{direction}.png"

        self.image = pygame.image.load(full_path)

        if player.weapon == "spear":
            if direction == "right":
                self.rect = self.image.get_rect(midleft = player.rect.midright - pygame.math.Vector2(0,-15))
            elif direction == "left":
                self.rect = self.image.get_rect(midright = player.rect.midleft - pygame.math.Vector2(0,0))
            elif direction == "up":
                self.rect = self.image.get_rect(midbottom = player.rect.midtop - pygame.math.Vector2(-10,-10))
            else:
                self.rect = self.image.get_rect(midtop = player.rect.midbottom - pygame.math.Vector2(5,10))

        elif player.weapon == "axe":
            if direction == "right":
                self.rect = self.image.get_rect(midleft = player.rect.midright - pygame.math.Vector2(0,-7))
            elif direction == "left":
                self.rect = self.image.get_rect(midright = player.rect.midleft - pygame.math.Vector2(0,-7))
            elif direction == "up":
                self.rect = self.image.get_rect(midbottom = player.rect.midtop - pygame.math.Vector2(0,-10))
            else:
                self.rect = self.image.get_rect(midtop = player.rect.midbottom - pygame.math.Vector2(-2,10))
                
        else:
            if direction == "right":
                self.rect = self.image.get_rect(midleft = player.rect.midright - pygame.math.Vector2(0,-10))
            elif direction == "left":
                self.rect = self.image.get_rect(midright = player.rect.midleft - pygame.math.Vector2(0,-5))
            elif direction == "up":
                self.rect = self.image.get_rect(midbottom = player.rect.midtop - pygame.math.Vector2(-5,-10))
            else:
                self.rect = self.image.get_rect(midtop = player.rect.midbottom - pygame.math.Vector2(0,10))