digits=int(input("Enter the number of digits in your number "))
number=("Enter number")
number[1]= 
#number=[number[0]**2] + [number[1]*number[1]]
numbers=0
while numbers != (1):
    for i in range (0,digits):
        number=int(input("enter digit"))
        numbers=numbers+(number*number)
        
    
    numbers=str(numbers)
    digits=len(numbers)
    numbers=int(numbers)
    print(numbers)
