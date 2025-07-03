from abc import ABC, abstractmethod
class Vehical(ABC):

    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehical):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("You stop the car")

car = Car()

car.go()
car.stop()
