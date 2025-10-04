gate=input(("Hi, would you like to use an and, an or or an xor gate?"))
if gate == "and":
    input1=input(("You have selected an and gate. Please enter your first input: "))
    input2=input(("Please enter your second input: "))
    if input1 == "1" and input2 == "1":
        print("1")
    else:
        print("0")
        
elif gate == "or":
    input1=input(("You have selected an or gate. Please enter your first input: "))
    input2=input(("Please enter your second input: "))
    if input1 == "0" and input2 == "0":
        print("0")
    else:
        print("1")    

elif gate == "xor":
    input1=input(("You have selected an xor gate. Please enter your first input: "))
    input2=input(("Please enter your second input: "))
    if input1== "0" and input2 == "1" or input1== "1" and input2 == "0":
        print("1")
    else:
        print("0")    
