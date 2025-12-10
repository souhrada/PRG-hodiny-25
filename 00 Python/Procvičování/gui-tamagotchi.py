import datetime as dt
import json
import os
from nicegui import ui
from PIL import Image # knihovna pillow, určena pro práci s obrázky

# globální proměnné, se kterými pracujeme v různých funkcích
zprava = None
obrazek = None
spritesheet = Image.open("cat.png") # otevření obrázku v pillow

kocka = {}
default_kocka = {
            "jméno": "Aladin",
            "hlad": 50,
            "žízeň": 0,
            "barvu": "fialová",
            "životy": 100,
            "čistota": 100,
            "energie": 100,
            "žije": True,
            "věk": 0,
            "nešťastnost": False,
            "nemoc": False
        }

puvodni_cas = dt.datetime.now()


# Funkce:

def krmeni():
    kocka["hlad"] -= 10
    print(f"{kocka["jméno"]} vypadá šťastně.\nHlad je {kocka["hlad"]}." )
    zprava.text = (f"{kocka["jméno"]} vypadá šťastně.\nHlad je {kocka["hlad"]}." )
    zkontroluj_status()

# funkce zkontroluj status, kterou spouštíme v ostatních funkcích a která kontroluje také
# hladovění, stárnutí a spouští ukládání hry
def zkontroluj_status():
    if kocka["hlad"] > 120 or kocka["hlad"] < -20:
        kocka["životy"] -= 10 

    if kocka["životy"] <= 0:
        kocka["žije"] = False
        print(f"{kocka["jméno"]} umřel.")
        
    hladoveni()
    starnuti()
    save_game()


def hra():
    kocka["energie"] -= 10
    kocka["žízeň"] += 10
    kocka["hlad"] += 10
    ui.notify("Energie + 10")
    ui.notify("Hlad +10")
    ui.notify("Žízeň + 10")
    kocka["nešťastnost"] = False
    print(f"Hraješ aport s {kocka["jméno"]}. {kocka["jméno"]} je šťastný")
    # jelikož neměníme celou proměnnou ale pouze .text, není potřeba global zprava
    zprava.text = f"Hraješ aport s {kocka["jméno"]}. {kocka["jméno"]} je šťastný" 
    zkontroluj_status()

def spanek():
    kocka["energie"] = 100
    print(f"{kocka["jméno"]} se vzbudil s plně odpočatý, energie je {kocka["energie"]}")
    zprava.text = f"Zzz... zzz... zzz.."
    ui.notify(f"Energie je {kocka["energie"]}")
    # jelikož neměníme celou proměnnou ale pouze .source, není potřeba global obrazek
    obrazek.source = vystrihni_obrazek(0, 45)
    zkontroluj_status()


def vypis_status():
    print(f"""
        Hlad je: {kocka["hlad"]}
        Žízeň je: {kocka["žízeň"]}
        Energie je: {kocka["energie"]}
        Zdraví je: {kocka["životy"]}
        {kocka["jméno"]} je {"Šťastný" if kocka["nešťastnost"] == False else "Nešťastný"}
          """)
    zkontroluj_status()


def hladoveni():
    global puvodni_cas

    ted = dt.datetime.now()

    if ted > puvodni_cas + dt.timedelta(minutes=10):
        kocka["hlad"] += 10
        print(f"{kocka["jméno"]} začíná mít hlad...")
        puvodni_cas = ted # aby kód kontroloval každých 10 minut, je potřeba nahradit původní čas

        
def starnuti():
    global puvodni_cas

    ted = dt.datetime.now()

    if ted > puvodni_cas + dt.timedelta(hours=1):
        kocka["věk"] += 1
        print(f"{kocka["jméno"]} má narozeniny!")
        puvodni_cas = ted 

def load_game():
    global kocka, default_kocka
    
    if os.path.exists("save_data.json"):
        with open("save_data.json", "r", encoding="utf-8") as f:
            kocka = json.load(f)
    else:
        kocka = default_kocka
        save_game()


def save_game():
    global kocka
    with open("save_data.json", "w", encoding="utf-8") as f:
        json.dump(kocka, f, ensure_ascii=False, indent=4)

def reset_game():
    global kocka, default_kocka
    kocka = default_kocka
    save_game()

# vystřihni obrázek přijímá x a y a aplikuje je na funkci crop() z knihovny pillow
# crop() sama o sobě funguje zvláštně, naše pomocná funkce nám vytváří jednodušší kód
# ze spritesheetů můžeme snadno vykreslit obrázek tím, že zadáme pozici na x (v řadě) a y (sloupci)
def vystrihni_obrazek(x, y):
    x = x * 64
    y = y * 64

    # vracíme vyříznutý obrázek
    # crop vyřezeává (zleva, zhora, zprava, zespod)
    # naše funkce to mění na x a y podle velikosti obrázku ve spritesheetu (u nás 64x64 pixelů)
    return spritesheet.crop((x, y, x + 64, y + 64))
    

def main():
    # jelikož budeme měnit zprava a obrazek, musíme na ně odkázat pomocí global
    global zprava, obrazek

    # názvy tlačítek a funkce, které spouštějí
    tlacitka = {
        "Krmení": krmeni,
        "Hra": hra,
        "Spánek": spanek,
    }

    load_game()

    # vytvoření divu, kterému dáváme flex a tím vycentrujeme ui
    with ui.element("div").classes("w-full h-screen flex items-center justify-center flex-col gap-5"):
        # vykreslení obrázku, pro které voláme vlastní pomocnou funkci vystrihni_obrazek
        obrazek = ui.image(vystrihni_obrazek(0, 0)).classes("h-32 w-32") # zmenšení obrázku na 32x32 pixelů
        zprava = ui.label("Vítej")
        with ui.grid(columns=3):
            for jmeno, funkce in tlacitka.items():
                ui.button(jmeno, on_click=funkce)

    print("Vítej!")
    print("""
        |\\---/|
        | o_o |
         \\_^_/
          """)
    
    

    zkontroluj_status()

    # spuštění aplikace v native nám skryje okno prohlížeče
    ui.run(native=True)

main()

