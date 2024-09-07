#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:


    APPROVED_BREEDS = ["Pug", "Bulldog", "Poodle", "Chihuahua", "Labrador"]

    def __init__(self, name=None, breed=None):

        if name is not None:
            self.set_name(name)
        else:
            self.name = None

        if breed is not None:
            self.set_breed(breed)
        else:
            self.breed = None

    def set_name(self, name):
   
        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name

    def set_breed(self, breed):
     
        if breed not in self.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self.breed = breed



