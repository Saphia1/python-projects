#import modules
import random 
import time

#setup files:

scoretable=open("scores.txt","w")
#table.write(rounds = [["Player", "\t", "Score","\t" ,"End Total","\n"], # \n -> newline, \t -> tab
#                      [name1,


User_1= "PLAYER_1"              
password1="hat" 

attemptuser=input("Hello! Please enter your username for PLAYER 1 ") 

while attemptuser != User_1: 

    attemptuser=input("Wrong! Try again! ") 

    print(" ") 

print("Correct!") 
name1=input("What is your name: PLAYER 1?")
time.sleep(1)
#scoretable.write(name1,"\n")
attemptpass=input("Please enter your Password for PLAYER 1 ") 

while attemptpass != password1: 

    attemptpass=input("Wrong! Try again! ") 

    print(" ") 

print("Correct! Welcome to the game player_1!") 

User_2="player_2" 

password2="potato" 

attemptuser=input("Please enter your username for PLAYER 2 ") 

while attemptuser != User_2: 

    attemptuser=input("Wrong! Try again! ") 

    print(" ") 

print("Correct!")
name2=input("What is your name: PLAYER 2?")
#scoretable.write(name2,"\n")
#scoretable.close()
scoretable=open("The scores.txt","r")

attemptpass=input("Please enter your Password for PLAYER 2 ") 

while attemptpass != password2: 

    attemptpass=input("Wrong! Try again! ") 

    print(" ") 

print("Correct! Welcome to the game player_2, let's play!!!") 

game= True 

while game== True: 

    for i in range (0,5): 

        ready=input("Are you ready to roll player_1? Y or N! ") 

        while ready == "N": 

            time.sleep(2) 

            ready=input("Are you ready now...?") 

            print(" ") 

        print("Great! Let's start!") 

        time.sleep(1) 

        print("Rolling...") 

        time.sleep(1) 

        print("You rolled a...") 

        time.sleep(1) 

        roll_1=random.randint(1,6) 

        print(roll_1)    

        time.sleep(2) 

        print("Rolling die 2...") 

        time.sleep(1) 

        print("You rolled a...") 

        time.sleep(1) 

        roll_2=random.randint(1,6) 

        print(roll_2) 

        if roll_1==roll_2: 

            print("You rolled a DOUBLE! This means you get to roll again! :D") 

            time.sleep(1) 

            print("Rolling...") 

            time.sleep(1) 

            print("You rolled a...") 

            time.sleep(1) 

            roll_3=random.randint(1,6) 

            print(roll_3) 

            time.sleep(1) 

            print("ADDING YOUR ROLLS TOGETHER...") 

            totalp1=roll_3+roll_2+roll_1 

        else: 

            time.sleep(1) 

            print("ADDING YOUR ROLLS TOGETHER...") 

            totalp1=roll_2+roll_1 

        print(totalp1) 

        check= totalp1 % 2 

        if check == 0: 

            scorep1=totalp1+10 

            print("Your score is:") 

            print(scorep1) 

        elif check == 1: 

            scorep1=totalp1-5 

            print("Your score is:") 

            print(scorep1)   

        if scorep1<1: 

            print("your score went under 0! i'm sorry your game is OVER!") 

            game= False
            break

        else: 

            print("Great it's time for player 2!") 

            ready=input("Are you ready? PLAYER 2? Y/N") 

            while ready == "N": 

                time.sleep(2) 

                ready=input("Are you ready now...?") 

                print(" ") 

            print("Great! Let's start!") 

            time.sleep(1) 

            print("Rolling...") 

            time.sleep(1) 

            print("You rolled a...") 

            time.sleep(1) 

            roll_1=random.randint(1,6) 

            print(roll_1)    

            time.sleep(2) 

            print("Rolling die 2...") 

            time.sleep(1) 

            print("You rolled a...") 

            time.sleep(1) 

            roll_2=random.randint(1,6) 

            print(roll_2) 

            if roll_1==roll_2: 

                print("You rolled a DOUBLE! This means you get to roll again! :D") 

                time.sleep(1) 

                print("Rolling...") 

                time.sleep(1) 

                print("You rolled a...") 

                time.sleep(1) 

                roll_3=random.randint(1,6) 

                print(roll_3) 

                time.sleep(1) 

                print("ADDING YOUR ROLLS TOGETHER...") 

                totalp2=roll_3+roll_2+roll_1 

            else: 

                time.sleep(1) 

                print("ADDING YOUR ROLLS TOGETHER...") 

                totalp2=roll_2+roll_1 

            print(totalp2) 

            check= totalp2 % 2 

            if check == 0: 

                scorep2=totalp2+10 

                print("Your score is:") 

                print(scorep2) 

            elif check == 1: 

                scorep2=totalp2-5 

                print("Your score is:") 

                print(scorep2)   

            if scorep2<1: 

                print("your score went under 0! i'm sorry your game is OVER!") 

                game= False

                break

            else: 

                print("It's time to see who won this round") 

                while scorep2 == scorep1: 

                    print("You BOTH have the same score :O!") 

                    time.sleep(1) 

                    print("That means that you guys should roll the dice until one of you gets a diferent score.") 

                    time.sleep(1) 

                    print("ROLLING DICE FOR PLAYER 1") 

                    twicedice1=random.randint(1,6) 

                    time.sleep(1) 

                    print("ROLLING DICE FOR PLAYER 2") 

                    twicedice2=random.randint(1,6) 

                    scorep1=scorep1+twicedice1 

                    scorep2=scorep2+twicedice2 

                time.sleep(1) 

                if scorep1> scorep2: 

                    print("PLAYER 1! You won well done! :D") 

                    print(" your total scores so far are: PLAYER 1:") 

                    time.sleep(1) 

                    print(scorep1) 

                    time.sleep(1) 

                    print("And player 2:") 

                    time.sleep(1) 

                    print(scorep2) 

                elif scorep2> scorep1: 

                    print("PLAYER 2! You won well done! :D") 

                    print(" your total scores so far are: PLAYER 1:") 

                    time.sleep(1) 

                    print(scorep1) 

                    time.sleep(1) 

                    print("And player 2:") 

                    time.sleep(1) 

                    print(scorep2) 

                elif scorep2> scorep1: 

                    time.sleep(1) 

                print(" It's time for the next round! Let's go!") 

        print(" ") 

