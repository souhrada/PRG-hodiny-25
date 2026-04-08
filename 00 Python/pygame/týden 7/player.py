import pygame
from utility import image_cutter

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 150
        self.y = 150
        self.spritesheet = pygame.image.load("assets/sprites/player/man_brownhair_run.png").convert_alpha() 
        self.image = image_cutter(self.spritesheet, 0, 0, 15, 16, 3) 
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.index = 0
        self.speed = 5
        self.lives = 3
        self.invulnerability = False

    
    def animation(self, direction):
        frame_count = 3

        self.index += 0.1


        if self.index >= frame_count:
            self.index = 0
        
        self.image = image_cutter(self.spritesheet, int(self.index), direction, 15, 16, 3) 

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.animation(1)
            self.rect.y -= self.speed
        if key[pygame.K_s]:
            self.animation(0)
            self.rect.y += self.speed
        if key[pygame.K_a]:
            self.animation(2)
            self.rect.x -= self.speed
        if key[pygame.K_d]:
            self.animation(3)
            self.rect.x += self.speed
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)