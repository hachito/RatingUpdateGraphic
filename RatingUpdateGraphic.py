import tkinter as tk
import winsound
from webread import getInfo

#creates window and geometry
root = tk.Tk()
root.title("Live Rating Update Reaction")
root.geometry("1080x600")
root.configure(background="#181414")

class Labels():
    link = tk.StringVar()
    start_num = 0
    player_text = None
    player_rank = None
    pos_text = None
    neg_text = None
    link_label = None
    link_label = None
    ent_btn = None

#Creates a display that asks for the user to input a player's RatingUpdate Link
#If there is already an instance of this display, destroy it
def inputBox(label):
    if not label.link_label:
        label.link_label = tk.Label(root, text="insert rating update link here:", foreground="#c80404", background="#181414")
        label.link_entry = tk.Entry(root, textvariable=label.link, foreground="#c80404", background="#181414", font=("Arial", 20))
        label.ent_btn = tk.Button(root, text="Enter", command=lambda:[mainScreen(label), inputBox(label)])
        label.link_label.pack()
        label.link_entry.pack()
        label.ent_btn.pack()
    else:
        label.link_label.destroy()
        label.link_entry.destroy()
        label.ent_btn.destroy()

#Deletes the mainScreen ui and puts in a cheerful text with accompanying sounds
#After a certain amount of time, perform the mainScreen function
def updatePos(label):
    if label.player_rank:
        label.player_rank.destroy()
        label.player_text.destroy()
        label.player_rank = None
        label.player_text = None
    if not label.pos_text:
        label.pos_text = tk.Label(root, text="yippee", foreground="white", background="#c80404", font=("Arial", 20), width=1080, height=600)
        label.pos_text.place(anchor=tk.CENTER)
        label.pos_text.pack()
        winsound.PlaySound('right.wav', winsound.SND_FILENAME)
    root.after(10000, lambda:[mainScreen(label)])

#Deletes the mainScreen ui and puts in a negative text with accompanying sounds
#After a certain amount of time, perform the mainScreen function
def updateNeg(label):
    if label.player_rank:
        label.player_rank.destroy()
        label.player_text.destroy()
        label.player_rank = None
        label.player_text = None
    if not label.neg_text:
        label.neg_text = tk.Label(root, text="do better next time", foreground="white", background="#c80404", font=("Arial", 20), width=1080, height=600)
        label.neg_text.place(anchor=tk.CENTER)
        label.neg_text.pack()
        winsound.PlaySound('wrong.wav', winsound.SND_FILENAME)
    root.after(10000, lambda:[mainScreen(label)])

#Grabs the Player info and displays on the screen
#After a certain amount of time, checks to see if the rank has changed, and either calls itself, updatePos, or updateNeg
def mainScreen(label):

    name, info = getInfo(label.link.get())
    info_list = info.split(" ")
    #grabs the rank
    if "Happy" in info_list[0]:
        rank = info_list[2]
    else:
        rank = info_list[1]

    #Creates the player labels if no previous instance is found
    if not label.player_rank:
        label.player_text = tk.Label(root, text=name, foreground="#c80404", background="#181414", font=("Arial", 20), width=60, height=9)
        label.player_rank = tk.Label(root, text=info, foreground="#c80404", background="#181414", font=("Arial", 20), width=60, height=9)
        label.player_rank.place(anchor=tk.CENTER)
        label.player_text.place(anchor=tk.CENTER)
        label.player_rank.pack()
        label.player_text.pack()

    #If an instance is found, renames and updates the info, and kills the pos or neg labels.
    else:
        if label.player_rank:
           label.player_rank.configure(text=info)
        if label.player_text:
            label.player_text.configure(text=name)
        if label.pos_text:
            label.pos_text.destroy()
            label.pos_text = None
        if label.neg_text:
            label.neg_text.destroy()
            label.neg_text = None

    if label.start_num == 0:
        label.start_num = rank
        root.after(1000, lambda:[mainScreen(label)])
    if rank > label.start_num:
        root.after(1000, lambda:[updatePos(label)])
        label.start_num = rank
    elif rank < label.start_num:
        root.after(1000, lambda:[updateNeg(label)])
        label.start_num = rank
    else:
        label.start_num = rank
        root.after(10000, lambda:[mainScreen(label)])

label = Labels()
inputBox(label)
root.mainloop()