while totalp2 == totalp1: 

    print("You BOTH have the same total score :O!") 

    time.sleep(1) 

    print("That means that you guys should roll the dice until one of you gets a diferent score. Whoever gets the bigger number will win the whole game!") 

    time.sleep(1) 

    print("ROLLING DICE FOR PLAYER 1") 

    twicedice1=random.randint(1,6) 

    time.sleep(1) 

    print("ROLLING DICE FOR PLAYER 2") 

    twicedice2=random.randint(1,6) 

    totalp1=totalp1+twicedice1 

    totalp2=totalp2+twicedice2 
if totap1>totalp2:
    print("PLAYER 1 HAS WON THE GAME")
elif totalp2>totalp1:
    print("PLAYER 2 HAS WON THE GAME")
print("Would you like to see a spreadhseet of all your score? Y/N ")
see=input()
if see == 'Y':
    time.sleep(1)
    print("CREATING SPREADSHEET...")
    time.sleep(1)
    print("CREATED")
    time.sleep(1)

print("Game over")
import random 

import time

scoretable=open("The scores.txt","w")
User_1="player_1"
table=open("The scores.txt","w")
#table.write(rounds = [["Player, Score, End Total","\N"],
#                      [name1,
               
password1="hat" 

attemptuser=input("Hello! Please enter your username for PLAYER 1 ") 

while attemptuser != User_1: 

    attemptuser=input("Wrong! Try again! ") 

    print(" ") 

print("Correct!") 
name1=input("What is your name: PLAYER 1?")
time.sleep(1)
scoretable.write(name1,"\n")
attemptpass=input("Please enter your Password for PLAYER 1 ") 

while attemptpass != password1: 

    attemptpass=input("Wrong! Try again! ") 

    print(" ") 

print("Correct! Welcome to the game player_1!") 

User_2="player_2" 

password2="potato" 

attemptuser=input("Please enter your username for PLAYER 2 ") 

while attemptuser != User_2: 

    attemptuser=input("Wrong! Try again! ") 

    print(" ") 

print("Correct!")
name2=input("What is your name: PLAYER 2?")
scoretable.write(name2,"\n")
scoretable.close()
scoretable=open("The scores.txt","r")

attemptpass=input("Please enter your Password for PLAYER 2 ") 

while attemptpass != password2: 

    attemptpass=input("Wrong! Try again! ") 

    print(" ") 

print("Correct! Welcome to the game player_2, let's play!!!") 

