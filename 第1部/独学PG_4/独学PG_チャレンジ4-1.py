def square():
    a = input("type a number : ")
    #input時点では"a"はstrのため、キャストする
    a = int(a)
    return a ** 2

def show_message(msg):
    print(msg)

def use_optinparam(a, b, c, d = 10, e = 20):
    return a + b + c + d + e
    
# result = square()
# show_message("出力してください")


#一部のオプション引数だけ設定する
result = use_optinparam(1, 2, 3, e= 5)
print(result)