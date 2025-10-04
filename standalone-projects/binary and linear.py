def binary(numbers, choice):
    found = False
    index = False
    first = 0
    last = len(numbers)-1
    while first <=last and found == False:
        midpoint=int((first + last)//2)
        if numbers[midpoint] == choice:
            found = True
        elif numbers[midpoint]< choice:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return found


def linear (numbers,choice):
    found = False
    index = 0
    while not found and index!=len(numbers):
        if numbers[index]== choice:
            found=True
        else:
            index +=1#basically made ur own for loop,increments i, in this case index, by 1.
    return found
################## !!! MAIN CODE !!! #########################################
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #created list
choice=int(input("WHAT NUMBER DO U WANT TO SEARCH FOR?")) #asking for the number that they want to find
search= input("Which search would you like to use?")
if search == "binary":
    present=binary(numbers,choice)
    print(present)
else:
    present=linear(numbers,choice)
    print(present)
