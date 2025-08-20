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
        self.coins = 0

    def stats(self):
        print(f"Stats for {self.name}: ")
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Dirty: {self.dirty}")
        print(f"Health: {self.health}")
        print(f"Energy: {self.energy}")
        print(f"Coins: {self.money}")

    def needs(self):
        if self.health >= 50 and self.hunger >= 50 and self.energy >= 50:
            return f"Everything is fine with {self.name}!!"
        elif self.health >= 50 and self.hunger >= 50 and self.energy <= 50:
            return f"You should go play with {self.name}!"
        elif self.health >= 50 and self.hunger <= 50 and self.energy <= 50:
            return f"You should feed and play with {self.name}!!"

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

    def play(self):
        if self.energy >= 20:
            print(f"You played some games with {self.name}")
            print(f"Energy -15")
            self.energy -= 15
        else:
            print(f"{self.name} is tired right now.")

class MiniGames:
    def __init__(self):
        self.coins = 0

    def numberGuessing(self):
        number = random.randint(1, 10)
        guess = int(input("Enter a number between 1 - 10: "))
        try:
            if guess == number:
                print("Correct!!")
                print("Coins +5")
                self.coins += 5
            else:
                print("Incorrect.")
        except ValueError:
            print("Enter a number in a range 1 to 10.")

    def coinFlip(self):
        pass

class Game:
    def __init__(self):
        self.pet = None

    def clearScreen(self):
        sys.stdout.write("\0333[H\0333[J")
        sys.stdout.flush

    def pause(self, seconds=5):
        time.sleep(seconds)
    
    def main(self):
        self.clearScreen()
        print("====== Tamagotchi ======")
        if self.pet == None:
            self.pet_name = input("Enter your pets name: ")
            self.pet = Tamagotchi(self.pet_name)
        else:
            while True:
                if self.pet == None:
                    self.pet_name = input("Enter your pets name: ")
                    self.pet = Tamagotchi(self.pet_name)
                else:
                    self.clear_screen()
                    print("=== MENU ===")
                    print("1) Show stats")
                    print("2) Show needs")
                    print("3) Feed")
                    print("4) Play")
                    print("5) Quit")

                    try:
                        choice = int(input("$ "))
                    except ValueError:
                        print("\nInvalid choice. Please enter a number.")
                        self.pause(2)
                        continue

                    if choice == 1:
                        self.clear_screen()
                        print(self.pet)
                        self.pause()
                    elif choice == 2:
                        self.clear_screen()
                        print(self.pet.needs())
                        self.pause(3)
                    elif choice == 3:
                        self.clear_screen()
                        self.pet.feed()
                        self.pause(3)
                    elif choice == 4:
                        self.clear_screen()
                        self.pet.play()
                        self.pause(3)
                    elif choice == 5:
                        self.clear_screen()
                        print(f"Goodbye! {self.pet.name} will miss you!")
                        self.pause(1.5)
                        break
                    else:
                        print("\nInvalid option, please choose between 1 and 5.")
                        self.pause()


if __name__ == '__main__':
    Game().main()
