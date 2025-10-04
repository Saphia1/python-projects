#binary search
numbers=[1,2,3,4,5,6,7,8]
target=int(input("what number you want to find"))
while len(numbers)>1 and found !=True:
    mid = numbers//2
    l=[:mid]
    r=[mid:]
    if mid> target:
        numbers=l
    elif mid< target:
        numbers=r
    elif mid== target:
        print("Found")
