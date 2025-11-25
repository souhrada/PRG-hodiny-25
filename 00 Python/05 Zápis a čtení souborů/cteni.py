with open("ukazka.txt", "r", encoding="utf-8") as soubor:
    # obsah = soubor.read() # přečtení souboru najednou
    # obsah = soubor.read().splitlines() - přečtení řádků bez whitespaces a neviditelných znaků
    obsah = soubor.readlines()

print(obsah)
print(obsah[1].strip()) # .strip() vymaže whitespaces a neviditelné znaky ze stringu

for radek in obsah:
    print(radek.strip())

