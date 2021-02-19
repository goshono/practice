musicians = ["Mr.Children", "Greeeen", "ゆず"]
# print(musicians)

tuple1 = ("愛知県", "岡崎市")
tuple2 = ("北海道", "富良野市")
tuples = [tuple1, tuple2]
# print(tuples)

my_features = {"height" : 177.1,
               "weight" : 64,
               "好きな色" : "navy"}

# print(my_features)

key = input("私の何について知りたいですか？：")
if key in my_features:
    print(my_features[key])
else:
    print("ひみつ")
