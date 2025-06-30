class Animal:
    def __init__ (self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Deer(Prey):
    pass

class Lion(Predator):
    pass

class Fish(Prey, Predator):
    pass

deer = Deer("cho")

lion = Lion("leo")

fish = Fish("fishy")

deer.sleep()
deer.eat()
deer.flee()

lion.sleep()
lion.eat()
lion.hunt()

fish.sleep()
fish.eat()
fish.hunt()
fish.flee()