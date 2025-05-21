from energiekosten import berechne_kosten
tarife = {
    "Erdgas": 0.09,
    "Heizöl": 0.11,
    "Strom": 0.30
}

print ("Heizkostenabschätzug, wähle den Energieträger")
print ("Für Erdgas drücken Sie 1")
print ("Für Heizöl drücken Sie 2")
print ("Für Strom drücken Sie 3")

Energieträger = input("Bitte wählen Sie den Energieträger (1, 2 oder 3): ")
if Energieträger == "1":
    energieträger = "Erdgas"
elif Energieträger == "2": 
    energieträger = "Heizöl"
elif Energieträger == "3":
    energieträger = "Strom"

lesitung = float(input("Bitte geben Sie die Heizleistung in kWh ein: "))

dauer = float(input("Bitte geben Sie die Dauer in Stunden ein: "))

energei_kwh = lesitung * dauer

tarif = tarife[energieträger]

kosten = berechne_kosten(energei_kwh, tarif)

print(f"Die Heizkosten betragen {kosten} Euro.")