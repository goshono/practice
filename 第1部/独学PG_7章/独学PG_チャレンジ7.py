# dolamas = ["教師びんびん物語", "スクールウォーズ", "やまとなでしこ", "HERO"]

# for i, dolama in enumerate(dolamas):
#     print(str(i) + " : " + dolamas[i])

# for i in range (25, 51):
#     print(i)

pitchers  = [11, 12, 14, 16, 18, 19]

while True:
    guess = input("type a number : ")
    if guess == "q":
        break

    try:
        if int(guess) in pitchers:
            print("正解！")
        else:
            print("不正解。。")
    except ValueError:
        print("数字を入力するか、qで終了します。")

