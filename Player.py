import pygame
from debug import debug
from support import *
from settings import *
from entity import Entity

pygame.init()

class Player(Entity):
    def __init__(self,pos,groups,obstacle_group,create_attack,destroy_attack,create_magic):
        super().__init__(groups)
        self.image = pygame.image.load(GAME_PATH + r"\graphics\player\down_idle\down_idle0.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,0)


        self.display = pygame.display.get_surface()

        self.import_player_assets()

        self.player_status = "down"

        self.obstacle_group = obstacle_group

        self.attacking = False
        self.attack_cooldown = 700
        self.attack_time = 0

        self.stats = {"health": 100, "stamina": 100, "exp": 0 ,"speed": 5}
        self.health = self.stats["health"]
        self.stamina = self.stats["stamina"]
        self.exp = self.stats["exp"]
        self.speed = self.stats["speed"]

        self.switch_duration = 200      

        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.weapon_switching = False
        self.weapon_switch_time = 0  

        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.magic_switching = False
        self.magic_switch_time = 0

    def import_player_assets(self):
        player_path = GAME_PATH + r"\graphics\player"

        self.animations = {
            "up": [], "down":[], "right": [], "left": [],
            "up_idle": [], "down_idle":[], "right_idle": [], "left_idle": [],
            "up_attack": [], "down_attack":[], "right_attack": [], "left_attack": []
        }

        for animation in self.animations.keys():
            full_path = player_path + "\\" + animation
            self.animations[animation] = import_folder_sprites(full_path)

    def animate(self):
        frames = self.animations[self.player_status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(frames):
            self.frame_index = 0

        self.image = frames[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def input(self):
        keys = pygame.key.get_pressed()
        mouse_keys = pygame.mouse.get_pressed()

        if not self.attacking:
            if keys[pygame.K_w]:
                self.direction.y = -1
                self.player_status = "up"
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.player_status = "down"
            else:
                self.direction.y = 0


            if keys[pygame.K_d]:
                self.direction.x = 1
                self.player_status = "right"

            elif keys[pygame.K_a]:
                self.direction.x = -1
                self.player_status = "left"

            else:
                self.direction.x = 0

            if mouse_keys[0]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()

            if mouse_keys[2]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()

                style = list(magic_data.keys())[self.magic_index]
                impact = magic_data[style]["impact"]
                cost = magic_data[style]["cost"]

                self.create_magic(style,impact,cost)

            if keys[pygame.K_q]:
                if not self.weapon_switching:
                    self.weapon_switch_time = pygame.time.get_ticks()
                    self.weapon_index += 1
                    if self.weapon_index > len(list(weapon_data.keys())) - 1:
                        self.weapon_index = 0
                    self.weapon_switching = True
                    self.weapon = list(weapon_data.keys())[self.weapon_index]

            if keys[pygame.K_r]:
                if not self.magic_switching:
                    self.magic_switch_time = pygame.time.get_ticks()
                    self.magic_index += 1
                    if self.magic_index > len(list(magic_data.keys())) - 1:
                        self.magic_index = 0
                    self.magic_switching = True
                    self.magic = list(magic_data.keys())[self.magic_index]

    def get_status(self):

        if self.direction.x == 0 and self.direction.y == 0:
            if not "_idle" in self.player_status and not "_attack" in self.player_status:
                self.player_status = self.player_status + "_idle"

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not "_attack" in self.player_status:
                if "_idle" in self.player_status:
                    self.player_status = self.player_status.replace("_idle","_attack")
                else:
                    self.player_status = self.player_status + "_attack"

        else:
            self.player_status = self.player_status.replace("_attack","")

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.centerx += self.direction.x * speed
        self.collisions("horizontal")

        self.hitbox.centery += self.direction.y * speed
        self.collisions("vertical")
        self.rect.center = self.hitbox.center

    def collisions(self,direction):
        for sprite in self.obstacle_group:
            if sprite.hitbox.colliderect(self.hitbox):
                if direction == "horizontal":

                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

                if direction == "vertical":

                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time > self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()

        if self.weapon_switching:
            if current_time - self.weapon_switch_time > self.switch_duration:
                self.weapon_switching = False      

        if self.magic_switching:
            if current_time - self.magic_switch_time > self.switch_duration:
                self.magic_switching = False      

    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.cooldowns()
        self.move(self.speed)
        #debug(self.direction)
