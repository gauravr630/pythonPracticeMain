def even_odd(x):
    num = x % 2
    if num == 0:
        print(x, "is even")
    else:
        print(x, "is odd")


def fact(x):
    f = 1
    for i in range(1, x + 1):
        f = i * f
        # print(f)
    print(f)


def rep_sp(str):
    ch = ""
    for i in str:
        if i != " ":
            ch = ch + i
    print(ch)


even_odd(25)
fact(5)
rep_sp("this is new room")

rep_sp("this is new room not ur room")

rep_sp("learning python first time and git")