from math import *

a = int(input("Enter number: "))
def fibN(a):
    n1 = 0
    n2 = 1
    n3 = 1
    for x in range(0, a - 1):
        if x == 0 or x == 1:
            print(1)
        else:
            n1 = n2 + n3
            n2 = n3
            n3 = n1
            print(n3)


print(fibN(a))


