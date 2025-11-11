uziv_input = input("Stiskni klávesu...")

if uziv_input.lower() == "a":
    print("Uživatel napsal a")
elif uziv_input.lower() == "b":
    print("Uživatel napsal b")
elif uziv_input.lower() == "c":
    print("Uživatel napsal c")
elif uziv_input.lower() == "d":
    print("Uživatel napsal d")
else:
    print("Žádná z možností")

match uziv_input.lower():
    case "a":
        print("Uživatel napsal a")
    case "b":
        print("Uživatel napsal b")
    case "c":
        print("Uživatel napsal c")
    case "d":
        print("Uživatel napsal d")
    case _: # tohle znamená else
        print("Žádná z možností")

