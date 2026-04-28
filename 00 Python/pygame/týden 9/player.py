import pygame
from utility import image_cutter
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

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
        self.elapsed_time = 0

    
    def animation(self, direction):
        frame_count = 3

        self.index += 0.1


        if self.index >= frame_count:
            self.index = 0
        
        self.image = image_cutter(self.spritesheet, int(self.index), direction, 15, 16, 3) 

    def update(self, monsters, clock):
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
        
        if self.rect.left > SCREEN_WIDTH:
            self.rect.left = 0
        elif self.rect.right < 0:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
        elif self.rect.bottom < 0:
            self.rect.bottom = SCREEN_HEIGHT

        # zapni časomíru - pod proměnnou elapsed_time přidávej čas
        self.elapsed_time += clock.get_time()
        
        if self.elapsed_time > 2000:
            self.invulnerability = False
        
        if pygame.sprite.spritecollide(self, monsters, False):
            # if invulerability == False:
            # alternativní, používaný zápis
            if not self.invulnerability: 
                print("Auuu!")
                self.lives -= 1 # odeberat život
                self.invulnerability = True # zapni nesmrtelnost
                self.elapsed_time = 0 # vynuluj časomíru
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)