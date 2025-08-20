import sys
import random
import datetime
import time

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.dirty = 0
        self.health = 100
        self.light = True
        self.energy = 50
        self.alive = True
        self.sick = False

    def stats(self):
        print(f"Stats for {self.name}: ")
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Dirty: {self.dirty}")
        print(f"Health: {self.health}")
        print(f"Energy: {self.energy}")

    def feed(self):
        if self.hunger <= 90:
            print(f"You fed {self.name}.")
            print(f"Hunger +10")
            self.hunger += 10
        elif self.hunger >= 90:
            print(f"{self.name} is not hungry right now.")
        else:
            print(f"You forgot to fed {self.name}..")
            self.alive = False

    def clean(self):
        if self.dirty <= 99:
            print(f"You cleaned {self.name}.")
            self.dirty = 0
        elif self.dirty >= 75:
            print(f"You've cleaned {self.name} but it got sick!!")
            print(f"You should do something fast!!!")
            self.dirty = 0
            self.sick = True
        else:
            print(f"{self.name} died because it got way too sick ;((")
            self.alive = False

    def health(self):
        if self.sick:
            print(f"You've healed {self.name}.")
            print(f"Health +15")
            self.sick = False
        else:
            print(f"{self.name} does not really need health care right now <3")

    def lightsOn(self):
        print("Lights on.")
        self.light = True
    
    def lightsOff(self):
        print("Lights off.")
        self.light = False

    def sleep(self):
        if self.light == False and self.energy <= 65:
            print(f"You put {self.name} to sleep")
            print("Hunger -25")
            print("Energy +25")
            print("Dirty +15")
            self.hunger -= 25
            self.energy += 25
            self.dirty += 15
        elif self.light == False and self.energy > 65:
            print(f"You should play first with {self.name} it have way to much energy!!!")
        else:
            print(f"{self.name} can't go to sleep beacuse lights are turn on!!!")

    