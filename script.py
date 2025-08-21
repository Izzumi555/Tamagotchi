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

    def __repr__(self):
        return(f"Stats for {self.name}: \nName: {self.name} \nHunger: {self.hunger} \nDirty: {self.dirty} \nHealth: {self.health} \nEnergy: {self.energy} \nCoins: {self.coins}")

    def needs(self):
        if self.health >= 50 and self.hunger >= 50 and self.energy >= 50:
            return f"Everything is fine with {self.name}!!"
        elif self.hunger < 50 and self.energy >= 50:
            return f"{self.name} is hungry! Feed them!"
        elif self.energy < 50 and self.hunger >= 50:
            return f"{self.name} needs to rest or play!"
        elif self.health < 50:
            return f"{self.name} is sick! Heal them!"
        else:
            return f"{self.name} needs attention!"

    def feed(self):
        if self.hunger <= 90:
            print(f"You fed {self.name}.")
            print(f"Hunger +10")
            self.hunger += 10
        else:
            print(f"{self.name} is not hungry right now.")
            self.alive = False

    def clean(self):
        if self.dirty < 75:
            print(f"You cleaned {self.name}.")
            self.dirty = 0
        elif self.dirty <= 99:
            print(f"You've cleaned {self.name} but it got sick!!")
            print(f"You should do something fast!!!")
            self.dirty = 0
            self.sick = True
        else:
            print(f"{self.name} died because it got way too sick ;((")
            self.alive = False

    def heal(self):
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
        if not self.light and self.energy <= 65:
            print(f"You put {self.name} to sleep.")
            self.hunger = max(0, self.hunger - 25)
            self.energy = min(100, self.energy + 25)
            self.dirty = min(100, self.dirty + 15)
        elif not self.light:
            print(f"{self.name} has too much energy to sleep right now!")
        else:
            print(f"{self.name} can't sleep while the lights are on!")

    def play(self):
        if self.energy >= 20:
            print(f"You played some games with {self.name}")
            print(f"Energy -15")
            self.energy -= 15
        else:
            print(f"{self.name} is tired right now.")

class MiniGames:
    def __init__(self, pet):
        self.pet = pet

    def numberGuessing(self):
        number = random.randint(1, 10)
        guess = int(input("Enter a number between 1 - 10: "))
        try:
            if guess == number:
                print("Correct!!")
                print("Coins +3")
                time.sleep(2)
                self.pet.coins += 5
            else:
                print("Incorrect.")
                time.sleep(2)
        except ValueError:
            print("Enter a number in a range 1 to 10.")

    def coinFlip(self):
        flip = random.choice(["HEADS", "TAILS"])
        guess = input("Enter (heads / tails): ").upper()
        if guess == flip:
            print("Correct.")
            print("Coins +1")
            time.sleep(2)
            self.pet.coins += 1
        else:
            print("Incorrect.")
            time.sleep(2)

class Game:
    def __init__(self):
        self.pet = None

    def clearScreen(self):
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()

    def pause(self, seconds=5):
        time.sleep(seconds)
    
    def main(self):
        self.clearScreen()
        print("====== Tamagotchi ======")
        while True:
            if self.pet == None:
                self.pet_name = input("Enter your pets name: ")
                self.pet = Tamagotchi(self.pet_name)
            else:
                self.clearScreen()
                print("=== MENU ===")
                print("1) Show stats")
                print("2) Show needs")
                print("3) Feed")
                print("4) Play")
                print("5) MiniGames")
                print("6) Quit")
    
                try:
                    choice = int(input("$ "))
                except ValueError:
                    print("\nInvalid choice. Please enter a number.")
                    self.pause(2)
                    continue

                if choice == 1:
                    self.clearScreen()
                    print(self.pet)
                    self.pause()
                elif choice == 2:
                    self.clearScreen()
                    print(self.pet.needs())
                    self.pause(3)
                elif choice == 3:
                    self.clearScreen()
                    self.pet.feed()
                    self.pause(3)
                elif choice == 4:
                    self.clearScreen()
                    self.pet.play()
                    self.pause(3)
                elif choice == 5:
                    self.clearScreen()
                    print("1) Pick a number")
                    print("2) Flip a coin")
                    try:
                        choice = int(input("$ "))
                    except ValueError:
                        print("\nInvalid choice. Please enter a number.")
                        self.pause(2)
                        continue
                    if choice == 1:
                        self.clearScreen
                        MiniGames(self.pet).numberGuessing()
                    elif choice == 2:
                        self.clearScreen
                        MiniGames(self.pet).coinFlip()
                    else:
                        print("Invalid option, please choose between 1 and 2.")
                        self.pause()
                elif choice == 6:
                    self.clearScreen()
                    print(f"Goodbye! {self.pet.name} will miss you!")
                    self.pause(1.5)
                    break
                else:
                    print("\nInvalid option, please choose between 1 and 5.")
                    self.pause()


if __name__ == '__main__':
    Game().main()
