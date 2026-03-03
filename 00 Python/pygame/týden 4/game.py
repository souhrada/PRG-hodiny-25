import pygame
from sys import exit

# inicializuje hru - spustíme pygame
pygame.init()

# funkce na vyřezávání obrázku ze spritesheetu
def image_cutter(sheet, frame_x, frame_y, width, height, scale):
    img = pygame.Surface((width, height)).convert_alpha() # Surface, na které později vykreslíme správnou část sprisheetu
    # na surface blitneme část spritesheetu, na surface blitujeme z 0,0
    # frame_x je číslo, kterým budeme manipulovat a určuje, kde na ose x vyřezáváme - násobíme jej vždy šířkou - např. 2 * šířka začne vyřezávat ve třetím sloupci framů  (např. 2*15 začne vyřezávat z 30 pixelu na x, takže ignoruje první dva framy)
    # frame_y je číslo, kterým budeme manipulovat a určuje, kde na ose y vyřezáváme - násobíme jej vždy výškou - např. 3 * výška začne vyřezávat ve čtvrté řadě spritesheetu framů (např. 3*15 začne vyřezávat z 45 pixelu na y, takže ignoruje první tři řady)
    # výška a šířka udává velikost vyřezávátka
    img.blit(sheet, (0, 0), ((frame_x * width), (frame_y * height), width, height)) 
    img = pygame.transform.scale(img, (width * scale, height* scale)) # obrázek zvětšíme, pokud je potřeba
    img.set_colorkey((0,0,0)) # tento údaj změní černou barvu na průhlednou, což je potřeba pro správné vykreslení průhlednosti
    return img # funkce vrátí vytvořený obrázek

def player_animation(direction):
    global  player_img, player_index
    frame_count = 3

    player_index += 0.1


    if player_index >= frame_count:
        player_index = 0
    
    player_img = image_cutter(player_spritesheet, int(player_index), direction, 15, 16, 3) 


def reset_game():
    global player_lives, game_state

    player_lives = 3
    player_rect.topleft = (50, 100)
    game_state = "playing"

def monster_animation():
    # importujeme globální proměnné, které přepisujeme
    global monster_surf, monster_index

    # animace zjednodušeně - loopujeme listem, ve kterém jsou obrázky v rúzné fázi pohybu
    # vykreslujeme vždy jeden obrázek
    # index zvolí, který obrázek vykreslujeme
    
    monster_index += 0.1 # index měníme 0.1, aby byla animace pomalejší

    # pokud je index větší, než množství obrázků v listu (délka listu), vyresetujeme index
    if monster_index > len(monster_images):
        monster_index = 0

    # jelikož poujžíváme desetinná čísla v indexu, je potřeba jej zaokrouhlit pomocí funkce int() - ta zaokrouhluje vždy dolu
    monster_surf = monster_images[int(monster_index)]


# caps lock označuje konstanty - proměnné, které by se neměly měnit
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


# vytvoření obrazu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# vytvoř hodiny
clock = pygame.time.Clock()

running = True


font = pygame.font.Font("PixelifySans-Regular.ttf", 25)
font_game_over = pygame.font.Font("PixelifySans-Regular.ttf", 50)

player_x = 150
player_y = 150
player_spritesheet = pygame.image.load("man_brownhair_run.png").convert_alpha() 
player_img = image_cutter(player_spritesheet, 0, 0, 15, 16, 3) 
player_rect = player_img.get_rect(midbottom=(player_x, player_y))
player_index = 0

player_speed = 5
player_lives = 3
invulnerability = False


monster_idle = pygame.image.load("monster.png").convert_alpha()
monster_idle = pygame.transform.scale(monster_idle, (monster_idle.get_width()*6, monster_idle.get_height()*6))
monster_run1 = pygame.image.load("monster-run1.png").convert_alpha()
monster_run1 = pygame.transform.scale(monster_run1, (monster_run1.get_width()*6, monster_run1.get_height()*6))
monster_run2 = pygame.image.load("monster-run2.png").convert_alpha()
monster_run2 = pygame.transform.scale(monster_run2, (monster_run2.get_width()*6, monster_run2.get_height()*6))

monster_images = [monster_idle, monster_run1, monster_run2]
monster_index = 0
monster_surf = monster_images[monster_index]

monster_x = 50
monster_y = 450
monster_rect = monster_surf.get_rect(midbottom=(monster_x, monster_y))
monster_speed = 5

restart_btn_w = 200
restart_btn_h = 60
restart_btn = pygame.Rect(0, 0, restart_btn_w, restart_btn_h)
restart_btn.center = (screen_rect.centerx, screen_rect.centery + 100)
restart_btn_color = "#FF0000"
restart_btn_hover_color = "#F76969"
restart_btn_text_color = "#FFFFFF"

restart_btn_font = pygame.font.Font("PixelifySans-Regular.ttf", 25)
restart_btn_text = restart_btn_font.render("Restart", False, restart_btn_text_color)


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


        if key[pygame.K_w]:
            player_animation(1)
            player_rect.y -= player_speed
        if key[pygame.K_s]:
            player_animation(0)
            player_rect.y += player_speed
        if key[pygame.K_a]:
            player_animation(2)
            player_rect.x -= player_speed
        if key[pygame.K_d]:
            player_animation(3)
            player_rect.x += player_speed


        # obarví obrazovku na bílo
        screen.fill("white")

        # render fontu
        text_lives = font.render(f"Lives: {player_lives}", False, "#000000")
        # vykreslení textu na obrazovku
        screen.blit(text_lives, (SCREEN_WIDTH-100, 10))


        monster_rect.x += monster_speed
        monster_animation()

        if monster_rect.right >= SCREEN_WIDTH:
            monster_speed *= -1
        if monster_rect.left <= 0:
            monster_speed *= -1

        # na obrazovku vykresli monster - .blit vykresluje na obrazovku, vždycky surface na rectangle
        screen.blit(monster_surf, monster_rect)

        # kulaté závorky = tuple, podobné jako list, ale efektivnější a nelze jej měnit
        # pygame.draw.rect(screen, (255,0,0), player)

        screen.blit(player_img, player_rect)

        # zapni časomíru - pod proměnnou elapsed_time přidávej čas
        elapsed_time += clock.get_time()
        
        if player_rect.colliderect(monster_rect):
            # if invulerability == False:
            # alternativní, používaný zápis
            if not invulnerability: 
                print("Auuu!")
                player_lives -= 1 # odeberat život
                invulnerability = True # zapni nesmrtelnost
                elapsed_time = 0 # vynuluj časomíru
        
        if elapsed_time > 2000:
            invulnerability = False

        if player_lives <= 0:
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