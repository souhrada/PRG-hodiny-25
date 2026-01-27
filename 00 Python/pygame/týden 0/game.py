import pygame
from sys import exit

# inicializuje hru - spustíme pygame
pygame.init()

# caps lock označuje konstanty - proměnné, které by se neměly měnit
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


# vytvoření obrazu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# vytvoř hodiny
clock = pygame.time.Clock()


running = True

# herní smyčka
while running:

    # kontroluje události, které se dějí v naší hře
    for event in pygame.event.get():
        # pokud nastane událost vypnout, vypni hru
        if event.type == pygame.QUIT:
            running = False
            exit()


    # obarví obrazovku na fialovo
    screen.fill("purple")

    # vše updatuje
    pygame.display.update()

    # pygame.display.flip() - alternativa k .update


    # omezí tickrate (rychlost hry) na 60 fps - aby hra běžela konzistentně rychle na všech zařízení
    clock.tick(60) 

pygame.quit()