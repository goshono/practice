# shows = ["Got", "Narcos", "Vice"]
# # for show in shows:
#     # print(show)

# coms = ("A.Development", "Friends", "Always Sunny")
# for show in coms:
#     print(show)

# people = {"G.Bluth Ⅱ" : "A. Development",
#           "Batney" : "HIMNYM",
#           "Dennis" : "Always Sunny"}
# for char in people:
#      print(char)

tv = ["GOT", "Narcos", "Vice"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)