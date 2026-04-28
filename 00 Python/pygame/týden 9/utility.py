import pygame

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