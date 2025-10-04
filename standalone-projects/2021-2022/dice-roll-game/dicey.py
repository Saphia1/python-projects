#import modules
import random
import time



#Setup User 1:
Username_1 = "PLAYER_1"
Password_1 = "hat"

#Setup User 2:
Username_2 = "PLAYER_2"
Password_2 = "potato"

#Login User 1:

UserAttempt = input("Hello! Please enter your username for PLAYER 1 ") # ask for username

while UserAttempt != Username_1: # Loop to get correct input
    UserAttempt = input("Wrong ! Try again! ")
    print(" ")

print("Correct!")


time.sleep(1)

PassAttempt = input("Please enter your Password for PLAYER 1 ")

while PassAttempt != Password_1:
    PassAttempt = input("Wrong! Try again! ")
    print(" ")


print("Correct! Welcome to the game PLAYER 1")

time.sleep(1)

#Login User 2

UserAttempt = input("Please enter the username for PLAYER 2 ")
while UserAttempt != Username_2:
    UserAttempt = input("Wrong ! Try again! ")
    print(" ")

PassAttempt = input("Please enter your Password for PLAYER 2 ")

while PassAttempt != Password_2:
    PassAttempt = input("Wrong! Try again! ")
    print(" ")


print("Correct! Welcome to the game PLAYER 2")

time.sleep(1)

print("It's time to start the game!")
time.sleep(1)
ready=input("Are you ready? Y or N! ") 

while ready == "N":
    time.sleep(2) 

    ready=input("Are you ready now...?") 

    print(" ") 

print("Great! Let's start!") 

time.sleep(1)




#initialise scores

p1_scores = [] #Create lists to hold total values of both rolls 
p1_total = 0
p2_scores = []
p2_total= 0


for i in range(0,5):
    roll_1 = random.randint(1,6) # Roll twice
    roll_2 = random.randint(1,6)
    print("Player 1 rolled: ", roll_1)
    time.sleep(1)
    print("Player 1 rolled: ", roll_2)

    total = roll_1 + roll_2 # Get the total
    time.sleep(1)

    print("Player 1 total of two die: ", total)

    if roll_1 == roll_2:
        total = roll_1 + roll_2 + random.randint(0,6) # add third dice to total if roll same number

    if total % 2 == 0: # If score is even, +5. If score is odd, +10
        total = total + 10
    elif total % 2 == 1:
        total = total - 5

    p1_scores.append(total) # Add total value to list
    p1_total = p1_total + total
    time.sleep(1)

    print("Player 1 total score: ", p1_total)
    time.sleep(1)
    print("Time for Player 2")
    time.sleep(2)
        
    roll_1 = random.randint(1,6) #Repeat for second player
    print("Player 2 rolled: ", roll_1)
    time.sleep(1)
    roll_2 = random.randint(1,6)
    print("Player 2 rolled: ", roll_2)
    time.sleep(1)

    total = roll_1 + roll_2
    print("Player 2 total of two die: ", total)
    time.sleep(1)

    if roll_1 == roll_2:
        total = roll_1 + roll_2 + random.randint(0,6)

    if total % 2 == 0:
        total = total + 10
    elif total %2 == 1:
        total = total - 5

    p2_scores.append(total)
    p2_total = p2_total + total
    print("Player 2 total score: ", p2_total)
    time.sleep(1)
    if p1_total <= 0:
        skip = True
        print("Player 1, I am sorry but your score is 0 or under meaning the game is OVER!")
        break
    elif p2_total <=0:
        skip = True
        print("Player 2, I am sorry but your score is 0 or under meaning the game is OVER!")
        break
    print("The totals so far are: ")
    time.sleep(1)
    print("Player 1: ", p1_total)
    time.sleep(1)
    print("Player 2: ", p2_total)
    time.sleep(1)


while p1_total == p2_total:#Keep adding dice rolls to break tie. sum(scores) gives you overall score
    print("Your scores are equal so let's roll a dice until one of you gets a bigger number!")
    if skip == True:
        break
    rollP1 = random.randint(1,6)
    p1_scores.append(rollP1)
    p1_total += rollP1

    rollP2 = random.randint(1,6)
    p2_scores.append(rollP2)
    p2_total += rollP2



print("Scores Player 1", p1_scores) #print total scores from each round for each player
print("Scores Player 2", p2_scores)
if p1_total > p2_total: # print out winner
    winner = "Player 1"
    winner_score= p1_total
else:
    winner = "Player 2"
    winner_score=p2_total

print("Winner is ", winner, "with a total score of: " ,str(winner_score), "pts")

make_file = input("Write to file? Y/N")

if make_file == 'Y': #Write all info to file
    scorecard = open('scorecard.txt', 'w') # open file
    scorecard.write('Scores: ') # command to write to file
    scorecard.write('\n') #line break
    scorecard.write('Player 1: ')
    scorecard.write(str(p1_scores)) # all numbers must be converted to strings using str() before being written
    scorecard.write('\t')
    scorecard.write('Player 1 Total: ')
    scorecard.write(str(p1_total))
    scorecard.write('\n')
    scorecard.write('Player 2: ')
    scorecard.write(str(p2_scores))
    scorecard.write('\t')
    scorecard.write('Player 2 Total: ')
    scorecard.write(str(p2_total))
    scorecard.close()
