from Temperaturumrechnung import celsius_to_kelvin, celsius_to_fahrenheit

celsius = float(input("Geben Sie die Temperatur in Celsius ein: "))
fahrenheit = celsius_to_fahrenheit(celsius)
kelvin = celsius_to_kelvin(celsius)

print(f"Die Temperatur in Fahrenheit beträgt: {fahrenheit}")
print(f"Die Temperatur in Kelvin beträgt: {kelvin}")
