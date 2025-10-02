jmena = [
    "Adam", "Jana", "Filip", "Marie", "Tomáš", "Klára", 
    "David", "Eva", "Martin", "Petra", "Jakub", "Lenka", 
    "Michal", "Anna", "Roman", "Lucie", "Pavel", "Tereza", 
    "Karel", "Veronika"
]


print(jmena[2])
print(jmena[-1]) # -1 je poslední položka v seznamu
print(jmena[1:4]) # 1 až 4 (ne včetně) položka v seznamu
print(jmena[:11])
print(jmena[14:])

# append přidává položku do seznamu
jmena.append("Radek")

# pro přepisování položky používáme =
jmena[2] = "Emil"

# insert vkládá položku na určitý index
jmena.insert(0, "Max")

# pop odebírá položku na základě indexu a umožní nám ji uložit pod proměnnou
odebrana_hodnota = jmena.pop(5)

print(f"Odebral jsem {odebrana_hodnota}")

# remove odebírá položku na základě hodnoty
jmena.remove("David")

print(jmena)

for i, jmeno in enumerate(jmena):
    print(f"{i+1}. {jmeno}")