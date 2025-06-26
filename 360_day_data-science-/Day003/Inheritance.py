# Inheritance
class Animal:# parent 
    def __init__(self, name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating")  
    
    def sleep(self):
        print(f"{self.name} is seelping")

# child
class Dog(Animal):
    def speek(self):
        print("boow!!")

class Cat(Animal):
    def speek(self):
        print("mewo!!")
    
class Bird(Animal):
    def speek(self):
        print("humming!!")
    

dog = Dog("Max")
cat = Cat("Tommy")
bird = Bird("little put")

dog.eat()
dog.sleep()
dog.speek()

cat.eat()
cat.sleep()
cat.speek()

bird.eat()
bird.sleep()
bird.speek()