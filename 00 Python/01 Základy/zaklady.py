print("Dobrý den géčko!")

jmeno = "Jarmil"
cislo = 5
bool = True
des_cislo = 5.5

# Komentář

print(jmeno)

seznam_studentu = ["Hugo", "Anděla", "Fridolína", "Jeroným"]

if cislo == 5:
    print(bool)
elif cislo > 5:
    print("číslo je větší než 5")
else:
    print("číslo je menší než 5")


# if cislo > 5:
#     print("číslo je větší než 5")
# elif cislo > 10:
#     print("číslo je větší než 10")

# if cislo > 5:
#     print("číslo je větší než 5")
# if cislo > 10:
#     print("číslo je větší než 10")


for student in seznam_studentu:
    print(student)

for x in range(1, 6):
    print(x)

for y in range(11):
    print(y)

# range(od kolika, do kolika, po kolika)
for z in range(20, 5, -1):
    print(z)


pocitadlo = 1
while pocitadlo < 11:
    print(pocitadlo)
    pocitadlo += 1 # pocitadlo = pocitadlo + 1; python neumí pocitadlo++

# def vytváří funkci
def pozdrav():
    print("Dobrý den")
    print("Ahoj")
    print("Nashledanou")

pozdrav()
pozdrav()