#functions
def usd (a):
    dollars=a

#main code
currency=input("What currency are you going to input? USD, GBP, AUD, EUR, CHF")
amount= int(input("Please enter the amount:"))
conv=input("What would u like to convert it to? USD, GDP, AUD, EUR, CHF")

if currency == "USD" and conv== "GDP":
    print(amount * 0.65)
elif currency == "GDP" and conv== "USD":
    print(amount/0.65)            
elif currency == "USD" and conv== "AUD":
    print(amount* 1.363782)
elif currency == "AUD" and conv== "USD":
    print(amount/ 1.363782)
elif currency == "USD" and conv== "EUR":
    print(amount* 0.87388312)
elif currency == "EUR" and conv== "USD":
    print(amount/ 0.87388312)
elif currency == "USD" and conv== "CHF":
    print(amount* 0.92117209)
elif currency == "CHF" and conv== "USD":
    print(amount/ 0.92117209)   
elif currency == "GDP" and conv== "AUR":
    print(amount*1.8302081)
elif currency == "AUR" and conv== "GDP":
    print(amount/1.8302081)
elif currency == "GDP" and conv== "EUR":
    print(amount*1.1725089 )
elif currency == "EUR" and conv== "GDP":
    print(amount/1.1725089 )
elif currency == "GDP" and conv== "CHF":
    print(amount*1.2359576 )
elif currency == "CHF" and conv== "GDP":
    print(amount/1.2359576 )
elif currency == "AUD" and conv== "EUR":
    print(amount*0.64080 )
elif currency == "EUR" and conv== "AUD":
    print(amount/0.64080 )
elif currency == "AUD" and conv== "CHF":
    print(amount*0.67557 )
elif currency == "CHF" and conv== "AUD":
    print(amount/0.67557 )
elif currency == "EUR" and conv== "CHF":
    print(amount*1.05425 )
elif currency == "EUR" and conv== "CHF":
    print(amount/1.05425 )
