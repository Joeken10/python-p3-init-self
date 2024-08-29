#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
        pass

from dog import Dog


fido = Dog("Fido", "Dalmatian")
print(fido.name) 
print(fido.breed) 
husky = Dog("Husky")
print(husky.name) 
print(husky.breed) 


