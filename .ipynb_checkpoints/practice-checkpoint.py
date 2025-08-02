m= "abc"
n = " "
u=n+m
print(u)

x = input("enter the string")
str = x
print("string is :" + str)
rev = ""
for i in str:
    rev = i+rev
    print(rev)
print(rev)


for i in range(1, 10):
    for j in range(1, i):
        print("*", end=" ")
    print()
