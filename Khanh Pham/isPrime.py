from math import *

n = int(input("Enter number: "))

def checkPrime(n):
    if n < 2:
        return False
    i = int(sqrt(n))
    num = []
    for m in range(0, i + 1):
        num.append(True)
    for m in range(2, i + 1):
        if num[m] is True:
            if n % m == 0:
                return False
                break
            for x in range(0, int(i / m)):
                num[(x * m)] = False
    return True

print(checkPrime(n))
