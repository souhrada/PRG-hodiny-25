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
    while True:
        print(f"Pro nakrmení {kocka["jméno"]} stikni k. \nPro ukončení napiš konec")

        uziv_input = input()

        if uziv_input.lower() == "konec":
            print("Ukončení programu... bye!")
            break
        elif uziv_input.lower() == "k":
            krmeni()
        
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

main()
