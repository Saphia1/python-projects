operation = input(("Enter operation: "))
number = int(input(("Enter number: ")))
mylist=[]
number=number+1
if operation == "+":
        for i in range(0,number):
            for y in range (0,number):
                print(operation,"I", (0,(i+y)), flush=True)
elif operation == "*":
        for i in range(0,number):
            for y in range (0,number):
                print(operation,"I", (0,(i*y)), flush = True)
elif operation == "-":
        for i in range(0,number):
            for y in range (0,number):
                print(operation,"I", (0,(i-y)), flush = True)
elif operation == "/":
        for i in range(0,number):
            for y in range (0,number):
                print(operation,"I", (0,(i/y)), flush = True)
 
