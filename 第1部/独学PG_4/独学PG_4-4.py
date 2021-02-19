# オプション引数はデフォルト値を設定する
def f(x=2):
    return x ** x

print(f())
print(f(4))