food=[ [ ["fruits","berries"],["apple","pear","banana"],["healthy"] ],
       [ ["veg","seeds"],["carrot","cucumber","courgette"],["healthy"] ],
       [ ["sweets","treats"],["cookie","donut","cake"],["unhealthy"] ],
    ]
#print off all healthy food
check=True
for i in range (0, len(food)):
    for j in range (0, len(food)):
        print("made it")
        if check==True:
            print("hello")
            print (food[i][j-1])
