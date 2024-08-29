#!/usr/bin/env python3


class Person:
    def __init__(self,name) :
        self.name=name
        pass

from person import Person

alice = Person("Alice")
print(alice.name)  # Output: Alice