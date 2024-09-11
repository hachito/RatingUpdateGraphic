from urllib.request import urlopen

profile_url = "https://puddle.farm/player/2EC4144135C48F8/MI"
# profile_url = "https://puddle.farm/player/2EC3DA787FC83DA/FA"
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
print(player_split)
player = player_split[3]
print(player)
shitfart = player.split(" ")
poopfart = player.split(" - ")
# poop is the current rank
poop = (shitfart[3])
print(poopfart)