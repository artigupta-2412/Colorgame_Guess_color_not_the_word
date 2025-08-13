import tkinter
import random

colours = ['Red', 'Blue', 'Green', 'Pink',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 30
def startGame(event):
    if timeleft == 30:

        countdown()

    nextColour()
def nextColour():

    global score
    global timeleft

    if timeleft > 0:

        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        b1.config(text="Score: " + str(score))
def countdown():
    global timeleft
    if timeleft > 0:

        timeleft -= 1
        timeLabel.config(text="Time left: "
                              + str(timeleft))
        timeLabel.after(1000, countdown)
    end()
def end():
    if  timeleft==0:
        timeLabel.config(text="GAME OVER:(")

root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("400x400")
root.configure(bg="black")
instructions = tkinter.Label(root, text="Type in the colour "
                                        "of the words, and not the word text!",
                             font=('Helvetica', 22),fg="white",bg="black")
instructions.pack()

b1 = tkinter.Button(root, text="Press enter to start",bg="red",fg="white",
                           font=('Helvetica', 12))
b1.pack()

timeLabel = tkinter.Label(root, text="Time left: " +
                                     str(timeleft), font=('Copperplate Gothic bold', 12),fg="white",bg="black")
timeLabel.pack()
label = tkinter.Label(root, font=('Showcard Gothic', 60),fg="white",bg="black")
label.pack()
e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()
root.mainloop()