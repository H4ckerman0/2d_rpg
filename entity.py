import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.direction = pygame.math.Vector2()
        self.frame_index = 0
        self.animation_speed = 0.08
        
    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.centerx += self.direction.x * speed
        self.collisions("horizontal")

        self.hitbox.centery += self.direction.y * speed
        self.collisions("vertical")
        self.rect = self.hitbox

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