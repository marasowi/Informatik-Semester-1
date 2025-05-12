
würfel = [1, 2, 3, 4, 5, 6]

import random

anzahlwurf = 0

while anzahlwurf < 3 or wurf == 6:
    anzahlwurf += 1
    wurf = random.choice(würfel)  
    print("Wurf" + ":" + str(wurf)) 

    if wurf == 6 :
        anzahlwurf = 3
        print ("Du hast eine 6 geworfen!")
        continue
    
    
# while anzahlwurf < 3 :
#     anzahlwurf += 1
#     wurf = random.choice(würfel)  
#     print("Wurf" + ":" + str(wurf)) 

# while wurf == 6 and anzahlwurf < 3:
#     anzahlwurf += 1
#     wurf = random.choice(würfel)  
#     print("Wurf" + ":" + str(wurf)) 

#     # if wurf == 6 :
#     #     anzahlwurf = 3
#     #     print ("Du hast eine 6 geworfen!")
#     #     continue