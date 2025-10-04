import random
import time
print("password please")
choice=input()
password='hehe'

while choice!= password:
    print("enter again")
    choice=input("incorrect re-enter")
print("entry gained")
lvl1= False
lvl2= False
game= True
level2=int(1)
print("Menu screen loading...")
time.sleep(1)
print('...LOADED...')
time.sleep(1)
while game == True:
    print("Welcome to the menu screen, we have three choices of difficulty for you...")
    print("Difficulty 1- from 1 to 10")
    print("Difficulty 2 - from 1 - 100")
    print("Difficulty 3 - from 1 to 1000")
    dif=int(input())
    if dif == 1 and game == True:
        attempts= 1
        mynumber=random.randint(1,10)
        usernumber=int(input("I am thinking of a number from 1 to 10...what is it?"))

        while usernumber != mynumber:
            attempts= attempts +1
            if usernumber<mynumber:
                usernumber=int(input("Wrong, my number is bigger"))
            else:
                usernumber=int(input("Wrong, my number is smaller!"))
        print("correct, you took", attempts,"tries to get my number")
        if attempts <=5:
            lvl1= True
            print("You had a great score :)")
        elif attempts >5 and attempts <10:
            print("You got an  alright score, you can do better, I believe in you!")
            lvl1= True
        else:
            print("What a bad score tut tut")
    
            
    if dif == 2 and game== True and lvl1== True:
        attempts= 1
        mynumber=random.randint(1,100)
        usernumber=int(input("I am thinking of a number from 1 to 100...what is it?"))

        while usernumber != mynumber:
            attempts=(attempts +1)
            if usernumber<mynumber:
                usernumber=int(input("Wrong, my number is bigger"))
            else:
                usernumber=int(input("Wrong, my number is smaller!"))
        print("correct, you took", attempts,"tries to get my number")
        if attempts <=5:
            print("You had a great score :)")
            lvl12= True
        elif attempts >5 and attempts <10:
            lvl2= True
            print("You got an  alright score, you can do better, I believe in you!")
        else:
            print("What a bad score tut tut")
                
    if dif == 3 and game== True and lvl2== True:
        attempts=1
        mynumber=random.randint(1,1000)
        usernumber=int(input("I am thinking of a number from 1 to 1000...what is it?"))

        while usernumber != mynumber:
            attempts=(attempts +1)
            if usernumber<mynumber:
                usernumber=int(input("Wrong, my number is bigger"))
            else:
                usernumber=int(input("Wrong, my number is smaller!"))
        print("correct, you took", attempts,"tries to get my number")
        if attempts <=5:
            print("You had a great score :)")
        elif attempts >5 and attempts <10:
            print("You got an  alright score, you can do better, I believe in you!")
        else:
            print("What a bad score tut tut")
                               
                

                
                
         
