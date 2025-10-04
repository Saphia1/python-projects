##4578423013769219
##Starting with the first digit, multiply every second digit by 2:
##8-5-14-8-8-2-6-0-2-3-14-6-18-2-2
##Every time you have a two-digit number, just add those digits together for a one-digit result:
##8-5-5-8-8-2-6-0-2-3-5-6-9-2-2
##Finally, add all the numbers together:
##8 + 5 + 5 + 8 + 8 + 2 + 6 + 0 + 2 + 3 + 5 + 6 + 9 + 2 + 2 = 71
##When this number is added to the check digit, then the result must be an even multiple of 10. In this case:
##71 + 9 = 80
##The number is therefore valid. If the algorithm doesn't produce a multiple of 10, then the card number cannot be valid.
#pin=input("ENTER CREDIT CARD NUMBER ")
cardnumb=[]
for i in range (0,16):
    cardnumb.append((input("Enter card number: ")))
    cardnumb.append("-")
print(cardnumb)
for i in range (0,len(cardnumb),4):
    cardnumb[i]= int(cardnumb[i])*2
    new=cardnumb[i]*2
    new=str(new)
    if len(new)== 2:
        one = int(new[0])
        two = int(new[1])
        cardnumb[i] = one + two
       # new=int(new)
        #one=(new(2))
 
       # two=(new(1))

       # cardnumb[i]=one+two
print (cardnumb)

#for i in range (0,16):