game= True 

while game== True: 

    for i in range (0,5): 

        ready=input("Are you ready to roll player_1? Y or N! ") 

        while ready == "N": 

            time.sleep(2) 

            ready=input("Are you ready now...?") 

            print(" ") 

        print("Great! Let's start!") 

        time.sleep(1) 

        print("Rolling...") 

        time.sleep(1) 

        print("You rolled a...") 

        time.sleep(1) 

        roll_1=random.randint(1,6) 

        print(roll_1)    

        time.sleep(2) 

        print("Rolling die 2...") 

        time.sleep(1) 

        print("You rolled a...") 

        time.sleep(1) 

        roll_2=random.randint(1,6) 

        print(roll_2) 

        if roll_1==roll_2: 

            print("You rolled a DOUBLE! This means you get to roll again! :D") 

            time.sleep(1) 

            print("Rolling...") 

            time.sleep(1) 

            print("You rolled a...") 

            time.sleep(1) 

            roll_3=random.randint(1,6) 

            print(roll_3) 

            time.sleep(1) 

            print("ADDING YOUR ROLLS TOGETHER...") 

            totalp1=roll_3+roll_2+roll_1 

        else: 

            time.sleep(1) 

            print("ADDING YOUR ROLLS TOGETHER...") 

            totalp1=roll_2+roll_1 

        print(totalp1) 

        check= totalp1 % 2 

        if check == 0: 

            scorep1=totalp1+10 

            print("Your score is:") 

            print(scorep1) 

        elif check == 1: 

            scorep1=totalp1-5 

            print("Your score is:") 

            print(scorep1)   

        if scorep1<1: 

            print("your score went under 0! i'm sorry your game is OVER!") 

            game= False
            break

        else: 

            print("Great it's time for player 2!") 

            ready=input("Are you ready? PLAYER 2? Y/N") 

            while ready == "N": 

                time.sleep(2) 

                ready=input("Are you ready now...?") 

                print(" ") 

            print("Great! Let's start!") 

            time.sleep(1) 

            print("Rolling...") 

            time.sleep(1) 

            print("You rolled a...") 

            time.sleep(1) 

            roll_1=random.randint(1,6) 

            print(roll_1)    

            time.sleep(2) 

            print("Rolling die 2...") 

            time.sleep(1) 

            print("You rolled a...") 

            time.sleep(1) 

            roll_2=random.randint(1,6) 

            print(roll_2) 

            if roll_1==roll_2: 

                print("You rolled a DOUBLE! This means you get to roll again! :D") 

                time.sleep(1) 

                print("Rolling...") 

                time.sleep(1) 

                print("You rolled a...") 

                time.sleep(1) 

                roll_3=random.randint(1,6) 

                print(roll_3) 

                time.sleep(1) 

                print("ADDING YOUR ROLLS TOGETHER...") 

                totalp2=roll_3+roll_2+roll_1 

            else: 

                time.sleep(1) 

                print("ADDING YOUR ROLLS TOGETHER...") 

                totalp2=roll_2+roll_1 

            print(totalp2) 

            check= totalp2 % 2 

            if check == 0: 

                scorep2=totalp2+10 

                print("Your score is:") 

                print(scorep2) 

            elif check == 1: 

                scorep2=totalp2-5 

                print("Your score is:") 

                print(scorep2)   

            if scorep2<1: 

                print("your score went under 0! i'm sorry your game is OVER!") 

                game= False

                break

            else: 

                print("It's time to see who won this round") 

                while scorep2 == scorep1: 

                    print("You BOTH have the same score :O!") 

                    time.sleep(1) 

                    print("That means that you guys should roll the dice until one of you gets a diferent score.") 

                    time.sleep(1) 

                    print("ROLLING DICE FOR PLAYER 1") 

                    twicedice1=random.randint(1,6) 

                    time.sleep(1) 

                    print("ROLLING DICE FOR PLAYER 2") 

                    twicedice2=random.randint(1,6) 

                    scorep1=scorep1+twicedice1 

                    scorep2=scorep2+twicedice2 

                time.sleep(1) 

                if scorep1> scorep2: 

                    print("PLAYER 1! You won well done! :D") 

                    print(" your total scores so far are: PLAYER 1:") 

                    time.sleep(1) 

                    print(scorep1) 

                    time.sleep(1) 

                    print("And player 2:") 

                    time.sleep(1) 

                    print(scorep2) 

                elif scorep2> scorep1: 

                    print("PLAYER 2! You won well done! :D") 

                    print(" your total scores so far are: PLAYER 1:") 

                    time.sleep(1) 

                    print(scorep1) 

                    time.sleep(1) 

                    print("And player 2:") 

                    time.sleep(1) 

                    print(scorep2) 

                elif scorep2> scorep1: 

                    time.sleep(1) 

                print(" It's time for the next round! Let's go!") 

        print(" ") 

