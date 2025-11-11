# def pozdrav(jmeno1, jmeno2):
#     print("Ahoj!", jmeno1)
#     print("Hi!", jmeno2)
#     print("Hallo!", jmeno1)
#     print("Ciao!", jmeno2)


# pozdrav("Kvído", "Anděla")
# pozdrav("Emil", "Fridolína")

zadane_km = int(input("Kolik km chceš převést na míle?: "))

def prevod(km):
    mile = km * 0.62
    return mile

vysledek = prevod(zadane_km)

print(f"Výsledek převodu je, že {zadane_km} km je {vysledek} mil!")

