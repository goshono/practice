# def f():
#     x = 1
#     y = 2
#     z = 3
#     print(x)
#     print(y)
#     print(z)

# f()

x = 100

def f():
    global x
    x += 1
    print(x)

f()