while totalp2 == totalp1: 

    print("You BOTH have the same total score :O!") 

    time.sleep(1) 

    print("That means that you guys should roll the dice until one of you gets a diferent score. Whoever gets the bigger number will win the whole game!") 

    time.sleep(1) 

    print("ROLLING DICE FOR PLAYER 1") 

    twicedice1=random.randint(1,6) 

    time.sleep(1) 

    print("ROLLING DICE FOR PLAYER 2") 

    twicedice2=random.randint(1,6) 

    totalp1=totalp1+twicedice1 

    totalp2=totalp2+twicedice2 
if totap1>totalp2:
    print("PLAYER 1 HAS WON THE GAME")
elif totalp2>totalp1:
    print("PLAYER 2 HAS WON THE GAME")
print("Would you like to see a spreadhseet of all your score? Y/N ")
see=input()
if see == 'Y':
    time.sleep(1)
    print("CREATING SPREADSHEET...")
    time.sleep(1)
    print("CREATED")
    time.sleep(1)

print("Game over")
import random 

import time

scoretable=open("The scores.txt","w")
User_1="player_1"
table=open("The scores.txt","w")
#table.write(rounds = [["Player, Score, End Total","\N"],
#                      [name1,
               
password1="hat" 

attemptuser=input("Hello! Please enter your username for PLAYER 1 ") 

while attemptuser != User_1: 

    attemptuser=input("Wrong! Try again! ") 

    print(" ") 

print("Correct!") 
name1=input("What is your name: PLAYER 1?")
time.sleep(1)
scoretable.write(name1,"\n")
attemptpass=input("Please enter your Password for PLAYER 1 ") 

while attemptpass != password1: 

    attemptpass=input("Wrong! Try again! ") 

    print(" ") 

print("Correct! Welcome to the game player_1!") 

User_2="player_2" 

password2="potato" 

attemptuser=input("Please enter your username for PLAYER 2 ") 

while attemptuser != User_2: 

    attemptuser=input("Wrong! Try again! ") 

    print(" ") 

print("Correct!")
name2=input("What is your name: PLAYER 2?")
scoretable.write(name2,"\n")
scoretable.close()
scoretable=open("The scores.txt","r")

attemptpass=input("Please enter your Password for PLAYER 2 ") 

while attemptpass != password2: 

    attemptpass=input("Wrong! Try again! ") 

    print(" ") 

print("Correct! Welcome to the game player_2, let's play!!!") 

game= True 

