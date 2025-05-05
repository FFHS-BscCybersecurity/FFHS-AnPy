from math import sin

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


# Generiere Koordinatenpunkte
x_genau = np.linspace(0, 2 * np.pi, 100)
y_genau = np.sin(x_genau)

# Festlegen der Koordinatenpunkte (Stützpunkte)
# ---
## Hier sind vier Punkte angegeben. Wenn mehr Punkte gewählt werden, wird die Approximation immer genauer (z.b. siehe bei Wahl von 10)
x_koordinate = np.linspace(0, 2 * np.pi, 4)
y_koordinate = np.sin(x_koordinate)

# Erstellt die Approximation mittels "CubicSpline" aus sympy
cs = CubicSpline(x_koordinate, y_koordinate)

# Generiert y-Werte für die Spline-Approximation
y_spline = cs(x_genau)

# Zeichnet die Funktion, Stützpunkte und Approximation
plt.figure(figsize=(10, 6))
plt.plot(x_genau, y_genau, label='Funktion', color='blue')
plt.plot(x_genau, y_spline, label='Approximation', color='red', linestyle='--')
plt.scatter(x_koordinate, y_koordinate, label='Stützpunkte', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximation einer nichtlinearen Kurve (Kubischer Spline)')
plt.legend()
plt.grid(True)
plt.show()
