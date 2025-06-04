from math import sqrt
def is_prime(number: int):
   sq_num = int(sqrt(number))
   zaehler = 2
   while sq_num >= zaehler:
        if sq_num >= zaehler:
            rest = number % zaehler

            if rest == 0:
                return False
            if number == 1:
                return False
            else:
                return True
            
border = 100

for i in range (border):
    checkPrime = is_prime(i)
    if checkPrime:
        print(i, "ist eine Primzahl")