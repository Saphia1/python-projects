#import modules
import random
import time

#setup files:
scoretable = open("scores.txt", "w")

#Setup User 1:
Username_1 = "PLAYER_1"
Password_1 = "hat"

#Setup User 2:
Username_2 = "PLAYER_2"
Password_2 = "potato"

#Login User 1:

UserAttempt = input("Hello! Please enter your username for PLAYER 1 ") # ask for username

while UserAttempt != Username_1: # Loop to get correct input
    UserAttempt = input("Wrong ! Try again! ")
    print(" ")

print("Correct!")


time.sleep(1)

PassAttempt = input("Please enter your Password for PLAYER 1 ")

while PassAttempt != Password_1:
    PassAttempt = input("Wrong! Try again! ")
    print(" ")


print("Correct! Welcome to the game PLAYER 1")

time.sleep(1)

name1 = input("What is your name: ", Username_1)

time.sleep(1)

UserAttempt = input("Please enter the username for PLAYER 2 ")
while UserAttempt != Username2:
    UserAttempt = input("Wrong ! Try again! ")
    print(" ")

PassAttempt = input("Please enter your Password for PLAYER 2 ")

while PassAttempt != Password_2:
    PassAttempt = input("Wrong! Try again! ")
    print(" ")


print("Correct! Welcome to the game PLAYER 2")

time.sleep(1)

name1 = input("What is your name: ", Username_2)

time.sleep(1)

