import tkinter as tk
import winsound
from webread import getInfo

start_num = 0
root = tk.Tk()
root.title("Live Rating Update Reaction")
root.geometry("1080x600")
root.configure(background="#181414")
link = tk.StringVar()
player_text = None
player_rank = None
pos_text = None
neg_text = None
testbut = None

def destruct(uilist):
    for ui in range(len(uilist)):
        uilist[ui].destroy()
        uilist[ui] = None
    return uilist

def inputBox():
    global link
    global link_label
    link_label = tk.Label(root, text="insert rating update link here:", foreground="#c80404", background="#181414")
    link_entry = tk.Entry(root, textvariable=link, foreground="#c80404", background="#181414", font=("Arial", 20))
    ent_btn = tk.Button(root, text="Enter", command=lambda:[destruct(inputUI), findPlayer()])
    inputUI = [link_label, link_entry, ent_btn]
    link_label.pack()
    link_entry.pack()
    ent_btn.pack()


def updatePos():
    global pos_text
    global player_text
    global player_rank
    # kill player rank and text
    if player_rank:
        player_rank.destroy()
        player_text.destroy()
        player_rank = None
        player_text = None
    if not pos_text:
        pos_text = tk.Label(root, text="you're did it", foreground="white", background="#c80404", font=("Arial", 20), width=1080, height=600)
        pos_text.place(anchor=tk.CENTER)
        pos_text.pack()
        winsound.PlaySound('right.wav', winsound.SND_FILENAME)
    root.after(15000, findPlayer)


def updateNeg():
    global neg_text
    neg = [neg_text]
    # kill player rank and text
    if not neg_text:
        neg_text = tk.Label(root, text="you're bad lol", foreground="white", background="#c80404", font=("Arial", 20), width=1080, height=600)
        neg_text.place(anchor=tk.CENTER)
        neg_text.pack()
        winsound.PlaySound('wrong.wav', winsound.SND_FILENAME)
    root.after(15000, lambda:[destruct(neg),findPlayer()])


def findPlayer():
    global player_text
    global player_rank
    global link
    global neg_text
    global link_label
    global pos_text
    global testbut
    global start_num

    if link_label is None:

        print("thing works")

    poop, player_name = getInfo(link.get())

    if not player_rank:
        player_rank = tk.Label(root, text=poop, foreground="#c80404", background="#181414", font=("Arial", 20), width=60, height=9)
        player_text = tk.Label(root, text=player_name, foreground="#c80404", background="#181414", font=("Arial", 20), width=60, height=9)
        player_rank.place(anchor=tk.CENTER)
        player_text.place(anchor=tk.CENTER)
        player_rank.pack()
        player_text.pack()
        playerUI = [player_rank, player_text]

    else:
        if player_rank:
           player_rank.configure(text=poop)
        if player_text:
            player_text.configure(text=player_name)
        if pos_text:
            pos_text.destroy()
            pos_text = None
        if neg_text:
            neg_text.destroy()
            neg_text = None

    if not testbut:
        testbut = tk.Button(root, text="Enter", command=lambda:[updateNeg(), destruct(playerUI)])
        testbut.pack()

    if start_num == 0:
        start_num = poop
        root.after(1000, findPlayer)
    if poop > start_num:
        print("good job")
        root.after(1000, lambda:[updatePos(), destruct(playerUI)])
        start_num = poop
    elif poop < start_num:
        print("youre ass")
        root.after(1000, updateNeg)
        start_num = poop
    else:
        start_num = poop
        root.after(10000, findPlayer)

inputBox()
root.mainloop()
