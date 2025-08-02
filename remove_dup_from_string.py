import pytest
text= "gauravisaboynotagirl"

def remove_dupl(text):
    set1=set(text)
    print(set1)


remove_dupl(text)

def sum1():
    a=2
    b=4
    sum=a+b
    print(sum)
    assert sum==7, "sum is 6"
sum1()