import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from utility import image_cutter

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.x = x
        self.y = y
        self.idle = pygame.image.load("assets/sprites/monsters/monster.png").convert_alpha()
        self.idle = pygame.transform.scale(self.idle, (self.idle.get_width()*6, self.idle.get_height()*6))
        self.run1 = pygame.image.load("assets/sprites/monsters/monster-run1.png").convert_alpha()
        self.run1 = pygame.transform.scale(self.run1, (self.run1.get_width()*6, self.run1.get_height()*6))
        self.run2 = pygame.image.load("assets/sprites/monsters/monster-run2.png").convert_alpha()
        self.run2 = pygame.transform.scale(self.run2, (self.run2.get_width()*6, self.run2.get_height()*6))
        self.images = [self.idle, self.run1, self.run2]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.speed = 5
        self.direction = direction

    def animation(self):
        # importujeme globální proměnné, které přepisujeme
        # animace zjednodušeně - loopujeme listem, ve kterém jsou obrázky v rúzné fázi pohybu
        # vykreslujeme vždy jeden obrázek
        # index zvolí, který obrázek vykreslujeme
        
        self.index += 0.1 # index měníme 0.1, aby byla animace pomalejší

        # pokud je index větší, než množství obrázků v listu (délka listu), vyresetujeme index
        if self.index > len(self.images):
            self.index = 0

        # jelikož používáme desetinná čísla v indexu, je potřeba jej zaokrouhlit pomocí funkce int() - ta zaokrouhluje vždy dolu
        self.image = self.images[int(self.index)]
    
    def update(self):
        if self.direction == "horizontal":
            self.rect.x += self.speed

            if self.rect.right >= SCREEN_WIDTH:
                self.speed *= -1
            if self.rect.left <= 0:
                self.speed *= -1
        
        elif self.direction == "vertical":
            self.rect.y += self.speed

            if self.rect.bottom >= SCREEN_HEIGHT:
                self.speed *= -1
            if self.rect.top <= 0:
                self.speed *= -1
        else:
            print("direction can only be horizontal or vertical")

        self.animation()


class Monster2(Monster):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.spritesheet = pygame.image.load("assets/sprites/monsters/monster_spritesheet.png").convert_alpha() 
        self.image = image_cutter(self.spritesheet, 0, 0, 15, 16, 3) 
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))


    def animation(self):
        frame_count = 2
        self.index += 0.1
        if self.index >= frame_count:
            self.index = 0
        self.image = image_cutter(self.spritesheet, int(self.index), 0, 15, 16, 4)

    def scream(self):
        print("AAAAAAAAAA")
    
    def update(self):
        super().update()
        self.scream()
