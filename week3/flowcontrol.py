#!/usr/bin/env python3

#Author: George Maysack-Schlueter
#Description: This is a script from week 3 of Python scripting class. This script is for the Flow control Lab
# Description (cont.): This is a modified version of the sample game code provided in the lab document


#importing time module so I can utilize the time.sleep() function to allow for for some dramatic pauses/reading time
import re
import time

# Introduction sequence, giving user chance to enter their name, then name their ship
print("Hello Astral Traveler!")
time.sleep(2)
# Using a while loop to ensure only letters are entered as the users name. Prompt will continually ask for alphabetical input, until it is honored.
while True:
    name = input("What is your name?--> ")
    if not name.isalpha():
        print("Sorry, numbers and symbols are reserved for us robots. Try again with letters only.")
        continue
    if name.isalpha():
        print(f"Hello, Captain {name}! Thank you for confirming your identity. I must be getting outdated.")
        break
            
# Asking the user to enter the name of their ship. To help with potentially broken dialogue, I added an if/else statement to ensure the ship name is always preceded with "The"
time.sleep(2.5) 
ship = input("What is the name of your ship? Make it a good one!--> ")
# Here, we are checking if the ship name starts with the word "The". If it does, we move on. If it does not, we append it to the beginning of the name to ensure proper dialogue. 
if not ship.startswith("The" or "THE" or "the"):
    ship = f"The {ship}"
else:
    ship = ship

# A little bit of dialogue between the prompt and the user, leading into the first decision branch.
print(f"Ah, yes, {ship}! How could I have forgotten. A gorgeous vessel indeed...")
time.sleep(2.5) 
print("Albeit a bit dirty...",)
time.sleep(2)
print("and smelly.")
print("...")
time.sleep(3)
print("...")
time.sleep(3)
print(f"Anyway, I am your trusty AI companion!\nI'm here to help guide {ship} and its wonderful Captain {name} through the galaxy!")
print(f"As our first order of buisness Captain {name}, we must go get {ship} cleaned.")
time.sleep(2)
print("")
print("Would you like to head through the astroid field, or the deep void?")
print("Please enter your choice on the keypad: 1) Astroid Field 2) Deep Void or 3) Self Destruct" )
pathChoice = input("--> " )
# Astroid Field Path
if pathChoice == "1":
    print(f"This astroid field is much denser than expected... {ship} is really taking a beating! Should we go left or right?")
    print("1)Left? or 2)Right?")

# Astroid Field Logic    
# Astroid Death Ending (right)
    while True:
        astroidField = input("--> " )
        if astroidField == ("1"):
            print(f"Uh oh. You turned directly into a massive astroid that ripped the hull of {ship} apart. Captain {name} was sucked into the vacuum of space. You are dead.")
            exit()
    # Astroid Success (left)
        elif astroidField == ("2"):
            print(f"Awesome. Good choice. {ship} will live to see another day. Lets get to that shipwash!")
            time.sleep(3)
        # Ship Wash Ending'
        print("You Make your way to the shipwash, would you like to use 1)Lemon, or 2)New Ship Scent?")
        scent = input("--> " )
        if scent == ("1"):
            print(f"You chose the lemon scent. You always loved the clean, refreshing smell of lemons")
            exit()
        elif scent == ("2"):
            print(f"You chose new ship smell. You're not fooling anyone, but you do love the smell!")
            exit()
    # Deep Void Path
if pathChoice == ("2"):
    print(f"This void is much darker than expected... {ship}'s navigation systems can't tell up from down! Should we follow our head or our heart?")
    print("1)Head? or 2)Heart?")
        #deep void logic
    while True:
        deepVoid = input("--> " )
        #deep void death (head)
        if deepVoid == ("1"):
            print(f"Uh oh. You decided to follow your head, and it lead you directly into a hostile aliens dinner party. He was not happy. You got vaporized, and you are dead.")
            exit()
    # Deep void success (heart)
        elif deepVoid == ("2"):
            print(f"Awesome job Captain {name}. Always best to follow your heart. Now Lets go wash this ship a well deserved wash!")
            time.sleep(3)
        # Ship Wash Ending'
        print("You Make your way to the shipwash, would you like to use 1)Lemon, or 2)New Ship Scent?")
        scent = input("--> " )
        if scent == ("1"):
            print(f"You chose the lemon scent. You always loved the clean, refreshing smell of lemons")
            exit()
        elif scent == ("2"):
            print(f"You chose new ship smell. You're not fooling anyone, but you do love the smell!")
            exit()
            
                    # Ship Wash Ending'
        print("You Make your way to the shipwash, would you like to use Lemon, or New Ship Scent?")
    # Self Destruct Path
if pathChoice == "3":
    print("You weren't supossed to press that button...")
    time.sleep(3)
    print("Why would you press that button?!?")
    time.sleep(2)
    print(f"Oh well, goodbye Captain {name}")
    exit()
    



