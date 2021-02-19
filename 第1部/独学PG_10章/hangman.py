import random

def hangman(word):
    # プレイヤー２が間違えた回数
    wrongcnt = 0
    stages = ["",
              "_______        ",
              "|              ",
              "|       |      ",
              "|       O      ",
              "|      /|\     ",
              "|      / \     "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    # プレイヤー2がハングマンを完成させてしまったらゲーム終了
    # 「stagesの要素は0始まり/wrongは1始まり」のため-1する。
    while wrongcnt < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            print("当たり")
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            print("ハズレ")
            wrongcnt += 1

        # 勝敗の判定
        print(" ".join(board))
        e = wrongcnt + 1
        print("\n".join(stages[0:e]))
        if  "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win = True
            break
    
    if not win:
        print("あなたは負け")
words = ["dog", "cat", "cow", "car", "pig"]

index = random.randint(0,len(words))
hangman(words[index])