import random

def animals(n):
    if n > 10:
        cislo_ruzove_ovce = random.randint(1, n) # vybere náhodné číslo od 1 do n

    for cislo_ovce in range(n):
        if cislo_ovce == cislo_ruzove_ovce:
            print("růžová ovce")
        else:
            print("ovce")
        
    print("pes")


animals(15)