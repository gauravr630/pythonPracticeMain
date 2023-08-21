x = "this is my new project"
arr = x.split(" ")
print(arr[0])
print(len(arr))


def revrs(s):
    rev = ""
    for i in s:
        rev = i + rev
    print(rev)


for i in range(0, len(arr)):
    revrs(arr[i])
