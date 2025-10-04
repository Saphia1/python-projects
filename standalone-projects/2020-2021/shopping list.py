items=[""]
print("SHOPPING LIST:")
for i in range (0,10):
    choice=input("Add an item: ")
    if choice == items[i]:
            print("Duplicate Item!")
    else:
        items.append(choice)

print("LIST:")
for i in range (0,len(items)):
    print(items[i])
for i in range (0,10):
    remove=input("What item have you bought? ")
    items.remove(remove)
print("Great! You finished shopping! Have a nice day! :D")

