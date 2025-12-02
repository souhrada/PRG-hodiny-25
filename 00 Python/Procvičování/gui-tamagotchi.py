from sys import exit
import datetime as dt
import json
import os
from nicegui import ui


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




def krmeni():
    kocka["hlad"] -= 10
    print(f"{kocka["jméno"]} vypadá šťastně.\nHlad je {kocka["hlad"]}." )

def zkontroluj_status():
    if kocka["hlad"] > 120 or kocka["hlad"] < -20:
        kocka["životy"] -= 10 

    if kocka["životy"] <= 0:
        kocka["žije"] = False
        print(f"{kocka["jméno"]} umřel.")
        exit()


def hra():
    kocka["energie"] -= 10
    kocka["žízeň"] += 10
    kocka["hlad"] += 10
    kocka["nešťastnost"] = False
    print(f"Hraješ aport s {kocka["jméno"]}. {kocka["jméno"]} je šťastný")

def spanek():
    kocka["energie"] = 100
    print(f"Zzz... zzz... zzz..")
    print(f"{kocka["jméno"]} se vzbudil s plně odpočatý, energie je {kocka["energie"]}")

def vypis_status():
    print(f"""
        Hlad je: {kocka["hlad"]}
        Žízeň je: {kocka["žízeň"]}
        Energie je: {kocka["energie"]}
        Zdraví je: {kocka["životy"]}
        {kocka["jméno"]} je {"Šťastný" if kocka["nešťastnost"] == False else "Nešťastný"}
          """)

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
    # TODO reset hry
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


def main():

    tlacitka = {
        "Krmení": krmeni,
        "Hra": hra,
        "Spánek": spanek,
    }

    load_game()

    with ui.element("div").classes("w-full h-screen flex items-center justify-center flex-col gap-5"):
        ui.label("Vítej")
        with ui.grid(columns=3):
            for jmeno, funkce in tlacitka.items():
                ui.button(jmeno, on_click=funkce)

    print("Vítej!")
    print("""
        |\\---/|
        | o_o |
         \\_^_/
          """)
    
    
    hladoveni()
    starnuti()
    zkontroluj_status()
    save_game()

    ui.run(native=True)

main()

