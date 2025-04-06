## Pythonfunktion um die Teilsummen der allgemeinen harmonischen Reihe in Abhängigkeit der Anzahl Summenglieder, n, zu berechnen.

def HarmonischeReiheBerechnen(summenglieder):
    summe = 0
    # Berechnung des Wertes, indem die Summe der Kehrwerte der Zahlen von 1 bis zur gewünschten Anzahl der
    # Summenglieder berechnet wird
    for position in range(1, summenglieder + 1):
        summe = summe + 1 / position
    return summe


# Test
print(HarmonischeReiheBerechnen(3))

# Stelle die harmonische Reihe für die Anzahl Summenglieder von 1 bis 10 dar mittels mathpltlib
import matplotlib.pyplot as plt
import numpy as np

# Anzahl der Summenglieder
n = np.arange(1, 11, 1)
# Berechnung der Teilsummen

summen = [HarmonischeReiheBerechnen(i) for i in n]
plt.plot(n, summen, 'o-')
plt.xlabel('Anzahl Summenglieder')
plt.ylabel('Wert der Teilsumme')
plt.title('Wert der Teilsumme der harmonischen Reihe')
plt.show()


import matplotlib.pyplot as plt
import numpy as np

def AllgemeineHarmonischeReiheBerechnen(summenglieder, p):
    summe = 0
    for position in range(1, summenglieder + 1):
        summe += 1 / (position ** p)
    return summe

# Anzahl der Summenglieder
n = np.arange(1, 101, 1)

# Verschiedene Werte des Exponenten p
p_values = [0.5, 1, 1.5, 2]

plt.figure(figsize=(10, 6))

for p in p_values:
    summen = [AllgemeineHarmonischeReiheBerechnen(i, p) for i in n]
    plt.plot(n, summen, label=f'p = {p}')

plt.xlabel('Anzahl Summenglieder')
plt.ylabel('Wert der Teilsumme')
plt.title('Konvergenz-/Divergenzverhalten der allgemeinen harmonischen Reihe')
plt.legend()
plt.yscale('log')  # Logarithmische Skala für bessere Visualisierung
plt.show()

