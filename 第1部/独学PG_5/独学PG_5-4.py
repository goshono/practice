locations = []

# これはタプルです。変更不可（イミュータブル）です
la = (34.0522, 188.2437)
chicago = (41.8731, 87.6928)

locations.append(la)
locations.append(chicago)

print(locations)

eights = ["田中さん", "佐藤くん"]
nines = ["東野圭吾", "北方謙三"]

authors = (eights, nines)
print(authors)


birhtday = {"山田哲人" : 1992,
            "中村悠平" : 1990}

my_list = [birhtday]
# print(my_list)
my_tuple = (my_list, )
print(my_tuple)