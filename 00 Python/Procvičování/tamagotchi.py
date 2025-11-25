from sys import exit
import datetime as dt
import json


kocka = {}

puvodni_cas = dt.datetime.now()

def main():
    load_game()

    print("Vítej!")
    print("""
        |\\---/|
        | o_o |
         \\_^_/
          """)
    while True:
        print(f"Pro nakrmení {kocka["jméno"]} stikni k. \nPro ukončení napiš konec")

        uziv_input = input()
       
        match uziv_input.lower():
            case "konec":
                print("Ukončení programu... bye!")
                break
            case "k":
                krmeni()
            case "h":
                hra()
            case "s":
                spanek()
            case "v":
                vypis_status()
            case _:
                print("Neplatná klávesa")
        
        hladoveni()
        starnuti()
        zkontroluj_status()
        save_game()


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
    # TODO reset hry, kontrola existence save_game.json
    global kocka
    with open("save_data.json", "r", encoding="utf-8") as f:
        kocka = json.load(f)

def save_game():
    global kocka
    with open("save_data.json", "w", encoding="utf-8") as f:
        json.dump(kocka, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()

