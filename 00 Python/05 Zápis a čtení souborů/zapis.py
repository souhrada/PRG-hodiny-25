seznam = ["Ciao", "Guten tag", "Bonjour"]

# "w" write přepíše celý soubor, "a" append dopíše do souboru
with open("ukazka2.txt", "w", encoding="utf-8") as soubor:
    soubor.write("Ahoj!\n")
    soubor.write("Bye!\n")
    # soubor.writelines(seznam)
    for radek in seznam:
        soubor.write(radek + "\n")