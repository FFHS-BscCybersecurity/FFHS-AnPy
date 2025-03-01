######################################################
# 1. Bestimmen der n-ten Fibonacci-Zahl
######################################################
# Rekursive Implementierung
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

######################################################
# 2. Bestimmen der Anzahl der Funktionsaufrufe
######################################################
# Gleiche Implementierung wie oben kopiert, nur mit zusätzlichem Zähler

# Globale Variable count (nicht empfohlen, aber einfach)
global count
count = 0

def fib_count(n): 
    # Hier nochmals die Variable count als global deklariert, sonst hatte ich Fehler (?)
    global count
    # Erhöhen vom Zähler
    count += 1
    # Für 0 und 1 wird der Rückgabewert direkt zurückgegeben
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        # Rekursiver Aufruf zur Berechnung der Fibonacci-Zahl
        fib = fib_count(n - 1) + fib_count(n - 2)
        # Rückgabe nur des Counters
        return count
    
######################################################
# 3. Ausgabe der Zahlen zum Vergleich (1-20)
######################################################
print("Plotten der Fibonacci-Zahlen und der Funktionsaufrufe")
import matplotlib.pyplot as plt
plt.plot([fib(n) for n in range(1, 20)], label="Fibonacci-Zahlen")
plt.plot([fib_count(n) for n in range(1, 20)], label="Funktionsaufrufe")
plt.legend()
plt.show()
print("-------------------")
######################################################
# 4. Laufzeiten
######################################################

import time # Aufgabenstellung
import timeit # Alternative


print("Rekursive Implementierung:")
# Start
start = time.time()
print(fib(20))
# Ende
end = time.time()
# Ausgabe time
print("Dies ist die Laufzeit des Befehls fib(20) gemessen mit time()")
print("Laufzeit in Sekunden:", end - start)
print("-------------------")
print("Alternative Zeitmessung der selben Implementierung:")
print("Dies ist die Laufzeit des Befehls fib(20) gemessen mit timeit()")
print("Laufzeit in Sekunden:", timeit.timeit("fib(20)", globals=globals(), number=1))
print("-------------------")
######################################################
# Alternative Implementierung
######################################################
# Dieses Mal iterativ
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print("Iterative Implementierung:")   
print(fib_iter(20))

print("Dies ist die Laufzeit des Befehls fib_iter(20) gemessen mit timeit()")
print("Laufzeit in Sekunden:", timeit.timeit("fib_iter(20)", globals=globals(), number=1))

print("-------------------")
######################################################
# 5. Mit Formel von Binet (gefunden durch Recherche im Netz)
######################################################
# Quelle: https://www.datacamp.com/de/tutorial/fibonacci-sequence-python#:~:text=der%20resultierenden%20Matrix.-,Binet%27s%20Formel,-Die%20Formel%20von
import math

def fib_binet(n):
    return round((math.pow((1 + math.sqrt(5)) / 2, n) - math.pow((1 - math.sqrt(5)) / 2, n)) / math.sqrt(5))

print("Formel von Binet:")
print(fib_binet(20))

print("Dies ist die Laufzeit des Befehls fib_binet(20) gemessen mit timeit()")
print("Laufzeit in Sekunden:", timeit.timeit("fib_binet(20)", globals=globals(), number=1))
print("-------------------")
