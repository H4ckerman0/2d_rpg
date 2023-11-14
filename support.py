from csv import reader
import os
import pygame

pygame.init()

def import_csv_layout(path):
    csv_layout = []

    with open(path) as map:

        layout = reader(map, delimiter= ",")

        for row in layout:
            csv_layout.append(list(row))

    return csv_layout

def import_folder_sprites(path):
    sprite_list = []
    for _,__,files in os.walk(path):
        for file in files:
            full_path = path + "\\" + file
            sprite = pygame.image.load(full_path).convert_alpha()
            sprite_list.append(sprite)
    return sprite_list
