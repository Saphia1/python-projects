a=input("Enter a string to reverse")
b=" "
for i in range (1,len(a)):
    b=b + a[-i]
print (b+a[0])
