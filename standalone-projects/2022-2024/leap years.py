#functions
#maincode
year=int(input("Enter the year: "))
###functions#
def is_leap (year):
    leap=False
    b=a%4
    if b>0:
        return leap
    elif b==0:
        c=a%100
        if c==0:
            d=a%400
            if d>0:
                return leap
            else:
                leap=True
                return leap
        elif c!=0:
            leap=True
            return leap

#a=(int(input("Enter the year: ")))
a=year
answer=is_leap(a)
print(answer)
