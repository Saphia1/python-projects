#imports#
import random
from threading import Timer
import time
#sub programs#
def check(number):
    if number % 3==0 and number % 5 !=0:
        return('Fizz')
    elif number % 5== 0 and number % 3 !=0:
        return('Buzz')
    elif number % 3== 0 and number % 5== 0:
        return('Fizzbuzz')
    else:
        return(str(number))
def compcheck (number):
    if number % 3==0 and number % 5 !=0:
        return('Fizz')
    elif number % 5== 0 and number % 3 !=0:
        return('Buzz')
    elif number % 3== 0 and number % 5== 0:
        return('Fizzbuzz')
    else:
        return(str(number))
def exit():
    print("Times UP!!!!!!!!!!")

#main code#
print("Hi there!")
time.sleep(1)
print("My name is Fizzle Buzz and I am the champion of Fizzbuzz! ( ͡° ͜ʖ ͡°)")
time.sleep(2)
poppy= input("Do you think you can beat me? HAHAHAHAHAH ( ͡° ͜ʖ ͡°)")
if poppy == "yes":
    print("You wish! No can beat me, fizzlebuzz, ( ͡° ͜ʖ ͡°)")
    time.sleep(1)
    print("LET THE GAMES BEGIN")
    t=Timer(5,exit)
    t.start()
    numb=(input("You enter: "))
    t.cancel()


    for i in range (1,101,2):
        answer=(check(i))
        wrong=random.randint(0,100)
        if answer== numb:
            if i<10:
                t=Timer(10,exit)
            elif i>=10 and i<=15:
                t=Timer(8,exit)
            elif i>=15 and i<=30:
                t=Timer(5,exit)
            elif i>30:
                t=Timer(3,exit)
            else:
                print("GO AWAY")
            
            if wrong<3:
                print("Fizzle Buzz is thinking hard... ")
                time.sleep(1)
                print("( ͡° .ʖ ͡°) ")
                time.sleep(1)
                print("( ͡° ..ʖ ͡°) ")
                time.sleep(1)
                print("( ͡° ͜ʖ ͡°) ")
                time.sleep(1)
                print("The Fizzle Buzz Prints:",wrong)
                print("YOU WIN! BUT NOT FOR LONG! I FIZZLE BUZZ MAY HAVE GONE EASY ON YOU THIS TIME! HAHAHAHA( ͡° ͜ʖ ͡°)")
                break
            elif wrong>3:
                print("Fizzle Buzz is thinking hard... ")
                time.sleep(1)
                print("( ͡° .ʖ ͡°) ")
                time.sleep(1)
                print("( ͡° ..ʖ ͡°) ")
                time.sleep(1)
                print("( ͡° ͜ʖ ͡°) ")
                time.sleep(1)
                print("The Fizzle Buzz Prints:", compcheck(i+1))
                t.start()
                numb=(input("You enter: "))
                t.cancel()
        else:
            print("GAME OVER")
            break

else:
    print("HAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAHAH THATS WHAT I THOUGHT! ( ͡° ͜ʖ ͡°)")
