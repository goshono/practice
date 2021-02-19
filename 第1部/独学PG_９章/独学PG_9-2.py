# ファイルのオープン時に閉じ忘れを防止する
with open ("st.txt", "w") as f:
    f.write("Hi from python with")
    #with内のコード実行後に自動的にファイルが閉じられる