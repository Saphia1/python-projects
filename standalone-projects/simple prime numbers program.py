limit=int(input("Enter your number!"))
j=0
x=0
count=0
for i in range (1, limit):
    for j in range (2,i):
        if i%j ==0:
            break
    else:
        print(i)

##    j=i-1
##    j=j%6
##    x=i+1
##    x=x%6
##    if j == 0 and x== 0:
##        print(i)
    

