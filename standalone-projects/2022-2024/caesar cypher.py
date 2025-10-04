import random
def encode(key,message):
    newmessage=("")
    for i in range (0,len(message)):
        for j in range(0,26):
            if abc[j] ==message[i]:
                key2=key+j
                newmessage=newmessage+abc[key2]
    return(newmessage)
def decode(key,nm):
    bewmessage=("")
    for i in range (0,len(nm)):
        for j in range(0,26):
            if abc[j] ==nm[i]:
                key2=j-key
                bewmessage=bewmessage+abc[key2]
    return bewmessage

key = random.randint(1,25)
message=input("What message would you like encoded?")
abc=['a','b','c' ,'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c' ,'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
newmessage=("")
nm=encode(key,message)
print(nm)
dec=input("Wanna decode it?")
if dec == "no":
    print("ok...")
else:
    m=decode(key,nm)
    print(m)

