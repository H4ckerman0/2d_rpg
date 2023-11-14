import pygame
from entity import Entity

class Enemy(Entity):
    def __init__(self, groups, name, pos):
        super().__init__(groups)