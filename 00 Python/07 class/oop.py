import random

class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.alive = True
        self.type = type

    def choose(self):
        print(f"{self.name} I choose you!")
    
    def attack(self, attack_type):
        if self.type == attack_type:
            print(f"{self.name} does {random.randint(20,50)} damage")
        else:
            print(f"{self.name} cannot do that!")
    

pikachu = Pokemon("Pikachu", "electric")

print(pikachu.name)
print(pikachu.alive)

pikachu.choose()
pikachu.attack("electric")
pikachu.attack("water")

charmander = Pokemon("Charmander", "fire")
charmander.attack("fire")


class Pokemon_S1(Pokemon):
    def __init__(self, name, type, level):
        super().__init__(name, type)
        self.level = level
    
    def evolve(self):
        print(f"{self.name} has evolved")


charmeleon = Pokemon_S1("Charmeleon", "fire", 2)
print(charmeleon.level)
print(charmeleon.type)
charmeleon.attack("fire")
charmeleon.evolve()