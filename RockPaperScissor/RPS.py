#Paper   > Rock
#Rock    > Scissor
#Scissor > Paper

import random
import sys

print("Let's Play Rock, Paper, Scissors!\nThe rules are as follows:\nRock beats Scissors\nPaper beats Rock\nScissors beats Paper\nWhen you want to leave type exit")
i = True
computer = ""
compScore = 0
userScore = 0
while(i == True):
    user = input("3. 2. 1.\nUser:")
    #1 will be rock. 2 will be paper. 3 will be scissors
    computerNum = random.randint(1,3)
    if computerNum == 1:
        computer == "Rock"
    elif computerNum == 2:
        computer = "Paper"
    else:
        computer = "Scissors"

    print("Computer: "+ computer)

    if user == "exit":
        #close the game
        sys.exit
    elif user == "rock" or user == "Rock":  #user vs comp
        if computerNum == 1:                #rock vs rock
            print("Draw")
        elif computerNum == 2:              #rock vs paper
            print("You Lose")
            compScore=compScore+1
        else:                               #rock vs scissor
            print("You Win")
            userScore=userScore+1
    elif user == "paper" or user == "Paper":#user vs comp
        if computerNum == 1:                #Paper vs rock
            print("You Win")
            userScore=userScore+1
        elif computerNum == 2:              #Paper vs paper
            print("Draw")
        else:                               #Paper vs scissor
            print("You Lose")
            compScore=compScore+1
    elif user == "scissors" or user == "Scissors" or user == "scissor" or user == "Scissor":  
        if computerNum == 1:                #Scissor vs rock
            print("You Lose")
            compScore=compScore+1
        elif computerNum == 2:              #Scissor vs paper
            print("You Win")
            userScore=userScore+1
        else:                               #Scissor vs scissor
            print("Draw")
    else:
        print("Error Input was not expected. Please try again")
    print(f"Current Score:\nUser:{userScore}   Computer:{compScore}")
    