while game== True: 

    for i in range (0,5): 

        ready=input("Are you ready to roll player_1? Y or N! ") 

        while ready == "N": 

            time.sleep(2) 

            ready=input("Are you ready now...?") 

            print(" ") 

        print("Great! Let's start!") 

        time.sleep(1) 

        print("Rolling...") 

        time.sleep(1) 

        print("You rolled a...") 

        time.sleep(1) 

        roll_1=random.randint(1,6) 

        print(roll_1)    

        time.sleep(2) 

        print("Rolling die 2...") 

        time.sleep(1) 

        print("You rolled a...") 

        time.sleep(1) 

        roll_2=random.randint(1,6) 

        print(roll_2) 

        if roll_1==roll_2: 

            print("You rolled a DOUBLE! This means you get to roll again! :D") 

            time.sleep(1) 

            print("Rolling...") 

            time.sleep(1) 

            print("You rolled a...") 

            time.sleep(1) 

            roll_3=random.randint(1,6) 

            print(roll_3) 

            time.sleep(1) 

            print("ADDING YOUR ROLLS TOGETHER...") 

            totalp1=roll_3+roll_2+roll_1 

        else: 

            time.sleep(1) 

            print("ADDING YOUR ROLLS TOGETHER...") 

            totalp1=roll_2+roll_1 

        print(totalp1) 

        check= totalp1 % 2 

        if check == 0: 

            scorep1=totalp1+10 

            print("Your score is:") 

            print(scorep1) 

        elif check == 1: 

            scorep1=totalp1-5 

            print("Your score is:") 

            print(scorep1)   

        if scorep1<1: 

            print("your score went under 0! i'm sorry your game is OVER!") 

            game= False
            break

        else: 

            print("Great it's time for player 2!") 

            ready=input("Are you ready? PLAYER 2? Y/N") 

            while ready == "N": 

                time.sleep(2) 

                ready=input("Are you ready now...?") 

                print(" ") 

            print("Great! Let's start!") 

            time.sleep(1) 

            print("Rolling...") 

            time.sleep(1) 

            print("You rolled a...") 

            time.sleep(1) 

            roll_1=random.randint(1,6) 

            print(roll_1)    

            time.sleep(2) 

            print("Rolling die 2...") 

            time.sleep(1) 

            print("You rolled a...") 

            time.sleep(1) 

            roll_2=random.randint(1,6) 

            print(roll_2) 

            if roll_1==roll_2: 

                print("You rolled a DOUBLE! This means you get to roll again! :D") 

                time.sleep(1) 

                print("Rolling...") 

                time.sleep(1) 

                print("You rolled a...") 

                time.sleep(1) 

                roll_3=random.randint(1,6) 

                print(roll_3) 

                time.sleep(1) 

                print("ADDING YOUR ROLLS TOGETHER...") 

                totalp2=roll_3+roll_2+roll_1 

            else: 

                time.sleep(1) 

                print("ADDING YOUR ROLLS TOGETHER...") 

                totalp2=roll_2+roll_1 

            print(totalp2) 

            check= totalp2 % 2 

            if check == 0: 

                scorep2=totalp2+10 

                print("Your score is:") 

                print(scorep2) 

            elif check == 1: 

                scorep2=totalp2-5 

                print("Your score is:") 

                print(scorep2)   

            if scorep2<1: 

                print("your score went under 0! i'm sorry your game is OVER!") 

                game= False

                break

            else: 

                print("It's time to see who won this round") 

                while scorep2 == scorep1: 

                    print("You BOTH have the same score :O!") 

                    time.sleep(1) 

                    print("That means that you guys should roll the dice until one of you gets a diferent score.") 

                    time.sleep(1) 

                    print("ROLLING DICE FOR PLAYER 1") 

                    twicedice1=random.randint(1,6) 

                    time.sleep(1) 

                    print("ROLLING DICE FOR PLAYER 2") 

                    twicedice2=random.randint(1,6) 

                    scorep1=scorep1+twicedice1 

                    scorep2=scorep2+twicedice2 

                time.sleep(1) 

                if scorep1> scorep2: 

                    print("PLAYER 1! You won well done! :D") 

                    print(" your total scores so far are: PLAYER 1:") 

                    time.sleep(1) 

                    print(scorep1) 

                    time.sleep(1) 

                    print("And player 2:") 

                    time.sleep(1) 

                    print(scorep2) 

                elif scorep2> scorep1: 

                    print("PLAYER 2! You won well done! :D") 

                    print(" your total scores so far are: PLAYER 1:") 

                    time.sleep(1) 

                    print(scorep1) 

                    time.sleep(1) 

                    print("And player 2:") 

                    time.sleep(1) 

                    print(scorep2) 

                elif scorep2> scorep1: 

                    time.sleep(1) 

                print(" It's time for the next round! Let's go!") 

        print(" ") 

while totalp2 == totalp1: 

    print("You BOTH have the same total score :O!") 

    time.sleep(1) 

    print("That means that you guys should roll the dice until one of you gets a diferent score. Whoever gets the bigger number will win the whole game!") 

    time.sleep(1) 

    print("ROLLING DICE FOR PLAYER 1") 

    twicedice1=random.randint(1,6) 

    time.sleep(1) 

    print("ROLLING DICE FOR PLAYER 2") 

    twicedice2=random.randint(1,6) 

    totalp1=totalp1+twicedice1 

    totalp2=totalp2+twicedice2 
if totap1>totalp2:
    print("PLAYER 1 HAS WON THE GAME")
elif totalp2>totalp1:
    print("PLAYER 2 HAS WON THE GAME")
print("Would you like to see a spreadhseet of all your score? Y/N ")
see=input()
if see == 'Y':
    time.sleep(1)
    print("CREATING SPREADSHEET...")
    time.sleep(1)
    print("CREATED")
    time.sleep(1)

print("Game over")
