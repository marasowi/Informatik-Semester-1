from math import sqrt

def is_prime(number: int):
    if number < 2:
        return False
    for zaehler in range(2, int(sqrt(number)) + 1):
        if number % zaehler == 0:
            return False
    return True

border = 100

for i in range(border):
    if is_prime(i):
        print(i, "ist eine Primzahl")