

# import random

# würfel = ["pasch", "kein pasch"]

# while True:
#     operation = input("Wie wollen Sie vorgehen? (Zahlen/Würfeln): ")
    
#     if operation == "Zahlen":
#         print("Sie haben sich entschieden zu zahlen. Sie sind frei")
#         break
    
#     elif operation == "Würfeln":
#         anzahlwurf = 0
#         while anzahlwurf < 3:
#             anzahlwurf += 1
#             würfelergebnis = random.choice(würfel)
#             print("Sie haben geworfen:" + str(würfelergebnis))
            
#             if würfelergebnis == "pasch":
#                 print("Sie haben einen Pasch geworfen. Sie sind frei!")
#                 break

#         else:
#             print("Sie haben dreimal geworfen und keinen Pasch erzielt. Sie müssen zahlen.")
#         break

#     else:
#         print("Ungültige Eingabe. Bitte wählen Sie 'Zahlen' oder 'Würfeln'.")

import random

def würfeln():
    return random.randint(1, 6)  

while True:
    operation = input("Wie wollen Sie vorgehen? (Zahlen/Würfeln): ")
    
    if operation == "Zahlen":
        print("Sie haben sich entschieden zu zahlen. Sie sind frei.")
        break
    
    elif operation == "Würfeln":
        anzahlwurf = 0
        while anzahlwurf < 3:
            anzahlwurf += 1
            wurf1 = würfeln()
            wurf2 = würfeln()
            print("Wurf" + str(anzahlwurf) + ": Würfel 1 =" + str(wurf1) + ", Würfel 2 = " + str(wurf2))
            
            if wurf1 == wurf2:  
                print("Sie haben einen Pasch geworfen! Sie sind frei!")
                break
        else:
            print("Sie haben dreimal geworfen und keinen Pasch erzielt. Sie müssen zahlen.")
        break

    else:
        print("Ungültige Eingabe. Bitte wählen Sie 'Zahlen' oder 'Würfeln'.")