from sys import exit


kocka = {
    "jméno": "Aladin",
    "hlad": 50,
    "žízeň": 0,
    "barvu": "fialová",
    "životy": 100,
    "čistota": 100,
    "energie": 90,
    "žije": True,
    "věk": 0,
    "nešťastnost": False,
    "nemoc": False,
}

def main():
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
        
        zkontroluj_status()


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

if __name__ == "__main__":
    main()

