food=[ [ ["fruits","berries"],["apple","pear","banana"],["healthy"] ],
       [ ["veg","seeds"],["carrot","cucumber","courgette"],["healthy"] ],
       [ ["sweets","treats"],["cookie","donut","cake"],["unhealthy"] ],
    ]
#print off all healthy food
for i in range (0, len(food)):
            if (food[i][2][0])== "healthy":
                print (food[i][0])
                print (food[i][1])

