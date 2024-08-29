#!/usr/bin/env python3


class Person:
    def __init__(self,name) :
        self.name=name
        pass

from person import Person

liz = Person("Liz")
print(liz.name) 