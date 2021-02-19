author = "Kafka"
strings = author * 3

print("WE ARE THE SWALLOWS".capitalize())

msg = "水たまりを飛び越えたんだ。3メートルもあったんぜ!".split("。")
# print(msg)
# splitした結果はリストとして保持される
# print(msg[0])

first_three = "abc"
result = "+".join("abc")
# print(result)

words = ["the", "fox", "jumped",
         "over", "the", "fence", "."]
one = "".join(words)
print(one)

two = " ".join(words)
print(two)

three = two.capitalize()
# print(three)

s = "   The   "
# s = s.strip()
# print(s)

# c = input("type char :")
# try:
#     print("animals".index(c))
# except ValueError:
#     print("Not found")

# print("Cat" not in "Cat in the hat.")

# print("彼女は\"そうだね\"と言った")
print('彼女は"そうだね"と言った')
print("line1\nline2\nline3")

