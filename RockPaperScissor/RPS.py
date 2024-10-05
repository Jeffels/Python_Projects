#Paper   > Rock
#Rock    > Scissor
#Scissor > Paper

import random
import sys
from tkinter import *
from tkinter import ttk

computer = ""
compScore = 0
userScore = 0

#The game is in the function
def RockPaperScissors():
    #Initialising some variables
    global computer, userScore, compScore 

    #Main loop of game
    #Get the user input first
    userText = user.get()

    #1 will be rock. 2 will be paper. 3 will be scissors
    #Generates Computer Answer
    computerNum = random.randint(1,3)
    if computerNum == 1:
        computer = "Rock"
    elif computerNum == 2:
        computer = "Paper"
    else:
        computer = "Scissors"

    #Decides the winner based on rules
    if userText == "exit":
        #close the game     ###THIS DOESN'T CURRENTLY WORK###
        sys.exit()
    elif userText.lower() == "rock":        #user vs comp
        if computerNum == 1:                #rock vs rock
            label_wl.config(text="It was a draw!")
        elif computerNum == 2:              #rock vs paper
            label_wl.config(text="Computer Won!")
            compScore=compScore+1
        else:                               #rock vs scissor
            label_wl.config(text="You Won!")
            userScore=userScore+1
    elif userText.lower() == "paper":       #user vs comp
        if computerNum == 1:                #Paper vs rock
            label_wl.config(text="You Won!")
            userScore=userScore+1
        elif computerNum == 2:              #Paper vs paper
            label_wl.config(text="It was a draw!")
        else:                               #Paper vs scissor
            label_wl.config(text="Computer Won!")
            compScore=compScore+1
    elif userText.lower() == "scissors"or userText.lower() == "scissor":  
        if computerNum == 1:                #Scissor vs rock
            label_wl.config(text="Computer Won!")
            compScore=compScore+1
        elif computerNum == 2:              #Scissor vs paper
            label_wl.config(text="You Won!")
            userScore=userScore+1
        else:                               #Scissor vs scissor
            label_wl.config(text="It was a draw!")
    #Anything other than the expected word answers
    else:   
        label_wl.config(text=f"Error Input was not expected. You put '{userText}'\nPlease try again")
    #Prints the score for the user to see the score
    score_text = f"User:{userScore}   Computer: {compScore}"
    label_score.config(text=score_text)
    #updates the computers choise
    comp_text = "Computer picked "+computer
    label_comp.config(text=comp_text)



#basic GUI initialisation
root = Tk()
root.title("Rock Paper Scissors")

#main frame set up
mainframe = ttk.Frame(root, relief=RIDGE)
mainframe.grid(column=3, row=6, sticky=N+S+E+W)

#general label
label_lp = ttk.Label(mainframe, text="Let's play!!")
label_lp.grid(column=1,row=1,columnspan=3)

#general rps statement
label_rps = ttk.Label(mainframe, text="Rock, Paper, Scissors?")
label_rps.grid(column=1,row=2,columnspan=3)

#will manually tally score this side of the funtion
score_text = f"User:{userScore}   Computer: {compScore}"
label_score = ttk.Label(mainframe, text=score_text)
label_score.grid(column=1,row=3,columnspan=3)

#user entry box
user = StringVar()
user_entry = ttk.Entry(mainframe, width=15, textvariable=user, justify=CENTER)
user_entry.grid(column=2, row=4)

#confirm play button
play = ttk.Button(mainframe, text="Play", command=RockPaperScissors)
play.grid(column=3,row=4)

#computer pick displayed
label_comp = ttk.Label(mainframe, text="")
label_comp.grid(column=1,row=5,columnspan=3)

#display if user won/lost or if it was a draw
label_wl = ttk.Label(mainframe, text="WIN/LOSE/DRAW")
label_wl.grid(column=1,row=6,columnspan=3)

root.mainloop()

