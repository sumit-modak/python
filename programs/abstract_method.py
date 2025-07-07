from abc import ABC, abstractmethod

# abstract class = a class which contain one or more abstract method
# abstract method = a method that has declaration but does not have implementation

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        print("the vehicle is running")

    @abstractmethod
    def stop(self):
        print("the vehicle is stopped")

class Car(Vehicle):

    def go(self):
        print("the car is moving")

    def stop(self):
        print("the car is stopped")
    
class Bike(Vehicle):

    def go(self):
        print("the bike is running")

    def stop(self):
        print("the bike is stopped")


# vehicle = Vehicle()
car = Car()
bike = Bike()

# vehicle.go()
car.go()
bike.go()

# vehicle.stop()
car.stop()
bike.stop()