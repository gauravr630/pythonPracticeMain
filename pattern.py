x = int(input("enter the number"))
num = 1
for i in range(1, x):
    num = num * i
print(num)


def prime(a):
    count = 0
    for i in range(2, a):
        if a % i == 0:
            count += 1

    if count >= 1:
        print(a, "not a prime number")
    else:
        print(a, "is a prime number")


def even_odd(a):
    if a % 2 == 0:
        print(a, "is even")
    else:
        print(a, "is odd")


prime(23)
even_odd(23)
