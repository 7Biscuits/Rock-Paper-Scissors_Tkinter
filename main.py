import tkinter
from tkinter import *
import random

root = tkinter.Tk()

computer_move = {
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}

def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text = "Player              ")
    l3.config(text = "Computer")
    l4.config(text = "")

def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

def isRock():
    computer_mv = computer_move[str(random.randint(0, 2))]
    if computer_mv == "Rock":
        match_result = "Its a tie!"

    elif computer_mv == "Scissor":
        match_result = "Player Won!"

    else:
        match_result = "Computer Won"

    l4.config(text = match_result)
    l1.config(text = "Rock            ")
    l3.config(text = computer_mv)
    button_disable()

def isPaper():
    computer_mv = computer_move[str(random.randint(0, 2))]
    if computer_mv == "Paper":
        match_result = "Its a tie!"

    elif computer_mv == "Rock":
        match_result = "Player Won!"

    else:
        match_result = "Computer Won"

    l4.config(text = match_result)
    l1.config(text = "Paper           ")
    l3.config(text = computer_mv)
    button_disable()

def isScissor():
    computer_mv = computer_move[str(random.randint(0, 2))]
    if computer_mv == "Scissor":
        match_result = "Its a tie!"

    elif computer_mv == "Paper":
        match_result = "Player Won!"

    else:
        match_result = "Computer Won"

    l4.config(text = match_result)
    l1.config(text = "Rock            ")
    l3.config(text = computer_mv)
    button_disable()

Label(root,
    text = "Rock Paper Scissor",
    font = "normal 20 bold",
    fg = "blue").pack(pady = 20)

frame = Frame(root)
frame.pack()

l1 = Label(frame, text = "Player              ", font = 10)
l2 = Label(frame, text = "VS             ",font = "normal 10 bold")
l3 = Label(frame, text = "Computer", font = 10)
  
l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()

l4 = Label(root,
           text = "",
           font = "normal 20 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")

l4.pack(pady = 20)

frame1 = Frame(root)
frame1.pack()
  
b1 = Button(frame1, text = "Rock",
            font = 10, width = 7,
            command = isRock)
  
b2 = Button(frame1, text = "Paper ",
            font = 10, width = 7,
            command = isPaper)
  
b3 = Button(frame1, text = "Scissor",
            font = 10, width = 7,
            command = isScissor)

b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(padx = 10)

Button(root, text = "Reset Game",
       font = 10, fg = "red",
       bg = "black", command = reset_game).pack(pady = 20)

root.title("Rock-Paper-Scissors")
root.mainloop()