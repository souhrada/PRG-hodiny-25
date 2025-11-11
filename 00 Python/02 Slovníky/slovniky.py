# dictionary (slovník) soubor zpárovaných klíčů a hodnot (key - value)
# levá strana = key, pravá strana = value

telefonni_seznam = {
    "Emil": "723 111 222",
    "Anděla": "777 666 555",
    "Kvído": "735 123 321",
}

print(telefonni_seznam["Anděla"])


cat = {
    "jméno": "Garfield",
    "věk": 15,
    "barva": "oranžová",
    "žije": True,
    "oblíbené_jídlo": "lasagne",
    "kamarádi": ["Pes", "Další kočka", "Kuchař"],
}

print(cat)
print(cat["barva"])
print(cat["kamarádi"][2])

for klic in cat:
    print(klic)

for klic, hodnota in cat.items():
    print(f"Klíč {klic}, hodnota {hodnota}")

# vypiš všechny hodnoty
for klic in cat:
    print(cat[klic])

# alternativní způsob, jak vypsat všechny hodnoty
for hodnota in cat.values():
    print(hodnota)


for kamarad in cat["kamarádi"]:
    print(kamarad)

cat["klubko"] = "6m"

print(cat)

cat["věk"] = 16

if "oblíbené_jídlo" in cat:
    print("Má oblíbené jídlo")

print(cat["věk"])