import time
import random
print("WELCOME TO CHAT BOT")
print("༼ ͡° ͜ʖ ͡° ༽ my name is SkimbleShanks")
print("How old are you?")
age = input()
print("oh... well I am.... 100 years old... ...")
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('BOO! ༼ ͡° ͜ʖ ͡° ༽')
time.sleep(1)
print('i scared ya didnt i? hehehehe')
time.sleep(2)
print('I know you are', age,'years old, but what is your NAME?')
name = input()
print('Hello',name)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('BOO! ༼ ͡° ͜ʖ ͡° ༽')
time.sleep(1)
print('i scared ya AGAIN didnt i? hehehehe')
time.sleep(1)
print('This is fun IS IT NOT', name,'!?')
fun=input()
while fun != 'yes':
        choice = input("I SAID ARE YOU HAVING FUN", name,"!?")
print("Great >:) Let's play a game!")
time.sleep(2)
print('I will think of a question and you can answer  it... (◕‿◕)')
time.sleep(1)
print("Pineapple on pizza?")
answer=input()
time.sleep(1)
pizza=['mushrooms','ANCHOVIES','olives'] 
if answer == 'yes':
    print("I love to have Pineapples and", random.choice(pizza) ,"ON my PIZZA!")
elif answer == 'no':
    print("BAD TASTE!")
print("What else do you like on YOUR pizza,",name)
time.sleep(2)
toppings=input()
print("I ALSO love love LOVE to have,", toppings,"on my PIZZA!!! WOW we have SOOO much in common, hang on a sec... my phone is ringing... one moment!")
phone=['Lilith','Fiona','Geraldine']
time.sleep(1)
print("It's my aunt,", random.choice(phone) ,"ooh? she wants to talk to you!")
time.sleep(1)
print("Do you want to talk to her? ")
choice=input()
password='yes'
while choice != password:
    choice = input("I SAID ARE YOU GOING TO TALK TO HER", name,"!?")
print("DELIGHTFUL! Here you go! :)")



