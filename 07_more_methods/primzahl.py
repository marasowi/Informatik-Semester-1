from math import sqrt
def is_prime(number: int) -> bool:
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
            
print(is_prime(1))
print(is_prime(12))
print(is_prime(13))
print(is_prime(7))
print(is_prime(22))
print(is_prime(27))