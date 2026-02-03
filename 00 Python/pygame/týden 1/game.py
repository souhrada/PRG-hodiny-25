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


player = pygame.Rect((50, 100, 50, 50))

player_speed = 5


monster_surf = pygame.image.load("monster.png").convert_alpha()
monster_surf = pygame.transform.scale(monster_surf, (monster_surf.get_width()*6, monster_surf.get_height()*6))
monster_x = 50
monster_y = 450
monster_rect = monster_surf.get_rect(midbottom=(monster_x, monster_y))
monster_speed = 5


# herní smyčka
while running:

    # kontroluje události, které se dějí v naší hře
    for event in pygame.event.get():
        # pokud nastane událost vypnout, vypni hru
        if event.type == pygame.QUIT:
            running = False
            exit()

    # proměnná key, pod kterou schováváme stisknutou klávesu
    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        player.move_ip(0, -player_speed)
    if key[pygame.K_s]:
        player.move_ip(0, player_speed)
    if key[pygame.K_a]:
        player.move_ip(-player_speed, 0)
    if key[pygame.K_d]:
        player.move_ip(player_speed, 0)


    # obarví obrazovku na bílo
    screen.fill("white")


    monster_rect.x += monster_speed

    if monster_rect.right >= SCREEN_WIDTH:
        monster_speed *= -1
    if monster_rect.left <= 0:
        monster_speed *= -1

    # na obrazovku vykresli monster - .blit vykresluje na obrazovku, vždycky surface na rectangle
    screen.blit(monster_surf, monster_rect)

    # kulaté závorky = tuple, podobné jako list, ale efektivnější a nelze jej měnit
    pygame.draw.rect(screen, (255,0,0), player)





    # vše updatuje
    pygame.display.update()

    # pygame.display.flip() - alternativa k .update


    # omezí tickrate (rychlost hry) na 60 fps - aby hra běžela konzistentně rychle na všech zařízení
    clock.tick(60) 

pygame.quit()