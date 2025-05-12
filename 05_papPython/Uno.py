kartenstapel = ["gr7", "+4", "gl2"]
#Nachziehstapel mit 3 Karten, im Speicher so dargestellt mit Farbe und Zahl oder zahl
while len(kartenstapel) != 0:
    #kartenstapel.count zählt wie viele Karten man noch hat hier: 3 und != heißt ungleich null
    #len heißt so lang die länge ungleich null ist
    print(kartenstapel)
    aktuelleKarte = kartenstapel.pop(0)

    if aktuelleKarte == "+4" :
        print("+4 kann gespielt werden.")
    #== heißt es wird überprüft ob etwas gleich ist
    #Einfache Variante da uno mit ob die karte auf dem stapel zur gezogenen passt ist zu kompliziert
        break
if len(kartenstapel) == 0 :
    print("Stapel ist leer")    
#If st ne verzweigung und kann nicht wieder zurück gehen (nach oben), while kann auch wieder zurück (nach obene gehen) (Unterscheid der Schleifen)
#while ist schleife, loop
#If ist eine Verzweigung

