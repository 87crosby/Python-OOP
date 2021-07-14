class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(name=pet)
    
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(self.pet.noise())
        return self

class Pet:
    def __init__(self,name,type='dog',tricks='flop',health=100,energy=100):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=health
        self.energy=energy
    
    def displayHealth(self):
        return self.health

    def displayEnergy(self):
        return self.energy

    def sleep(self):
        self.energy=self.energy + 25
        return self
    
    def eat(self):
        self.energy=self.energy + 5
        self.health=self.health + 10
        return self
    
    def play(self):
        self.health=self.health + 5
        return self
    
    def noise(self):
        return self.tricks

ninjago = Ninja('Joe','Stalin','Bacon','Dog Food','Beria')
ninjago.walk().feed().bathe()
print(ninjago.pet.displayHealth())
print(ninjago.pet.displayEnergy())