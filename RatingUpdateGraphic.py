import tkinter as tk
import winsound
from urllib.request import urlopen

start_num = 0
player_name = ""
root = tk.Tk()
root.title("Live Rating Update Reaction")
root.geometry("1080x600")
root.configure(background="#181414")
link = tk.StringVar()
player_text = None
player_rank = None
link_label = None
link_entry = None
ent_btn = None
pos_text = None
neg_text = None
testbut = None


def inputBox():
    global link
    global link_label
    global link_entry
    global ent_btn
    if not link_label:
        link_label = tk.Label(root, text="insert rating update link here:", foreground="#c80404", background="#181414")
        link_entry = tk.Entry(root, textvariable=link, foreground="#c80404", background="#181414", font=("Arial", 20))
        ent_btn = tk.Button(root, text="Enter", command=lambda: [findPlayer(), inputBox()])
        link_label.pack()
        link_entry.pack()
        ent_btn.pack()
    else:
        link_label.destroy()
        link_entry.destroy()
        ent_btn.destroy()


def updatePos():
    global pos_text
    global player_text
    global player_rank
    # kill player rank and text
    if player_rank:
        player_rank.master.destroy()
        player_text.master.destroy()
    if not pos_text:
        pos_text = tk.Label(root, text="you're did it", foreground="white", background="#c80404", font=("Arial", 20), width=1080, height=600)
        pos_text.place(anchor=tk.CENTER)
        pos_text.pack()
        winsound.PlaySound('right.wav', winsound.SND_FILENAME)
    root.after(15000, findPlayer)


def updateNeg():
    global neg_text
    global player_text
    global player_rank
    # kill player rank and text
    if player_rank:
        player_rank.destroy()
        player_text.destroy()
    if not neg_text:
        neg_text = tk.Label(root, text="you're bad lol", foreground="white", background="#c80404", font=("Arial", 20), width=1080, height=600)
        neg_text.place(anchor=tk.CENTER)
        neg_text.pack()
        winsound.PlaySound('wrong.wav', winsound.SND_FILENAME)
    root.after(15000, findPlayer)


def findPlayer():
    global start_num
    global player_name
    global player_text
    global player_rank
    global link
    global neg_text
    global pos_text
    global testbut
    # opens the profile page of the player
    profile_url = link.get()
    profile_page = urlopen(profile_url)

    # reads and converts the page to a really long string
    html_bytes = profile_page.read()
    html = html_bytes.decode("utf-8")

    # splits the string into lists to find the player's name and rank
    # splits the line that contains the player's name and rank
    html_split = html.splitlines()
    player_line = html_split[6]
    player_split = player_line.split("\"")
    # player is the name and rank
    player = player_split[3]
    shitfart = player.split(" - ")
    # poop is the current rank
    poop = shitfart[1]
    player_name = shitfart[0]

    if not player_rank:
        player_rank = tk.Label(root, text=poop, foreground="#c80404", background="#181414", font=("Arial", 20), width=60, height=9)
        player_text = tk.Label(root, text=player_name, foreground="#c80404", background="#181414", font=("Arial", 20), width=60, height=9)
        player_rank.place(anchor=tk.CENTER)
        player_text.place(anchor=tk.CENTER)
        player_rank.pack()
        player_text.pack()
    else:
        if player_rank:
            player_rank.configure(text=poop)
        if player_text:
            player_text.configure(text=player_name)
        if pos_text:
            pos_text.destroy()
        if neg_text:
            neg_text.destroy()

    if not testbut:
        testbut = tk.Button(root, text="Enter", command=updateNeg)
        testbut.pack()

    if start_num == 0:
        start_num = poop
        root.after(1000, findPlayer)
    if poop > start_num:
        print("good job")
        root.after(1000, updatePos)
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
