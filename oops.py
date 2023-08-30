import random

class Animal:
    alive = True
    def eat():
        print("this animal is eating")
    def die():
        alive = False
        print("this animal has died")

class Mammal(Animal): 
    def give_birth(self, max):
        count = random.randint(0, max+1)
        return count 

class Fish(Animal):
    def lay_eggs():
        return random.randint(1, 7)

class Bird(Animal):
    def lay_eggs():
        return random.randint(1, 7)
    
    def fly():
        print("the bird is flying")
