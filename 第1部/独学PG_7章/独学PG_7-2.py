tv = ["GOT", "Narcons", "Vice"]
coms = ["Arrested Development", "friends", "Always Sunny"]

all_shows = []

# for i , new in enumerate(tv):
#     new = tv[i]
#     new = new.upper()
#     tv[i] = new

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

