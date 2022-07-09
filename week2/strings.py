#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: A script applying concepts related to string formatting. I'll be recreating the example output given in the Lab document as per the rules.


# Variable Library - Defined variables exactly as written in assignment
varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295


# Print statements to replicate output listed in String Formatting Lab Document
print(f"Hello {varName}")
print(f"{varRed}-{varGreen}-{varBlue}")
print(f"Is this {varGreen.lower()} or {varBlue.lower()}?")
print(f"My name is {varName.upper()}")
print(f"[{varRed:+^7s}]")
print(f"[{varGreen.lower():=<7s}]")
print(f"[{varBlue.lower():*>9s}]")
print(varBlue * 10)
print(varLoot)
print(f"{varLoot: <.1f}")
print(f"I have ${varLoot: <.2f}")
print(f"[{varRed:$^10s}] [{varGreen:$^10s}] [{varBlue:$^10s}]")
print(f"[{varRed[::-1]: ^10s}] [{varGreen: ^10s}] [{varBlue[::-1]: ^10s}]")
print(f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")
