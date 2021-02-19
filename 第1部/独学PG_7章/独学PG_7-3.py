# x = 10
# while x > 0:
#     print('今は{}です。'.format(x))
#     x -= 1

# print("Happy New Year")

# for i in range(1, 11):
    # print(i)

# questions = ["what is your name?",
#              "what is your fav. color?",
#              "what is your quest?"]
# n = 0
# while True:
#     print("Type q to quit")
#     a = input(questions[n])
#     if a == "q":
#         break
    
#     # 0 → 1 → 2 → 0 → 1 ...
#     n = (n + 1) % 3

# continue と break の違いは、反復処理を継続するか否か
for i in range(1, 6):
    if i == 3:
        continue

    # continue が実行されると以降のコードは実行されない
    print(i)