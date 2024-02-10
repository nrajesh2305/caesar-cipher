from hacker import *

printIntro()
eOrD = input("Do you want to (e)ncrypt or d(ecrypt)?\n")

while(eOrD != "e" and eOrD != "d"):
    print("That's not a valid input, please try again.")
    eOrD = input("Do you want to (e)ncrypt or d(ecrypt)?\n")

if eOrD == "e":
    key = int(input("Please enter the key (0 to 25) to use: "))
    while(key < 0 or key > 25):
        print("That's not a valid input, please try again.")
        key = int(input("Please enter the key (0 to 25) to use: "))
    message = input("Enter the message to encrypt.\n")
    print(encrypt_message(message, key))
else:
    key = int(input("Please enter the key (0 to 26) to use: "))
    while(key < 0 or key > 26):
        print("That's not a valid input, please try again.")
        key = int(input("Please enter the key (0 to 25) to use: "))
    message = input("Enter the message to decrypt.\n")
    print(decrypt_message(message, key))