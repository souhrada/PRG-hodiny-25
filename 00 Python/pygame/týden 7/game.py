import pygame
from sys import exit
from settings import *
from utility import image_cutter
from player import Player
from monster import Monster

# inicializuje hru - spustíme pygame
pygame.init()


def reset_game():
    global  game_state

    player.sprite.lives = 3
    player.sprite.rect.topleft = (50, 100)
    game_state = "playing"



# vytvoření obrazu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# vytvoř hodiny
clock = pygame.time.Clock()

running = True


font = pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 25)
font_game_over = pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 50)


restart_btn_w = 200
restart_btn_h = 60
restart_btn = pygame.Rect(0, 0, restart_btn_w, restart_btn_h)
restart_btn.center = (screen_rect.centerx, screen_rect.centery + 100)
restart_btn_color = "#FF0000"
restart_btn_hover_color = "#F76969"
restart_btn_text_color = "#FFFFFF"

restart_btn_font = pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 25)
restart_btn_text = restart_btn_font.render("Restart", False, restart_btn_text_color)


player = pygame.sprite.GroupSingle()
player.add(Player())

monsters = pygame.sprite.Group()
monsters.add(Monster())

# počáteční hodnota časomíry
elapsed_time = 0

game_state = "playing"

# herní smyčka
while running:

    # kontroluje události, které se dějí v naší hře
    for event in pygame.event.get():
        # pokud nastane událost vypnout, vypni hru
        if event.type == pygame.QUIT:
            running = False
            exit()
        
        if game_state == "game_over":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_btn.collidepoint(event.pos):
                    reset_game()

    # proměnná key, pod kterou schováváme stisknutou klávesu
    key = pygame.key.get_pressed()


    if game_state == "playing":

        # obarví obrazovku na bílo
        screen.fill("white")

        # render fontu
        text_lives = font.render(f"Lives: {player.sprite.lives}", False, "#000000")
        # vykreslení textu na obrazovku
        screen.blit(text_lives, (SCREEN_WIDTH-100, 10))



       

        # na obrazovku vykresli monster - .blit vykresluje na obrazovku, vždycky surface na rectangle
        monsters.draw(screen)
        monsters.update()

        # kulaté závorky = tuple, podobné jako list, ale efektivnější a nelze jej měnit
        # pygame.draw.rect(screen, (255,0,0), player)

        player.draw(screen)
        player.update()

        # zapni časomíru - pod proměnnou elapsed_time přidávej čas
        elapsed_time += clock.get_time()
        
        # if player_rect.colliderect(monster_rect):
        #     # if invulerability == False:
        #     # alternativní, používaný zápis
        #     if not invulnerability: 
        #         print("Auuu!")
        #         player_lives -= 1 # odeberat život
        #         invulnerability = True # zapni nesmrtelnost
        #         elapsed_time = 0 # vynuluj časomíru
        
        if elapsed_time > 2000:
            invulnerability = False

        if player.sprite.lives <= 0:
            game_state = "game_over"


    elif game_state == "game_over":

        mouse_pos = pygame.mouse.get_pos()

        screen.fill("black")
        text_game_over = font_game_over.render(f"Game over", False, "#FFFFFF")
        text_game_over_rect = text_game_over.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(text_game_over, text_game_over_rect)

        if restart_btn.collidepoint(mouse_pos):
            pygame.draw.rect(screen, restart_btn_hover_color, restart_btn, border_radius=10)
        else:
            pygame.draw.rect(screen, restart_btn_color, restart_btn, border_radius=10)

        screen.blit(restart_btn_text, (restart_btn.centerx - restart_btn_text.get_width() / 2, 
                                       restart_btn.centery - restart_btn_text.get_height() / 2))


    # vše updatuje
    pygame.display.update()

    # pygame.display.flip() - alternativa k .update


    # omezí tickrate (rychlost hry) na 60 fps - aby hra běžela konzistentně rychle na všech zařízení
    clock.tick(60) 

pygame.quit()