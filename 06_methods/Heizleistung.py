breite = float(input("Geben Sie die Breite des Raumes in Metern ein: "))
laenge = float(input("Geben Sie die Länge des Raumes in Metern ein: "))
hoehe = float(input("Geben Sie die Höhe des Raumes in Metern ein: "))
temperatur_innen = float(input("Geben Sie die Temperatur in Grad Celsius ein: "))
temperatur_aussen = float(input("Geben Sie die Außentemperatur in Grad Celsius ein: "))
#breite höhe und länge defnieren und als input von benutzer eintragen lassen
volumen = breite * laenge * hoehe
#volumen brechnen in m3
dt = temperatur_innen - temperatur_aussen
# dt = Temperaturdifferenz
if dt < 0:
    print("Die Innentemperatur ist niedriger als die Außentemperatur.")

Heizleistung = volumen * dt * 0.024
print(f"Die Heizleistung beträgt {Heizleistung} kw")
# Heizleistung in kw
