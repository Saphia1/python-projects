name=input("entername")
length=len(name)
new=""
for i in range (length):
    if (name[i]).isupper():
        new+=(name[i]).lower()
    elif (name[i]).islower():
        new += (name[i]).upper()
    else:
        new+=(name[i])
    
print (new)
