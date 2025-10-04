#imports
import time
import random
#functions
def times (a,b):
    c=a * b
    return c
def divide (a,b):
    c=a / b
    return c
def subtract (a,b):
    c=a - b
    return c
    
def addition (a,b):
    c=a + b
    return c

    
#operating systems menu
choice = input("Welcome to the operating system! What would you like to access? Calculator or Doctor Appointment")
if choice == "Calculator":
    calculator= input("A. Addition, B. Subtraction, C. Multiplication or D. Division?")
    if calculator == "Addition" or calculator == "A":
        num1=int(input("Enter first number"))
        num2=int(input("Enter second number"))
        print(addition(num1,num2))
    elif calculator == "Subtraction" or calculator == "B":
        num1=int(input("Enter first number"))
        num2=int(input("Enter second number"))
        print(subtract(num1,num2))
    elif calculator == "Multiplication" or calculator == "C":
        num1=int(input("Enter first number"))
        num2=int(input("Enter second number"))
        print(times(num1,num2))
    elif calculator == "Division" or calculator == "D":
        num1=int(input("Enter first number"))
        num2=int(input("Enter second number"))
        print(divide(num1,num2))
elif choice == "Doctor Appointment":
    surname=input("Hello, can I take your surname please?")
    firstname=input("And your firstname please?")
    fullname = firstname + " "+ surname
    print("Your name is"," ",fullname)
    time.sleep(1)
    print("...Writing down...")
    time.sleep(1)
    print("My name is Dr Saphia, the most qualified doctor in the world! Let me take your temperature.")
    time.sleep(3)
    print("Taking temp")
    time.sleep(1)
    temp=random.randint(0,78)
    time.sleep(1)
    if temp >37:
            print("YOUR TEMPERATURE IS ABNORMALY HIGH! ", temp," DEGREES!")
    elif temp <35:
        print("YOUR TEMPERATURE IS ABNORMALY LOW!", temp, " DEGREES!")
    else:
        print("Hmmm your temperature is normal...")
    time.sleep(1)
    print("Checking your reflexes..")
    time.sleep(1)
    reflex = random.randint(0,1)
    if reflex == 0:
        print("Your reflexes dont work! Hmmm one last test to determine!")
    elif reflex ==1:
        print("Hmmm your reflexes seem normal...")
    history=random.randint(0,1)
    history=0
    time.sleep(1)
    print("Let me scan your legs")
    time.sleep(1)
    if history == 0:
        print("Your legs are unhealthy")
    else:
        print("hmmm... your legs are fine...")
    if temp>37 and reflex == 0 and history == 0:
        print("You have a deadly disease called itisis (made up by kouther)")
        variable = open ("myhealthfile.txt","w")
        temp=str(temp)
        variable.write(temp)
        variable.close()
        variable = open("myhealthfile","a")
        variable.write("reflexes not working")
        variable.write("unhealthy legs")
        variable.write(fullname)
        variable.close()
        print("I have recorded your data on a file which you are now free to access.")
    elif temp>37 and reflex == 0 and history ==1:
        print("You have a deadly disease called hypernomia (made up by diya)")
        variable = open ("myhealthfile.txt","w")
        temp=str(temp)
        variable.write(temp)
        variable.close()
        variable = open("myhealthfile","a")
        variable.write("reflexes not working")
        variable.write("healthy legs")
        variable.write(fullname)
        variable.close()
        print("I have recorded your data on a file which you are now free to access.")
        print("I have recorded your data on a file which you are now free to access.")
    elif temp>37 and reflex == 1 and history == 0:
        print("You have a deadly disease called curly (made up by riya)")
        variable = open ("myhealthfile.txt","w")
        temp=str(temp)
        variable.write(temp)
        variable.close()
        variable = open("myhealthfile","a")
        variable.write("reflexes working")
        variable.write("unhealthy legs")
        variable.write(fullname)
        variable.close()
        print("I have recorded your data on a file which you are now free to access.")
    elif temp<35 and reflex == 1 and history == 0:
        print("You have a deadly disease called curly (made up by riya)")
        variable = open ("myhealthfile.txt","w")
        temp=str(temp)
        variable.write(temp)
        variable.close()
        variable = open("myhealthfile","a")
        variable.write("reflexes working")
        variable.write("unhealthy legs")
        variable.write(fullname)
        variable.close()
        print("I have recorded your data on a file which you are now free to access.")
    elif temp<35 and reflex == 0 and history == 1:
        print("You have a deadly disease called hypernomia (made up by diya)")
        variable = open ("myhealthfile.txt","w")
        temp=str(temp)
        variable.write(temp)
        variable.close()
        variable = open("myhealthfile","a")
        variable.write("reflexes not working")
        variable.write("healthy legs")
        variable.write(fullname)
        variable.close()
        print("I have recorded your data on a file which you are now free to access.")
    elif temp<35 and reflex == 0 and history == 0:
        print("You have a deadly disease called itisis (made up by kouther)")
        variable = open ("myhealthfile.txt","w")
        temp=str(temp)
        variable.write(temp)
        variable.close()
        variable = open("myhealthfile","a")
        variable.write("reflexes working")
        variable.write("healthy legs")
        variable.write(fullname)
        variable.close()
        print("I have recorded your data on a file which you are now free to access.")
    else:
        print("Eh... you will be okay don't worry")
    
        
