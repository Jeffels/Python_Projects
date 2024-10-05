#Paper   > Rock
#Rock    > Scissor
#Scissor > Paper

import random
import sys
from tkinter import *
from tkinter import ttk

#The game is in the function
def RockPaperScissors():
    print("Let's Play Rock, Paper, Scissors!\nThe rules are as follows:\nRock beats Scissors\nPaper beats Rock\nScissors beats Paper\nWhen you want to leave type exit")
    #Initialising some variables used in the loop
    i = True
    computer = ""
    compScore = 0
    userScore = 0

    #Main loop of game
    #while(i == True):
    #Get the user input first
    userText = user.get()

    #1 will be rock. 2 will be paper. 3 will be scissors
    #Generates Computer Answer
    computerNum = random.randint(1,3)
    if computerNum == 1:
        computer == "Rock"
    elif computerNum == 2:
        computer = "Paper"
    else:
        computer = "Scissors"

    print("Computer: "+ computer)

    #Decides the winner based on rules
    if userText == "exit":
        #close the game     ###THIS DOESN'T CURRENTLY WORK###
        sys.exit
    elif userText == "rock" or userText == "Rock":  #user vs comp
        if computerNum == 1:                #rock vs rock
            print("Draw")
        elif computerNum == 2:              #rock vs paper
            print("You Lose")
            compScore=compScore+1
        else:                               #rock vs scissor
            print("You Win")
            userScore=userScore+1
    elif userText == "paper" or userText == "Paper":#user vs comp
        if computerNum == 1:                #Paper vs rock
            print("You Win")
            userScore=userScore+1
        elif computerNum == 2:              #Paper vs paper
            print("Draw")
        else:                               #Paper vs scissor
            print("You Lose")
            compScore=compScore+1
    elif userText == "scissors" or userText == "Scissors" or userText == "scissor" or userText == "Scissor":  
        if computerNum == 1:                #Scissor vs rock
            print("You Lose")
            compScore=compScore+1
        elif computerNum == 2:              #Scissor vs paper
            print("You Win")
            userScore=userScore+1
        else:                               #Scissor vs scissor
            print("Draw")
    #Anything other than the expected word answers
    else:   
        print(f"Error Input was not expected. You put {userText} Please try again")
    #Prints the score for the user to see the score
    print(f"Current Score:\nUser:{userScore}   Computer:{compScore}")
    ##add a return statment here of who won

#basic GUI initialisation
root = Tk()
root.title("Rock Paper Scissors")


mainframe = ttk.Frame(root, padding="6 6 24 24", relief=RIDGE)
mainframe.grid(column=3, row=6, sticky=(N, W, E, S))


label_lp = ttk.Label(mainframe, text="Let's play!!")
label_lp.grid(column=1,row=1,columnspan=3)

label_rps = ttk.Label(mainframe, text="Rock, Paper Scissors?")
label_rps.grid(column=1,row=2,columnspan=3)

#will manually tally score this side of the funtion

label_score = ttk.Label(mainframe, text="Score:")
label_score.grid(column=1,row=3,columnspan=3)

user = StringVar()
user_entry = ttk.Entry(mainframe, width=15, textvariable=user, justify=CENTER)
user_entry.grid(column=2, row=4)

play = ttk.Button(mainframe, text="Play", command=RockPaperScissors())
play.grid(column=3,row=4)

label_comp = ttk.Label(mainframe, text="Computer Picked: ")
label_comp.grid(column=1,row=5,columnspan=3)

label_wl = ttk.Label(mainframe, text="WIN/LOSE/DRAW")
label_wl.grid(column=1,row=6,columnspan=3)

root.mainloop()

